import sqlite3
import pandas as pd
import os

# Get project root folder
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DB_PATH = os.path.join(BASE_DIR, "data", "processed", "healthcare_claims.db")
SQL_FILE_PATH = os.path.join(BASE_DIR, "sql", "01_create_tables.sql")
MEMBERS_CSV_PATH = os.path.join(BASE_DIR, "data", "raw", "members.csv")
CLAIMS_CSV_PATH = os.path.join(BASE_DIR, "data", "raw", "claims.csv")

os.makedirs(os.path.join(BASE_DIR, "data", "processed"), exist_ok=True)

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

with open(SQL_FILE_PATH, "r") as file:
    cursor.executescript(file.read())

members_df = pd.read_csv(MEMBERS_CSV_PATH)
claims_df = pd.read_csv(CLAIMS_CSV_PATH)

members_df.to_sql("members", conn, if_exists="append", index=False)
claims_df.to_sql("claims", conn, if_exists="append", index=False)

conn.commit()
conn.close()

print("Database created successfully!")
print("Tables loaded: members and claims")
print("Database saved at:", DB_PATH)