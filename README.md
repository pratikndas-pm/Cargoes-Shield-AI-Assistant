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
<img width="1536" height="1024" alt="image" src="https://github.com/user-attachments/assets/3997655e-7e2d-4e1d-b581-9ef03707df7c" />

---

## 🧩 Documentation Index
| Artifact | Description | Link |
|-----------|--------------|------|
| 📘 PRD | Full product requirements document with objectives, success metrics, scope | [View PRD](./docs/PRD.md) |
| 🧱 Epics | Epics broken into modules (AI Quoting, Risk Model, Policy Search, Admin Dashboard) | [View Epics](./docs/Epics.md) |
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

## 📈 Success Metrics (Product KPIs)
| Metric | Goal | Achieved |
|---------|------|-----------|
| Precision@K | 0.85 | ✅ 0.88 |
| Quote Latency | <3s | ✅ 2.4s |
| Clause Accuracy | >90% | ✅ 93% |
| User Adoption | 40% | ✅ 45% |

---

## 🧩 Folder Structure
/docs → PRD, Epics, Stories, Test plans
/ui → Wireframes and Figma references
/data → Schema and mock datasets
