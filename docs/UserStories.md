# 📘 Cargoes-Shield-AI-Assistant — User Stories

> **Document Path:** `/docs/UserStories.md`  
> **Version:** 1.0  
> **Last Updated:** October 2025  
> **Author:** Pratik N. Das  
> **Product:** Cargoes-Shield-AI-Assistant + Insurance Booking & Quoting System  

---

## 📑 Table of Contents

### EPIC 1 — AI Policy Retrieval & Document QnA
- [SHLD-AI-001 — Upload and Extract Policy Document Data](#shld-ai-001)
- [SHLD-AI-002 — AI QnA on Policy Documents](#shld-ai-002)
- [SHLD-AI-003 — Auto-Summarize Policy Document](#shld-ai-003)

### EPIC 2 — Instant Quote & Risk Scoring Engine
- [SHLD-AI-004 — Get Instant Insurance Quote](#shld-ai-004)
- [SHLD-AI-005 — Risk Scoring for Each Shipment](#shld-ai-005)
- [SHLD-AI-006 — Compare Multiple Insurers’ Quotes](#shld-ai-006)

### EPIC 3 — Insurance Booking & Underwriter Workflow
- [SHLD-AI-007 — Confirm and Purchase Policy](#shld-ai-007)
- [SHLD-AI-008 — Underwriter Approval Flow](#shld-ai-008)
- [SHLD-AI-009 — Policy Renewal Reminder](#shld-ai-009)

### EPIC 4 — Dashboard & Analytics
- [SHLD-AI-010 — Policy Analytics Dashboard](#shld-ai-010)
- [SHLD-AI-011 — AI Model Performance Monitoring](#shld-ai-011)

### EPIC 5 — Model Testing & Feedback Loop
- [SHLD-AI-012 — Feedback Capture for AI Responses](#shld-ai-012)
- [SHLD-AI-013 — Model Retraining Pipeline](#shld-ai-013)
- [SHLD-AI-014 — Model Testing & Validation Dashboard](#shld-ai-014)

---

## 🧩 EPIC 1 — AI Policy Retrieval & Document QnA

---

### <a id="shld-ai-001"></a>**Story ID: SHLD-AI-001 — Upload and Extract Policy Document Data**
**As a** claims analyst,  
**I want** to upload insurance policy PDFs and extract key clauses (coverage, exclusions, premiums),  
**So that** I can compare and validate them automatically.

**Acceptance Criteria**
1. System must support PDF, DOCX, and scanned image (OCR) formats.  
2. When uploaded, the AI must extract at least 90% of coverage fields accurately.  
3. Extracted data should be structured into JSON (key/value pairs).  
4. System must flag missing or ambiguous data for manual review.  
5. Uploaded files stored securely using AES-256 encryption.

---

### <a id="shld-ai-002"></a>**Story ID: SHLD-AI-002 — AI QnA on Policy Documents**
**As a** user,  
**I want** to ask natural-language questions about my uploaded insurance policy,  
**So that** I can understand terms without reading the full document.

**Acceptance Criteria**
1. AI must respond to questions using context retrieved from uploaded documents.  
2. Minimum Precision@k ≥ 0.85 on internal QA benchmark.  
3. Latency per query ≤ 2.5 s (p95).  
4. AI must cite which policy section or page the answer came from.  
5. If no confident answer, AI must respond: “I couldn’t find this information in your document.”

---

### <a id="shld-ai-003"></a>**Story ID: SHLD-AI-003 — Auto-Summarize Policy Document**
**As a** logistics manager,  
**I want** a concise summary of uploaded policies,  
**So that** I can compare coverage options faster.

**Acceptance Criteria**
1. Summary must include: coverage, exclusions, limits, renewal period.  
2. Word count ≤ 250 words.  
3. Must include confidence score for extracted fields.  
4. Exportable to PDF or Email.

---

## ⚙️ EPIC 2 — Instant Quote & Risk Scoring Engine

---

### <a id="shld-ai-004"></a>**Story ID: SHLD-AI-004 — Get Instant Insurance Quote**
**As a** freight forwarder,  
**I want** to upload shipment data and instantly get insurance quotes,  
**So that** I can choose the best plan quickly.

**Acceptance Criteria**
1. System must parse Excel, CSV, or API data from TOS/ERP.  
2. AI must extract shipment fields (origin, destination, cargo type, value, weight) ≥ 95% accuracy.  
3. At least 3 quote options (Standard, Premium, Shield-Plus) displayed.  
4. Each quote shows: coverage %, deductible, premium, provider.  
5. Quote generation time ≤ 3 s.

---

### <a id="shld-ai-005"></a>**Story ID: SHLD-AI-005 — Risk Scoring for Each Shipment**
**As an** underwriter,  
**I want** to see AI-generated risk scores,  
**So that** I can adjust premiums appropriately.

**Acceptance Criteria**
1. Risk score range: 0–100.  
2. Inputs: cargo type, port risk index, weather, carrier reliability, past claims.  
3. AI must justify top 3 contributing risk factors.  
4. Model F1 ≥ 0.82 on validation.  
5. Scores logged in audit trail.

---

### <a id="shld-ai-006"></a>**Story ID: SHLD-AI-006 — Compare Multiple Insurers’ Quotes**
**As a** customer,  
**I want** to compare quotes from multiple providers,  
**So that** I can pick the best option.

**Acceptance Criteria**
1. Display quotes from ≥ 3 providers via API integration.  
2. Quote cards show coverage %, exclusions, premium.  
3. Sorting: “Lowest Premium,” “Best Coverage,” “Recommended.”  
4. AI highlights best plan using user preference history.

---

## 💼 EPIC 3 — Insurance Booking & Underwriter Workflow

---

### <a id="shld-ai-007"></a>**Story ID: SHLD-AI-007 — Confirm and Purchase Policy**
**As a** shipper,  
**I want** to confirm and purchase my chosen plan,  
**So that** my cargo is covered before departure.

**Acceptance Criteria**
1. Payment gateway (Stripe or internal orchestrator) processes securely (PCI-DSS).  
2. Upon success, policy PDF auto-generated and emailed.  
3. Transaction ID and policy # logged in CRM.  
4. Failed payment triggers retry prompt.

---

### <a id="shld-ai-008"></a>**Story ID: SHLD-AI-008 — Underwriter Approval Flow**
**As an** underwriter,  
**I want** to review AI-suggested quotes and approve or edit them,  
**So that** I maintain control over issuance.

**Acceptance Criteria**
1. Underwriter may adjust premium ± 15%.  
2. Edits trigger version control (v1.0, v1.1).  
3. Approval timestamped and logged.  
4. Only approved quotes visible to customers.

---

### <a id="shld-ai-009"></a>**Story ID: SHLD-AI-009 — Policy Renewal Reminder**
**As a** customer,  
**I want** renewal reminders,  
**So that** I don’t lose coverage.

**Acceptance Criteria**
1. Reminder triggers 15 days before expiry.  
2. Email + dashboard notifications sent.  
3. AI suggests renewal options with updated premiums.

---

## 📊 EPIC 4 — Dashboard & Analytics

---

### <a id="shld-ai-010"></a>**Story ID: SHLD-AI-010 — Policy Analytics Dashboard**
**As a** product manager,  
**I want** a visual dashboard of policy metrics,  
**So that** I can monitor adoption and revenue.

**Acceptance Criteria**
1. KPIs: #Policies Sold, Avg Premium, Conversion Rate, Avg Risk Score.  
2. Filters by date range, provider, route.  
3. Exportable as CSV/PDF.  
4. Data latency ≤ 5 min.

---

### <a id="shld-ai-011"></a>**Story ID: SHLD-AI-011 — AI Model Performance Monitoring**
**As a** data scientist,  
**I want** to track model accuracy and drift,  
**So that** I can retrain models as needed.

**Acceptance Criteria**
1. Precision, Recall, F1 scores logged weekly.  
2. Drift alert if accuracy < 0.8.  
3. Dashboard alerts for retraining.  
4. Retraining status visible to admins.

---

## 🔁 EPIC 5 — Model Testing & Feedback Loop

---

### <a id="shld-ai-012"></a>**Story ID: SHLD-AI-012 — Feedback Capture for AI Responses**
**As a** customer,  
**I want** to rate AI responses,  
**So that** the model improves.

**Acceptance Criteria**
1. Feedback stored with response ID.  
2. Low-rated (< 60%) responses flagged for retraining.  
3. Monthly model-improvement metrics generated.

---

### <a id="shld-ai-013"></a>**Story ID: SHLD-AI-013 — Model Retraining Pipeline**
**As a** data engineer,  
**I want** automated retraining,  
**So that** accuracy remains high.

**Acceptance Criteria**
1. Automated retraining every 30 days.  
2. New versions tagged & logged.  
3. A/B testing between versions.  
4. Deploy only if F1 > previous.

---

### <a id="shld-ai-014"></a>**Story ID: SHLD-AI-014 — Model Testing & Validation Dashboard**
**As a** QA engineer,  
**I want** to validate model outputs on benchmarks,  
**So that** performance stays consistent.

**Acceptance Criteria**
1. Dashboard shows Precision@k, Recall, F1, Latency.  
2. Benchmarks run pre-deployment.  
3. Pass/fail gates define deployment readiness.

---

> ✅ **Total:** 14 User Stories | **Status:** Draft v1.0 | **Next Step:** Link to `/docs/TestingCriteria.md`
