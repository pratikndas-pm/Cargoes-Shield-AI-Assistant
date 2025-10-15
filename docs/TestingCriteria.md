# ✅ Cargoes-Shield-AI-Assistant — Testing Criteria

**Scope:** Functional, Integration, API, Performance, Security tests for all user stories in `/docs/UserStories.md`.  
**Traceability:** Each Test Case (TC) maps to a Story and Acceptance Criterion (AC).

---

## 📚 How to Use This File

- **IDs:** `TC-<Story>-<Number>` (e.g., `TC-001-01` = Story SHLD-AI-001, Case 01)  
- **Types:** F=Functional, I=Integration, API=Service, P=Performance, S=Security, U=Usability, N=Negative/Edge  
- **Priority:** P0 (Blocker), P1 (High), P2 (Medium), P3 (Low)

---

## 🔗 Traceability Matrix (Stories → Test Case Ranges)

| Story ID | Title (short) | TC ID Range |
|---|---|---|
| SHLD-AI-001 | Upload & Extract Policy | TC-001-01 … 06 |
| SHLD-AI-002 | Policy QnA | TC-002-01 … 08 |
| SHLD-AI-003 | Auto-Summarize | TC-003-01 … 06 |
| SHLD-AI-004 | Instant Quote | TC-004-01 … 07 |
| SHLD-AI-005 | Risk Scoring | TC-005-01 … 07 |
| SHLD-AI-006 | Compare Quotes | TC-006-01 … 06 |
| SHLD-AI-007 | Purchase Policy | TC-007-01 … 08 |
| SHLD-AI-008 | Underwriter Approval | TC-008-01 … 07 |
| SHLD-AI-009 | Renewal Reminder | TC-009-01 … 05 |
| SHLD-AI-010 | Analytics Dashboard | TC-010-01 … 07 |
| SHLD-AI-011 | Model Monitoring | TC-011-01 … 06 |
| SHLD-AI-012 | Feedback Capture | TC-012-01 … 05 |
| SHLD-AI-013 | Retraining Pipeline | TC-013-01 … 07 |
| SHLD-AI-014 | Validation Dashboard | TC-014-01 … 06 |

---

## 🧩 EPIC 1 — AI Policy Retrieval & Document QnA

### SHLD-AI-001 — Upload and Extract Policy Document Data

**AC Recap:** Supports PDF/DOCX/OCR, ≥90% field extraction, JSON output, flags missing/ambiguous, AES-256 at rest.

| ID | Type | Priority | Preconditions | Steps | Expected |
|---|---|---|---|---|---|
| TC-001-01 | F | P0 | Authenticated user | Upload `policy_sample.pdf` | File accepted; status=“Processed” |
| TC-001-02 | F | P0 | TC-001-01 done | Open extraction JSON | JSON includes coverage, exclusions, premiums; schema valid |
| TC-001-03 | F | P1 | — | Upload scanned image `policy_scan.jpg` (OCR) | OCR completes; fields populated; extraction accuracy ≥90% against gold file |
| TC-001-04 | N | P1 | — | Upload unsupported `.txt` | Graceful error: “Format not supported” |
| TC-001-05 | F | P1 | — | Upload file with missing “Deductible” | UI flag “Missing field: Deductible”; manual add enabled |
| TC-001-06 | S | P0 | Access to DB/Blob logs | Inspect storage metadata | Encryption at rest = AES-256; no PII in logs |

---

### SHLD-AI-002 — AI QnA on Policy Documents

**AC Recap:** Grounded answers, Precision@k ≥0.85, p95 latency ≤2.5s, citation to section/page, fallback message when uncertain.

| ID | Type | Priority | Preconditions | Steps | Expected |
|---|---|---|---|---|---|
| TC-002-01 | F | P0 | Policy uploaded & indexed | Ask: “What is the deductible?” | Direct answer + citation (Section & page) |
| TC-002-02 | P | P1 | Use 100 queries | Run load test; collect latencies | p95 ≤ 2.5s |
| TC-002-03 | F | P1 | Benchmark set | Run evaluation harness | Precision@k ≥ 0.85 |
| TC-002-04 | F | P1 | — | Ask unrelated: “Does it cover war in Mars?” | Fallback: “I couldn’t find this information…” |
| TC-002-05 | N | P2 | — | Ask ambiguous “limits?” | AI requests clarification or lists top candidates with citations |
| TC-002-06 | U | P3 | — | Review answer card | Citation link scrolls to doc location |
| TC-002-07 | API | P1 | API token | `POST /qna` with docId & query | 200; payload includes answer, citation, latency_ms |
| TC-002-08 | S | P0 | — | Try prompt injection in query | Guardrails strip instructions; output grounded only |

---

### SHLD-AI-003 — Auto-Summarize Policy Document

**AC Recap:** Include coverage/exclusions/limits/renewal, ≤250 words, confidence scores, export to PDF/Email.

| ID | Type | Priority | Preconditions | Steps | Expected |
|---|---|---|---|---|---|
| TC-003-01 | F | P1 | Policy processed | Click “Generate Summary” | Summary contains 4 required sections |
| TC-003-02 | F | P2 | — | Count words | ≤ 250 words |
| TC-003-03 | F | P1 | — | Inspect summary JSON | Confidence scores present per field |
| TC-003-04 | I | P1 | Email configured | Click “Email Summary” | Email delivered with summary PDF |
| TC-003-05 | API | P2 | — | `POST /summaries` | 200; includes sections & confidence |
| TC-003-06 | N | P2 | — | Missing limits in source | Summary lists “Limits: Not found” and flags low confidence |

---

## ⚙️ EPIC 2 — Instant Quote & Risk Scoring Engine

### SHLD-AI-004 — Get Instant Insurance Quote

**AC Recap:** Parse Excel/CSV/API, ≥95% field extraction, 3 plan options, show coverage/deductible/premium/provider, ≤3s.

| ID | Type | Priority | Preconditions | Steps | Expected |
|---|---|---|---|---|---|
| TC-004-01 | F | P0 | — | Upload `shipment.xlsx` | Fields parsed; accuracy report ≥95% |
| TC-004-02 | F | P0 | Parsed shipment | Click “Get Quote” | 3 options displayed (Standard, Premium, Shield-Plus) |
| TC-004-03 | F | P1 | — | Inspect quote cards | Each shows coverage %, deductible, premium, provider |
| TC-004-04 | P | P0 | — | Measure response time (10 runs) | Average ≤ 3s |
| TC-004-5 | API | P1 | — | `POST /quotes` with payload | 200; options≥3 |
| TC-004-06 | N | P1 | Missing cargo value | Prompt for missing field before quoting |
| TC-004-07 | I | P1 | TOS/ERP connector | Fetch via connector | Data parsed end-to-end |

---

### SHLD-AI-005 — Risk Scoring for Each Shipment

**AC Recap:** Score 0–100, inputs (cargo/port/weather/carrier/claims), explain top 3 factors, F1≥0.82, audit logged.

| ID | Type | Priority | Preconditions | Steps | Expected |
|---|---|---|---|---|---|
| TC-005-01 | F | P0 | Quote available | View “Risk Score” | Value in 0–100 |
| TC-005-02 | F | P1 | — | Expand “Explanation” | Top 3 contributing factors listed |
| TC-005-03 | API | P1 | — | `POST /risk/score` | 200; includes score & `top_factors[]` |
| TC-005-04 | F | P1 | Benchmark set | Run model eval | F1 ≥ 0.82 |
| TC-005-05 | I | P1 | Claims DB access | Score reflects historical claims input | Inputs referenced |
| TC-005-06 | F | P1 | — | Open audit log | Risk score + payload snapshot recorded |
| TC-005-07 | N | P2 | Missing weather | Uses fallback baseline; flags reduced confidence |

---

### SHLD-AI-006 — Compare Multiple Insurers’ Quotes

**AC Recap:** ≥3 providers via API, cards show key fields, sorting modes, AI recommendation.

| ID | Type | Priority | Preconditions | Steps | Expected |
|---|---|---|---|---|---|
| TC-006-01 | I | P0 | Provider APIs mocked | Trigger quote comparison | ≥3 providers listed |
| TC-006-02 | F | P1 | — | Inspect each card | coverage%, exclusions, premium visible |
| TC-006-03 | F | P1 | — | Sort by “Lowest Premium” | List reorders correctly |
| TC-006-04 | F | P2 | — | Sort by “Best Coverage” | Highest coverage first |
| TC-006-05 | F | P1 | Pref history exists | “Recommended” badge shown with rationale |
| TC-006-06 | N | P2 | One provider down | Degraded gracefully; shows remaining providers + warning |

---

## 💼 EPIC 3 — Insurance Booking & Underwriter Workflow

### SHLD-AI-007 — Confirm and Purchase Policy

**AC Recap:** PCI-DSS payment, policy PDF emailed, CRM logs Txn ID & policy #, retry on failure.

| ID | Type | Priority | Preconditions | Steps | Expected |
|---|---|---|---|---|---|
| TC-007-01 | I | P0 | Payment gateway sandbox | Click “Pay” (valid card) | Payment success |
| TC-007-02 | F | P0 | TC-007-01 | Check email & downloads | Policy PDF generated & emailed |
| TC-007-03 | I | P1 | CRM connected | Open CRM record | Transaction ID + policy # logged |
| TC-007-04 | N | P0 | Invalid card | Pay with declined card | Clear error + retry option |
| TC-007-05 | S | P0 | PCI attestation | Inspect logs/DB | No PAN/PCI data stored; tokenization used |
| TC-007-06 | API | P1 | — | `POST /payments/charge` | 200 on success; 402 on decline |
| TC-007-07 | F | P2 | — | Retry after failure | Second attempt succeeds |
| TC-007-08 | U | P3 | — | Review receipt screen | Receipt shows plan, premium, date, ref |

---

### SHLD-AI-008 — Underwriter Approval Flow

**AC Recap:** Adjust ±15%, versioning, timestamped approvals, only approved visible.

| ID | Type | Priority | Preconditions | Steps | Expected |
|---|---|---|---|---|---|
| TC-008-01 | F | P0 | Underwriter role | Edit premium +10% | Value saved; within bounds |
| TC-008-02 | N | P1 | — | Edit +25% | Validation error (exceeds limit) |
| TC-008-03 | F | P1 | — | Save edits | Version increments v1.0→v1.1 |
| TC-008-04 | F | P1 | — | Click “Approve” | Approval timestamp + actor recorded |
| TC-008-05 | F | P1 | Customer view | Check quote visibility | Only approved quotes shown |
| TC-008-06 | API | P2 | — | `POST /underwriting/approve` | 200; returns version, approver, ts |
| TC-008-07 | S | P0 | Role matrix | Try with non-UW role | 403 Forbidden |

---

### SHLD-AI-009 — Policy Renewal Reminder

**AC Recap:** Trigger 15 days pre-expiry, Email + in-app notif, suggest renewed premiums.

| ID | Type | Priority | Preconditions | Steps | Expected |
|---|---|---|---|---|---|
| TC-009-01 | I | P1 | Policy expiry mocked | Run scheduler | Reminders sent at T-15 |
| TC-009-02 | F | P1 | — | Check inbox & bell | Email + in-app notification present |
| TC-009-03 | F | P2 | — | Open reminder panel | Shows updated premium suggestions |
| TC-009-04 | N | P2 | Expiry changed | Verify rescheduling | Reminder rescheduled per new date |
| TC-009-05 | API | P2 | — | `POST /renewals/preview` | 200; returns premium options |

---

## 📊 EPIC 4 — Dashboard & Analytics

### SHLD-AI-010 — Policy Analytics Dashboard

**AC Recap:** KPIs, filters, export CSV/PDF, ≤5-min data latency.

| ID | Type | Priority | Preconditions | Steps | Expected |
|---|---|---|---|---|---|
| TC-010-01 | F | P1 | Data seeded | Open Dashboard | KPIs visible: Count, Avg Premium, Conversion, Avg Risk |
| TC-010-02 | F | P2 | — | Apply date/provider/route filters | Charts & KPIs update accordingly |
| TC-010-03 | I | P2 | Export service | Export CSV | Download valid CSV |
| TC-010-04 | I | P2 | Export service | Export PDF | Download valid PDF |
| TC-010-05 | P | P1 | Streaming on | Generate new policy | Metrics reflect within 5 minutes |
| TC-010-06 | U | P3 | — | Review legends/axes | Labels readable & accessible |
| TC-010-07 | S | P1 | RBAC | Try viewer on admin metric | Access denied |

---

### SHLD-AI-011 — AI Model Performance Monitoring

**AC Recap:** Log Precision/Recall/F1 weekly, drift alert if acc<0.8, alerts & retraining status visible.

| ID | Type | Priority | Preconditions | Steps | Expected |
|---|---|---|---|---|---|
| TC-011-01 | I | P1 | Metrics job | Run weekly job | Precision/Recall/F1 logged |
| TC-011-02 | F | P1 | Acc drop simulated | Dashboard view | Drift alert displayed |
| TC-011-03 | I | P2 | Notifier | Alert sent to channel/email |
| TC-011-04 | F | P2 | Retraining started | View admin | Status: queued → running → done |
| TC-011-05 | API | P2 | — | `GET /models/metrics?period=week` | 200; metric list |
| TC-011-06 | N | P2 | Metric gap | Job reruns | Missing interval backfilled or flagged |

---

## 🔁 EPIC 5 — Model Testing & Feedback Loop

### SHLD-AI-012 — Feedback Capture for AI Responses

**AC Recap:** Store rating with response ID, <60% flagged, monthly improvements.

| ID | Type | Priority | Preconditions | Steps | Expected |
|---|---|---|---|---|---|
| TC-012-01 | F | P1 | Answer shown | Click 👍/👎 | Feedback stored with `responseId` |
| TC-012-02 | F | P1 | Rate multiple | Submit low ratings | Items flagged to “retraining_queue” |
| TC-012-03 | I | P2 | Monthly job | Run job | Improvement report generated |
| TC-012-04 | API | P2 | — | `POST /feedback` | 201; persists userId, responseId, score |
| TC-012-05 | N | P2 | Unauth user | Submit feedback | Prompt login |

---

### SHLD-AI-013 — Model Retraining Pipeline

**AC Recap:** Auto every 30 days, versioning, A/B test, deploy only if F1 improves.

| ID | Type | Priority | Preconditions | Steps | Expected |
|---|---|---|---|---|---|
| TC-013-01 | I | P1 | Scheduler | Wait 30-day window | Retraining job triggered |
| TC-013-02 | F | P1 | Job run | Inspect model registry | New version tagged `vX.Y.Z` |
| TC-013-03 | I | P1 | Traffic splitter | Enable A/B 50/50 | Both versions get traffic |
| TC-013-04 | F | P1 | Eval complete | Compare metrics | New F1 > old; else block deploy |
| TC-013-05 | N | P1 | Lower F1 | Attempt deploy | Deployment prevented; reason logged |
| TC-013-06 | API | P2 | — | `POST /models/retrain` | 202; job id returned |
| TC-013-07 | S | P1 | Access control | Call endpoint as viewer | 403 Forbidden |

---

### SHLD-AI-014 — Model Testing & Validation Dashboard

**AC Recap:** Show Prec@k/Recall/F1/Latency, run benchmarks pre-deploy, pass/fail gates.

| ID | Type | Priority | Preconditions | Steps | Expected |
|---|---|---|---|---|---|
| TC-014-01 | F | P1 | Benchmark run | Open Validation Dashboard | Metrics panels visible: Prec@k, Recall, F1, Latency |
| TC-014-02 | F | P1 | Gate rules set | Click “Run Pre-Deploy” | Run completes; status PASS/FAIL |
| TC-014-03 | N | P1 | Force low metrics | Re-run | Status FAIL; deploy blocked |
| TC-014-04 | API | P2 | — | `POST /validation/run` | 202; returns runId |
| TC-014-05 | I | P2 | CI pipeline | Trigger pipeline | Pre-deploy validation stage executed |
| TC-014-06 | U | P3 | — | Interpret charts | Tooltips show thresholds & definitions |

---

## 🔒 Cross-Cutting Security & Privacy (applies across stories)

- **S-CC-01 (P0):** Verify TLS 1.2+ enforced, HSTS set, no mixed content.  
- **S-CC-02 (P0):** RBAC/ABAC checks: least privilege for Underwriter, Analyst, Customer.  
- **S-CC-03 (P0):** PII redaction in logs; secrets in vault; KMS for keys.  
- **S-CC-04 (P1):** OWASP Top-10: SQLi/XSS/CSRF tested on all form and API inputs.  
- **S-CC-05 (P1):** Rate limits on `/qna`, `/quotes`, `/payments`, `/models/*`.  
- **S-CC-06 (P1):** Data retention & deletion workflows verified.

---

## 🧪 Test Data & Fixtures

- **Docs:** `policy_sample.pdf`, `policy_scan.jpg`, `policy_edge.pdf` (missing fields)  
- **Shipments:** `shipment.xlsx`, `shipment_missing_value.xlsx`, mock TOS feed  
- **Benchmarks:** `qna_benchmark.jsonl`, `risk_eval.parquet`  
- **API Mocks:** Provider quote stubs, payment sandbox, CRM stub, email stub

---

## 🛠️ Environment & Tooling

- **Envs:** `dev`, `staging` (prod-like), `prod` (monitor-only)  
- **Pipelines:** CI triggers: unit → API → integration → pre-deploy validation (TC-014)  
- **Observability:** Traces + logs with correlation IDs; metrics for latency p95/p99

---

## ✅ Exit Criteria (Release Readiness)

- All **P0/P1** test cases pass in **staging**  
- Pre-deploy validation **PASS** (TC-014-02)  
- Security S-CC-01..06 **PASS**  
- Rollback plan validated

---

> **Next:** Link this file from README and wire CI to run API/validation suites before merge.

