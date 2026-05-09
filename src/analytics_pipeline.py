import sqlite3
import pandas as pd
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DB_PATH = os.path.join(BASE_DIR, "data", "processed", "healthcare_claims.db")
REPORTS_DIR = os.path.join(BASE_DIR, "reports")

os.makedirs(REPORTS_DIR, exist_ok=True)

print("Using database:", DB_PATH)

conn = sqlite3.connect(DB_PATH)

# Check tables first
tables_check = pd.read_sql_query(
    "SELECT name FROM sqlite_master WHERE type='table';",
    conn
)

print("Tables found:")
print(tables_check)

if "members" not in tables_check["name"].values or "claims" not in tables_check["name"].values:
    conn.close()
    raise Exception(
        "members or claims table not found. Please run load_database.py first."
    )

care_gap_query = """
SELECT
    m.member_id,
    m.first_name,
    m.last_name,
    m.gender,
    m.date_of_birth,
    m.plan_type,

    CASE
        WHEN m.gender = 'F'
        AND CAST((julianday('now') - julianday(m.date_of_birth)) / 365.25 AS INTEGER)
            BETWEEN 50 AND 74
        AND m.member_id NOT IN (
            SELECT member_id
            FROM claims
            WHERE procedure_code IN ('77067', '77066')
        )
        THEN 'Overdue Mammogram'

        WHEN m.member_id IN (
            SELECT member_id
            FROM claims
            WHERE diagnosis_code LIKE 'E11%'
        )
        AND m.member_id NOT IN (
            SELECT member_id
            FROM claims
            WHERE procedure_code = '83036'
        )
        THEN 'Overdue Diabetes A1C Screening'

        WHEN CAST((julianday('now') - julianday(m.date_of_birth)) / 365.25 AS INTEGER) >= 65
        AND m.member_id NOT IN (
            SELECT member_id
            FROM claims
            WHERE procedure_code IN ('G0438', 'G0439')
        )
        THEN 'Overdue Wellness Visit'

        ELSE 'No Gap'
    END AS care_gap

FROM members m;
"""

care_gaps_df = pd.read_sql_query(care_gap_query, conn)

care_gaps_df = care_gaps_df[care_gaps_df["care_gap"] != "No Gap"]

care_gaps_df["priority_score"] = care_gaps_df["care_gap"].map({
    "Overdue Diabetes A1C Screening": 95,
    "Overdue Mammogram": 85,
    "Overdue Wellness Visit": 75
})

care_gaps_df.to_csv(
    os.path.join(REPORTS_DIR, "care_gap_report.csv"),
    index=False
)

utilization_query = """
SELECT
    claim_type,
    COUNT(*) AS total_claims,
    ROUND(SUM(paid_amount), 2) AS total_paid_amount,
    ROUND(AVG(paid_amount), 2) AS avg_paid_amount
FROM claims
GROUP BY claim_type
ORDER BY total_paid_amount DESC;
"""

utilization_df = pd.read_sql_query(utilization_query, conn)

utilization_df.to_csv(
    os.path.join(REPORTS_DIR, "utilization_summary.csv"),
    index=False
)

procedure_cost_query = """
SELECT
    procedure_code,
    COUNT(*) AS total_services,
    ROUND(SUM(paid_amount), 2) AS total_cost,
    ROUND(AVG(paid_amount), 2) AS average_cost
FROM claims
GROUP BY procedure_code
ORDER BY total_cost DESC;
"""

procedure_df = pd.read_sql_query(procedure_cost_query, conn)

procedure_df.to_csv(
    os.path.join(REPORTS_DIR, "procedure_cost_summary.csv"),
    index=False
)

conn.close()

print("Care gap report generated.")
print("Utilization summary generated.")
print("Procedure cost summary generated.")
print("Analytics pipeline completed successfully.")