import pandas as pd
import numpy as np
from faker import Faker
import random
import os

fake = Faker()

random.seed(42)
np.random.seed(42)

# Create folders if not exist
os.makedirs("data/raw", exist_ok=True)

NUM_MEMBERS = 1000
NUM_CLAIMS = 5000

procedure_codes = {
    "mammogram": ["77067", "77066"],
    "diabetes_a1c": ["83036"],
    "wellness_visit": ["G0438", "G0439"],
    "colorectal_screening": ["45378", "82270"],
    "office_visit": ["99213", "99214"]
}

diagnosis_codes = {
    "diabetes": ["E11.9", "E10.9"],
    "hypertension": ["I10"],
    "general": ["Z00.00"]
}

members = []

# Generate members
for i in range(1, NUM_MEMBERS + 1):
    members.append({
        "member_id": f"M{i:05d}",
        "first_name": fake.first_name(),
        "last_name": fake.last_name(),
        "gender": random.choice(["M", "F"]),
        "date_of_birth": fake.date_of_birth(minimum_age=18, maximum_age=85),
        "plan_type": random.choice([
            "Medicare Advantage",
            "Employer Sponsored",
            "Medicaid"
        ]),
        "provider_id": f"P{random.randint(1, 50):03d}"
    })

members_df = pd.DataFrame(members)

claims = []

# Generate claims
for i in range(1, NUM_CLAIMS + 1):

    member = members_df.sample(1).iloc[0]

    procedure_category = random.choice(list(procedure_codes.keys()))
    diagnosis_category = random.choice(list(diagnosis_codes.keys()))

    claims.append({
        "claim_id": f"C{i:06d}",
        "member_id": member["member_id"],
        "claim_date": fake.date_between(start_date="-2y", end_date="today"),
        "claim_type": random.choice([
            "inpatient",
            "outpatient",
            "pharmacy",
            "professional"
        ]),
        "diagnosis_code": random.choice(
            diagnosis_codes[diagnosis_category]
        ),
        "procedure_code": random.choice(
            procedure_codes[procedure_category]
        ),
        "paid_amount": round(random.uniform(50, 10000), 2),
        "provider_id": member["provider_id"]
    })

claims_df = pd.DataFrame(claims)

# Save CSV files
members_df.to_csv("data/raw/members.csv", index=False)
claims_df.to_csv("data/raw/claims.csv", index=False)

print("Healthcare sample data generated successfully!")
print("Members Shape:", members_df.shape)
print("Claims Shape:", claims_df.shape)