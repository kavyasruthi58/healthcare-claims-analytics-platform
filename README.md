# AI-Powered Healthcare Claims Analytics Platform

An end-to-end healthcare analytics platform built using Python, SQL, and Tableau to analyze healthcare claims data, identify preventive care gaps, monitor utilization trends, and generate population health insights.

This project simulates real-world healthcare analytics workflows commonly used by healthcare organizations, insurance providers, Medicare Advantage plans, and population health management teams.

---

# Project Highlights

- Built a healthcare claims analytics pipeline using Python and SQL
- Performed preventive care gap identification using cohort-based analytics
- Generated utilization and procedure cost reports from claims data
- Developed interactive Tableau dashboards for healthcare KPI reporting
- Simulated real-world healthcare workflows used in payer and population health analytics
- Implemented analytics pipelines supporting preventive outreach prioritization

---

# Business Problem

Healthcare organizations and insurance providers often struggle to identify members overdue for preventive services such as:

- Mammograms
- Diabetes screenings
- Annual wellness visits

Delayed preventive care can increase healthcare costs and negatively impact patient outcomes.

This platform addresses that challenge by analyzing claims and member datasets to identify care gaps, generate outreach-ready reports, and visualize population health trends.

---

# Solution Overview

The platform consists of three major layers:

## 1. Data Layer

Simulated healthcare datasets including:

- Member demographics
- Claims data
- Procedure records
- Preventive care indicators

Technologies:
- Python
- SQLite
- SQL

---

## 2. Analytics Layer

Implemented healthcare analytics workflows including:

- Preventive care gap identification
- Cohort-based analysis
- Utilization trend analysis
- Procedure cost analysis
- Population health reporting

Technologies:
- Pandas
- NumPy
- SQL queries

---

## 3. Visualization Layer

Developed Tableau dashboards to visualize:

- Care gap distribution
- Insurance plan comparison
- Preventive screening trends
- Population health KPIs
- Healthcare utilization metrics

Technologies:
- Tableau Public

---

# Technology Stack

| Category | Technologies |
|---|---|
| Programming | Python, SQL |
| Data Processing | Pandas, NumPy |
| Database | SQLite |
| Visualization | Tableau Public |
| Data Generation | Faker |
| Version Control | Git, GitHub |

---

# Project Architecture

```text
Healthcare Claims Data
        ↓
SQL Data Processing
        ↓
Python Analytics Pipeline
        ↓
Care Gap Identification
        ↓
Population Health Reporting
        ↓
Tableau Dashboard Visualization
```

---

# Key Features

## Preventive Care Gap Identification
Detects members overdue for preventive healthcare services using claims and utilization history.

## Population Health Analytics
Analyzes healthcare trends across:
- Medicare Advantage
- Medicaid
- Employer-sponsored plans

## Utilization Reporting
Generates insights into:
- Healthcare service utilization
- Procedure frequency
- Cost trends

## Interactive Dashboarding
Provides visual analytics dashboards for healthcare KPI monitoring and reporting.

---

# Project Structure

```bash
healthcare_claims_analytics/

│── data/
│   ├── raw/
│   │   ├── claims.csv
│   │   └── members.csv
│   │
│   └── processed/

│── reports/
│   ├── care_gap_report.csv
│   ├── utilization_summary.csv
│   └── procedure_cost_summary.csv

│── sql/
│   └── 01_create_tables.sql

│── src/
│   ├── generate_sample_data.py
│   ├── load_database.py
│   └── analytics_pipeline.py

│── requirements.txt
│── main.py
│── README.md
```

---

# Analytics Outputs

## Care Gap Report
Identifies members overdue for:
- Mammograms
- Diabetes A1C screenings
- Annual wellness visits

## Utilization Summary
Provides:
- Utilization counts
- Service category trends
- Healthcare usage insights

## Procedure Cost Summary
Analyzes:
- Total procedure costs
- Average claim amounts
- High-cost procedures

---

# Tableau Dashboard Insights

The Tableau dashboard enables healthcare analytics visualization including:

- Preventive care gap distribution
- Insurance plan-based comparisons
- Population health monitoring
- Healthcare KPI tracking
- Claims utilization analysis

---

# Sample Dashboard Components

- Preventive Care Gap Pie Chart
- Insurance Plan Comparison Bar Chart
- Healthcare KPI Dashboard
- Utilization Trend Reports

---

# Future Enhancements

Planned future improvements include:

- Streamlit web application integration
- OpenAI-powered healthcare analytics chatbot
- Natural language querying of claims data
- HEDIS measure expansion
- Real CMS Medicare dataset integration
- Predictive healthcare risk scoring
- Machine learning-based utilization forecasting

---

# Real-World Relevance

This project mirrors real healthcare analytics workflows commonly used in:

- Healthcare insurance organizations
- Population health analytics teams
- Medicare Advantage programs
- Preventive care outreach initiatives
- Healthcare BI and reporting teams
