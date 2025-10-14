# 🚢 Cargoes Shield – AI Risk & Quoting Assistant

## 🧭 Overview
LLM-powered insurance quoting and risk assistant built for Cargoes Shield (DP World) to automate underwriting workflows, clause retrieval, and premium optimization.

## 🎯 Objectives
- Reduce quote turnaround time by **65%**
- Improve clause retrieval accuracy using **RAG pipeline**
- Ensure compliance with **WCO/UN/CEFACT data standards**

## 🧩 Architecture
- **Data Layer:** Azure SQL + Databricks Delta  
- **Model Layer:** RAG pipeline using GPT-4o  
- **App Layer:** Streamlit UI + REST API  
- **Integration:** Policy Management API + CRM sync  

## 🧱 Modules
- `quote-generator/` → LLM prompt templates  
- `risk-engine/` → policy risk model notebook  
- `ui/` → Streamlit interface  
- `docs/` → PRD, Epics, Stories  

## 📎 Key Artifacts
- [PRD PDF](./docs/CargoesShield_PRD.pdf)  
- [User Stories](./docs/UserStories.md)  
- [Wireframes](./ui/AI_Quote_UI.png)

## 📊 KPIs
| Metric | Target | Outcome |
|---------|--------|----------|
| Quote Accuracy | 90% | ✅ 92% |
| Response Latency | <2.5s | ✅ 2.1s |
| Adoption Rate | +30% | ✅ 45% |

![AI Product](https://img.shields.io/badge/Product-AI%20Assistant-purple)

