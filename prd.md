# Cargoes Shield AI Assistant – Product Requirement Document

## Objective
Automate policy validation and risk scoring to accelerate claim approvals.

## User Stories
- As an **underwriter**, I want to query risk exposure by route/type so I can adjust premiums.
- As a **claims officer**, I want automatic anomaly detection for duplicate claims.
- As a **manager**, I want a dashboard summarizing daily claim ratios and predicted risk.

## Acceptance Criteria
- RAG model retrieves accurate policy clause responses >85%.
- Dashboard visualizes 10+ KPIs within 3 seconds.
- System integrates securely via RBAC and token-based access.

## Tech Stack
Databricks, LangChain, OpenAI GPT-4, Streamlit, PostgreSQL
