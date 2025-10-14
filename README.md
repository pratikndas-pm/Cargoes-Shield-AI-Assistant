# Cargoes Shield AI Assistant 🤖
LLM-powered risk-reporting and claims insight tool for maritime cargo insurance.

## 🌍 Overview
Cargoes Shield AI Assistant automates policy validation, risk scoring, and claims analysis for global cargo insurers and underwriters within the Cargoes ecosystem.

## 🚢 Problem
Manual risk scoring and policy document validation delayed claims approval and led to inconsistent risk assessments.  
Average underwriting turnaround time: **3–5 days.**

## 💡 Solution
An AI-powered assistant using **Retrieval-Augmented Generation (RAG)** to extract insights from policy documents, shipment data, and historical claims.

## 🧠 Architecture
1. **Data Layer:** Cargoes Shield policy PDFs, TOS data, and claims history stored in **Databricks Delta Lake**.  
2. **Retrieval Layer:** FAISS-based retriever + LangChain metadata filters.  
3. **LLM Layer:** GPT-4 Turbo fine-tuned for insurance reasoning.  
4. **Presentation Layer:** Streamlit/Gradio dashboard for “Ask Shield AI” interface.

## 📊 KPIs
| Metric | Baseline | Post-AI |
|---------|-----------|----------|
| Claim Processing Time | 5 days | 2.8 days |
| Risk Score Accuracy | 60% | 84% |
| User Adoption | - | 78% |

## 📁 Files
- `prd.md` – Detailed product requirements  
- `pseudo_code.txt` – RAG workflow logic  

## 🔮 Future Enhancements
- Multilingual policy understanding (Arabic/Chinese)
- Integration with Cargoes Community System for unified insights
- Self-service analytics dashboard
