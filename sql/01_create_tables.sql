DROP TABLE IF EXISTS members;
DROP TABLE IF EXISTS claims;

CREATE TABLE members (
    member_id TEXT PRIMARY KEY,
    first_name TEXT,
    last_name TEXT,
    gender TEXT,
    date_of_birth DATE,
    plan_type TEXT,
    provider_id TEXT
);

CREATE TABLE claims (
    claim_id TEXT PRIMARY KEY,
    member_id TEXT,
    claim_date DATE,
    claim_type TEXT,
    diagnosis_code TEXT,
    procedure_code TEXT,
    paid_amount REAL,
    provider_id TEXT,
    FOREIGN KEY (member_id) REFERENCES members(member_id)
);