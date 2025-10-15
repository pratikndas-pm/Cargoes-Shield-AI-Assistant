# 🚢 Cargoes Shield – AI Risk & Quoting Assistant

> AI-powered quoting and risk intelligence platform built on top of Cargoes ecosystem.  
> Designed to automate insurance policy evaluation, premium recommendations, and claim risk scoring.

---

## 📊 Overview
**Goal:** Automate marine insurance quote generation using LLMs and data-driven risk prediction.  
**Outcome:** Reduced quote turnaround time by 65% and increased clause retrieval accuracy by 32%.

---

## 🧱 Architecture Snapshot
| Layer | Description | Technology |
|--------|--------------|-------------|
| Data | Policy documents, historical claims, tariff sheets | Azure SQL, Databricks |
| Model | LLM with retrieval (RAG), risk scoring | GPT-4o, LangChain |
| API | Policy, Quoting, CRM | REST, Azure Functions |
| UI | Shield Assistant Dashboard | Streamlit / React |


---

## 🧩 Documentation Index
| Artifact | Description | Link |
|-----------|--------------|------|
| 📘 PRD | Full product requirements document with objectives, success metrics, scope | [View PRD](./docs/PRD.md)
| 🧾 User Stories | Gherkin-format stories aligned to Jira tickets | [View User Stories](./docs/UserStories.md) |
| ✅ Testing Criteria | Model testing, functional test cases, QA validation flows | [View Testing Criteria](./docs/TestingCriteria.md) |
| 🎨 Frontend & Model Guidelines | Design specs + LLM prompt engineering standards | [View Frontend Guide](./docs/Frontend_Model_Guidelines.md) |

---

## 🧠 Core Features
- 🧩 AI-driven quote and premium engine  
- 📄 Policy clause retrieval via RAG  
- ⚙️ Multi-insurer comparison and optimization  
- 🔒 Compliance with WCO / UN/CEFACT standards  
- 📊 Dashboard with predictive claim scoring  

---

## 🧮 Example Use Case
**User Query:**  
> “Generate a quote for refrigerated cargo from Singapore to Jebel Ali, 5 containers, high-risk category.”

**Response:**  
- Risk Score: 7.8/10  
- Recommended Premium: USD 3,920  
- Policy Clauses: WCO-A12, Shield-7B, MarineHazard-02  
- ETA: 3 days  

---


### 💰 Revenue & Commercial KPIs

| KPI | Definition | Target | Data Source |
|------|-------------|---------|--------------|
| **Total Premiums Processed (AED)** | Total value of all insurance policies purchased through Cargoes Shield. | ≥ AED **10M / month** | Payment Gateway / CRM |
| **Average Policy Value (AED)** | Mean value per issued policy across all providers. | ≥ **5,000 AED** | CRM / Finance DB |
| **Quote-to-Policy Conversion Rate** | Percentage of quotes that convert into paid policies. | ≥ **35%** | Analytics / CRM |
| **Gross Written Premium (GWP)** | Total premiums booked before deductions. | ≥ **AED 120M / Year** | Finance Reports |
| **Commission Margin per Policy (%)** | Net revenue margin after insurer commissions. | ≥ **12%** | Financial Ledger |
| **Underwriter Approval SLA** | Average time from AI quote to final underwriter approval. | ≤ **15 minutes** | Underwriter Console Logs |
| **Payment Success Rate** | Percentage of successful transactions out of all payment attempts. | ≥ **98%** | Payment Gateway Logs |
| **Refund / Failure Rate (%)** | Ratio of failed or refunded transactions to total transactions. | ≤ **1%** | Finance & Payment Reports |
| **Renewal Retention Rate** | Percentage of users renewing policies within 15 days of expiry. | ≥ **75%** | CRM / Renewal Module |
| **Active Insurer Partnerships** | Number of insurer APIs actively integrated and quoting. | ≥ **5** by Q1 | Integration Dashboard |

> 💡 *Objective:* These KPIs measure the financial health, operational speed, and transaction reliability of the Cargoes Shield AI quoting and booking ecosystem.

### 🤖 Model & AI Performance KPIs

| KPI | Definition | Target | Data Source |
|------|-------------|---------|--------------|
| **Precision@k** | Measures how accurately the AI retrieves relevant policy or quote information within the top-k responses. | ≥ **0.85** | ModelOps Validation Suite |
| **Recall** | Percentage of all relevant answers or quotes correctly retrieved by the AI. | ≥ **0.80** | Model Evaluation Reports |
| **F1 Score** | Combined measure of precision and recall for balanced model performance. | ≥ **0.82** | Model Testing Dashboard |
| **Latency (p95)** | 95th percentile of AI response time per query (user-perceived). | ≤ **2.5 seconds** | API Gateway Metrics |
| **AI Response Helpfulness Rate** | Percentage of AI responses rated “Helpful” by users. | ≥ **85%** | Feedback Logs |
| **Model Drift Rate** | Month-over-month drop in model accuracy due to outdated data or context. | ≤ **3%** | Model Monitoring Reports |
| **Retraining Frequency** | Frequency of scheduled model retraining to maintain accuracy and reduce drift. | Every **30 days** | MLOps Pipeline |
| **Feedback Incorporation Rate** | Percentage of low-rated AI responses used in retraining datasets. | ≥ **70%** | Feedback Data Pipeline |
| **Average Confidence Score (AI Answers)** | Mean confidence level returned by the model per answer or quote. | ≥ **0.90** | Model Inference Logs |
| **Model Explainability Coverage** | Percentage of AI responses with cited sources or document references. | 100% | AI Audit Logs |

> ⚙️ *Objective:* Maintain high trust, transparency, and predictability in AI-driven recommendations by balancing accuracy, latency, and explainability.

---

## 🧩 Diagram
<img width="1536" height="1024" alt="image" src="https://github.com/user-attachments/assets/3997655e-7e2d-4e1d-b581-9ef03707df7c" />
