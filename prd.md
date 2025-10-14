# Cargoes Shield AI Assistant + Insurance Booking & Quoting System (B2B)

![Built with GPT-5](https://img.shields.io/badge/Built%20with-GPT--5-blueviolet)
![Platform](https://img.shields.io/badge/Platform-DP%20World%20|%20Cargoes%20Shield-teal)
![Status](https://img.shields.io/badge/Status-MVP%20v1.2-green)
![Author](https://img.shields.io/badge/Author-Pratik%20Das-lightgrey)

> Comprehensive Product Requirement Document (PRD) for Cargoes Shield AI Assistant and Insurance Booking & Quoting System (B2B) under DP World’s Digital Trade Solutions (DTS) ecosystem.

---

## 1. Objective
The **Cargoes Shield AI Assistant** transforms the traditional cargo insurance workflow into an intelligent, conversational, and data-driven experience. The system empowers freight forwarders, shippers, and logistics operators to generate, review, and purchase cargo insurance policies in seconds — without manual data input or broker coordination.

### Strategic Objectives
1. **Automation:** Eliminate manual data entry by integrating Marsh’s broker API and Cargoes Runner shipment data.
2. **User Experience:** Enable conversational insurance booking powered by AI to improve adoption and reduce friction.
3. **Predictive Intelligence:** Use machine learning to provide indicative premiums and route-based risk recommendations.
4. **Revenue Growth:** Increase insurance conversion and admin-fee revenue for DP World’s business units.
5. **Compliance:** Standardize insurance documentation and reporting across jurisdictions.

---

## 2. High-Level Summary
Cargoes Shield AI Assistant combines **AI-based conversational interfaces** with **enterprise-grade integrations** to enable an embedded insurance experience.

The assistant uses **GPT-5** and **Azure Cognitive Search** to understand user intent, retrieve relevant policies and data, and initiate quoting or certification workflows through **Marsh APIs**. It also interacts with **Cargoes Runner**, **Oracle Fusion**, and the **DP World payment gateway** to ensure operational parity between insurance and logistics records.

### Key Features
- **Natural-language interface** for quoting, booking, and certificate generation.
- **AI-driven auto-completion** of shipment attributes and quote parameters.
- **Integrated Marsh connectivity** for dynamic quote generation, referrals, and policy management.
- **AI Insights Dashboard** providing adoption, premium, and claim analytics.

---

## 3. Target Market
The MVP targets **Small and Medium Enterprises (SMEs)**, **freight forwarders**, and **exporters/importers** using DP World’s Cargoes.com platform.  
These users typically lack dedicated insurance teams and rely on freight platforms to provide fast, transparent, and compliant coverage options.

---

## 4. User Personas
| Persona | Description | Responsibilities | Pain Points | AI Value Add |
|----------|--------------|------------------|--------------|---------------|
| Freight Forwarder | Core user managing shipments and insurance | Requests quotes, views indicative pricing, accepts or rejects offers | Manual data entry, delayed quotes | Conversational AI quoting |
| DP World Operations | Oversees insurance adoption | Monitors metrics, resolves escalations | Limited visibility | Real-time dashboards |
| Marsh Broker | Provides quote and policy data | Approves or refers quotes | Poor input data | AI validates input |
| Administrator | Manages integrations | Maintains uptime | Multi-system complexity | Centralized admin and logs |

---

## 5. Key Performance Indicators (KPIs)
| Metric | Description | Target |
|---------|--------------|--------|
| Quote-to-Purchase Conversion | % of quotes accepted | ≥ 35% |
| Avg. Time to Generate Quote | Quote generation latency | ≤ 3 seconds |
| AI Field Accuracy | Correctness of AI auto-fill | ≥ 95% |
| Referral Resolution Time | Avg. Marsh API response | ≤ 2 hours |
| System Uptime | Availability | ≥ 99.5% |
| Admin Fee Revenue | DP World admin margin | ≥ 10% |
| Customer Retention | Repeat users | ≥ 75% |
| CSAT | User satisfaction | ≥ 90% |
| Quote Error Rate | API or AI failure | ≤ 1% |

---

## 6. System Architecture
### Core Layers
1. **Frontend:** Cargoes.com / Shield web UI (React)
2. **AI Layer:** GPT-5 + Azure Cognitive Search + Pinecone Vector DB
3. **Integration Layer:** Marsh, Cargoes Runner, Oracle Fusion APIs
4. **Data & Analytics:** Databricks, Data Lake, Power BI
5. **Security:** OAuth 2.0, RBAC, AES-256 encryption

> Diagram Placeholder: `/assets/architecture.png`

---

## 7. Functional Epics

### Epic 1 – AI-Assisted Interest Capture
**Objective:** Capture user intent to insure cargo at shipment creation.

**Workflow:**
1. AI prompts user for insurance intent.
2. Parses yes/no and triggers quote or logs preference.
3. Validates shipment data for completeness.
4. Syncs with Cargoes Runner for auto-fill.

**Frontend Guidelines:**
- Contextual pop-up with smooth transition (2s delay post-booking).
- Consistent Cargoes Shield theme and typography.
- Accessibility: Keyboard navigable, color-contrast ratio 4.5:1 minimum.

**Testing Criteria:**
- User response captured 100% of time.
- API sync verified with valid response.
- Incorrect shipment ID gracefully handled.
- Frontend latency ≤ 1.5s for AI pop-up.

**Model Testing Criteria:**
- Intent detection accuracy ≥ 98%.
- False-positive rate ≤ 2%.
- Latency ≤ 1s for GPT-5 classification.

---

### Epic 2 – AI-Driven Price Indication
**Objective:** Generate instant indicative premium.

**Workflow:**
1. Extract 4 core shipment attributes.
2. Fetch indicative price from Marsh API.
3. Display premium, coverage range, and notes.

**Frontend Guidelines:**
- Show insurance summary card under shipment details.
- Button: “Proceed to Quote” with hover tooltip.
- Loading animation ≤ 800ms.

**Testing Criteria:**
- Price displayed within 3s.
- Marsh API response validation.
- Accuracy cross-verified with test payloads.
- Error screen must show fallback text.

**Model Testing Criteria:**
- Prediction accuracy ≥ 95%.
- Hallucination rate ≤ 1%.
- Response latency ≤ 1.5s.
- Confidence score ≥ 0.8.

---

### Epic 3 – AI Quote Generation & Certificate
**Objective:** Automate quote and certificate creation.

**Workflow:**
1. Collect 22 required fields.
2. Submit to Marsh API.
3. Handle accept/reject/refer.
4. Generate certificate on acceptance.

**Frontend Guidelines:**
- Certificate preview panel before payment.
- Marsh logo and policy number displayed dynamically.
- Status toast notification for API callback.

**Testing Criteria:**
- Certificate URL returned in ≤ 5s.
- 100% validation of all fields.
- Payment link tested for three currencies.
- Rejected quotes retried automatically.

**Model Testing Criteria:**
- Response classification F1 ≥ 0.92.
- Fallback coverage success ≥ 98%.
- API call confidence ≥ 0.85.

---

### Epic 4 – Conversational Dashboard
**Objective:** Enable AI-powered analytics queries.

**Features:**
- Conversational queries for portfolio view.
- AI generates on-demand reports.

**Frontend Guidelines:**
- Unified chat + analytics tab.
- Dynamic charts with hover data.
- Export options (CSV/PDF).

**Testing Criteria:**
- Dashboard load time ≤ 2s.
- Chart refresh < 1s.
- Query accuracy ≥ 95%.
- Response caching enabled.

**Model Testing Criteria:**
- Precision@K ≥ 0.9.
- Response faithfulness ≥ 98%.
- Latency ≤ 1.2s.

---

### Epic 5 – Payments & Reconciliation
**Objective:** Streamline payment validation.

**Workflow:**
- Sync with DP World Payment Gateway.
- Reconcile Marsh and Cargoes Runner records.
- Generate audit reports.

**Frontend Guidelines:**
- Tabular summary with pagination.
- Success/failure badges.
- PDF export confirmation message.

**Testing Criteria:**
- 100% transaction ID reconciliation.
- Mismatch alerts triggered correctly.
- Report export verified.

**Model Testing Criteria:**
- Auto-match accuracy ≥ 97%.
- Confidence threshold ≥ 0.9.

---

### Epic 6 – Post-Dated Insurance
**Objective:** Allow policy creation for dispatched cargo.

**Workflow:**
1. Validate dispatch date.
2. If within threshold → submit quote.
3. Else → refer to Marsh manually.

**Frontend Guidelines:**
- Info banner warning (“Backdated Policy Requires Review”).
- CTA disabled if > X days after dispatch.

**Testing Criteria:**
- Policy validation logic correct.
- Rejected cases logged accurately.
- Manual override tested.

**Model Testing Criteria:**
- Date parsing accuracy ≥ 99%.
- Compliance flagging ≥ 100%.

---

### Epic 7 – Predictive Insights & Analytics
**Objective:** Provide data-driven insights.

**Features:**
- Risk scoring by route and commodity.
- Trend forecast visualization.
- AI recommends optimized coverage.

**Frontend Guidelines:**
- Map visualization using Cargoes UI kit.
- Risk color gradient: Green → Amber → Red.
- Tooltip displays probability values.

**Testing Criteria:**
- Data refresh ≤ 1h.
- ML model predictions validated on test dataset.
- Accuracy ≥ 90% on historical backtest.

**Model Testing Criteria:**
- Precision@K ≥ 0.92.
- F1 ≥ 0.88.
- Drift detection every 7 days.
- Explainability via SHAP values.

---

## 8. Non-Functional Requirements
| Category | Requirement | Target |
|-----------|--------------|--------|
| Performance | API <3s | SLA |
| Availability | 99.5% uptime | Global |
| Security | RBAC, audit, encryption | ISO 27001 |
| Scalability | Auto-scale 2× load | Azure |
| AI Governance | <2% hallucination | DP World Policy |
| Compliance | GDPR, IMO, WCO | Legal verified |

---

## 9. Deployment & Activation Plan
**Phases**
1. Dev → QA → UAT → Prod (Azure)
2. CI/CD via GitHub Actions
3. Canary release (5% traffic)
4. Gradual rollout to full access

**Testing**
- Functional, integration, regression.
- AI evaluation: precision@k, F1, latency.
- Frontend regression via Cypress.
- Load testing with JMeter (1k concurrent users).

---

## 10. Future Enhancements
1. Multilingual support (Arabic, Mandarin, Spanish).  
2. Voice-based quote interaction.  
3. Claims automation module.  
4. Risk-based premium optimization.  
5. Model retraining automation pipeline.

---

## 11. Appendix
**Dependencies:** Marsh APIs, Cargoes Runner, Oracle Fusion, Databricks, GPT-5, Azure Cognitive Search, Pinecone.  
**Author:** Pratik Das, Product Marketing Manager – DP World | DTS  
**Version:** v1.2 | October 2025  
