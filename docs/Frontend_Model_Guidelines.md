
## 4. Core Layout Standards

- Container width: `max-w-7xl`, centered with horizontal padding 24px.  
- Grid system: 12-column, responsive.  
- Breakpoints: `sm:640`, `md:768`, `lg:1024`, `xl:1280`.  
- Consistent header/footer height across all modules.  
- Error pages (404/500) must reuse layout with unified navigation and action links.

---

## 5. Input & Form Behavior

**Applies to:** Shipment data, policy uploads, underwriter edits, and feedback flows.  

| Element | Behavior | Validation |
|----------|-----------|------------|
| Text Inputs | Real-time validation on blur | Regex or schema (Zod) |
| File Uploads | PDF/DOCX/JPG ≤ 20MB | MIME + size validation client-side |
| Dropdowns | Searchable, keyboard accessible | Default “Select” placeholder |
| Buttons | Primary (teal), secondary (outline) | Disable during submission |
| Errors | Inline red text under field | Top summary for form errors |

> **PO Note:** User must receive **clear recovery paths** for all validation errors — never dead ends.

---

## 6. AI Interaction Guidelines (Stories SHLD-AI-001 to 003)

**Goal:** Ensure users can upload, read, and query policy documents seamlessly.

- File upload modal must accept drag-drop and click-to-browse.  
- Show progress bar (0–100%) and success state once parsing completes.  
- OCR extractions must display confidence per field (e.g., Coverage – 95%).  
- Missing data appears in a right-side “Issues” drawer, editable inline.  
- AI QnA responses must include:
  - Answer text
  - Confidence % (color-coded: Green ≥90%, Amber 70–89%, Red <70%)
  - Citation (section + page number)
  - Response time badge (in seconds)

> **Fallback Rule:** If confidence < 70%, AI must display: “I couldn’t find this information in your document.”

---

## 7. Quoting Experience (Stories SHLD-AI-004 to 006)

**Objective:** Deliver instant, transparent quotes from uploaded shipment data.

- **Form Input:** Origin, destination, cargo type, cargo value, and weight.  
- **Processing:** AI should parse file or manual input → validate → display quotes.  
- **Output Display:**
  - At least **3 quote cards**: Standard / Premium / Shield+  
  - Each card shows coverage %, deductible, premium, provider name/logo  
  - “Recommended” tag uses prior user preferences and AI ranking  

**Sorting options:**
1. Lowest Premium  
2. Best Coverage  
3. Recommended  

> **PO Acceptance:** Quote generation time ≤ 3 seconds (client perceived).

---

## 8. Risk Scoring & Explanation (Story SHLD-AI-005)

**Purpose:** Help underwriters and customers understand risk factors.

- Risk score displayed as badge (0–100 scale).  
- Color scale: Green < 40, Amber 40–70, Red > 70.  
- Expandable panel shows “Top 3 risk drivers” with short explanations.  
- Tooltip should clarify how each factor impacts premium.

---

## 9. Checkout & Policy Issuance (Story SHLD-AI-007)

**Objective:** Complete secure payment and generate policy instantly.

- Payment via PCI-DSS–compliant gateway (Stripe/Orchestrator).  
- On success:
  - Display success screen with Policy ID, coverage summary, and PDF link.  
  - Send confirmation email (template managed in CRM).  
- On failure:
  - Display retry option with clear error reason.  
  - Preserve form state (don’t clear values).  

> **PO Rule:** No sensitive card data stored in browser or logs.

---

## 10. Underwriter Console (Story SHLD-AI-008)

- Accessible only to underwriter roles (RBAC).  
- Editable fields: Premium (±15%), Coverage %, Deductible.  
- Version control: Every save increments version (v1.0 → v1.1).  
- Approve/Reject action logs timestamp + approver name.  
- Only approved quotes visible to customer dashboard.

---

## 11. Renewal & Notifications (Story SHLD-AI-009)

- Automatic reminder **15 days before policy expiry.**  
- Notification types:
  - Email: “Your Cargoes Shield policy expires soon.”  
  - Dashboard: Renewal banner with updated premium option.  
- CTA: “Renew Now” opens pre-filled form with revised rates.

---

## 12. Analytics Dashboards (Stories SHLD-AI-010 & 011)

**Objective:** Provide actionable business insights and model monitoring.

**Policy Dashboard**
- KPIs: Policies sold, average premium, conversion rate, average risk score.  
- Filters: Date range, provider, route.  
- Charts: Line (sales trend), bar (provider comparison), pie (coverage mix).  
- Export options: CSV & PDF.

**AI Model Performance**
- Table shows precision, recall, F1-score, latency.  
- Alerts appear if F1 < 0.8 or latency > 2s.  
- Retraining button triggers backend job (admin only).

---

## 13. Feedback & Model Improvement (Stories SHLD-AI-012 to 014)

- Each AI answer has “Helpful 👍 / Not Helpful 👎”.  
- On “Not Helpful”, show optional comment box.  
- Feedback stored with response ID and timestamp.  
- Validation dashboard visualizes:
  - Precision@k, Recall, F1, Latency  
  - Status: PASS / FAIL  
  - Deployment gate: “Proceed to Prod” only if all metrics > threshold

---

## 14. Visual & Interaction Consistency

| Element | Spec | Description |
|----------|------|-------------|
| Buttons | Rounded-2xl | Primary teal / Secondary grey |
| Inputs | Shadow-sm + border | Focus ring teal |
| Cards | Rounded-2xl | Shadow-md + hover elevation |
| Modals | Blur backdrop | ESC or close icon exits |
| Loaders | Skeleton for data | Spinner for actions |
| Toasts | 5s auto-dismiss | 3 color variants |

---

## 15. Accessibility & Compliance

- Keyboard navigation must work for all modals, lists, and inputs.  
- Screen reader-friendly labels for all icons and buttons.  
- Text contrast ≥ 4.5:1.  
- Reduced-motion users bypass animation.  
- Upload flow and quote comparison must pass WCAG 2.1 AA validation.

---

## 16. Performance & Quality Metrics

| Metric | Target | Validation Method |
|---------|---------|------------------|
| LCP | ≤ 2.5s | Lighthouse |
| FID | ≤ 100ms | Chrome DevTools |
| CLS | ≤ 0.1 | Lighthouse |
| Quote Load Time | ≤ 3s | Manual / E2E |
| Dashboard Latency | ≤ 5min data freshness | API logs |
| Accessibility Score | ≥ 90 | axe-core |

---

## 17. QA & Test Hooks

- Use `data-testid` attributes for automation:
  - `data-testid="quote-card"`
  - `data-testid="risk-badge"`
  - `data-testid="upload-progress"`
- Cypress for E2E (User stories 1–9)
- Playwright for AI response rendering and latency measurement.
- All Acceptance Criteria mapped to `/docs/TestingCriteria.md`.

---

## 18. Analytics & Telemetry

- Track with Segment / GA4:
  - `quote_generated`
  - `policy_purchased`
  - `ai_feedback_submitted`
  - `model_retrain_triggered`
- Include anonymous session IDs only.
- PO validates that analytics fields map to business KPIs in `/docs/PRD.md`.

---

## 19. PO Acceptance Checklist (Before Merge)

| Check | Owner | Status |
|--------|--------|--------|
| UI matches Figma spec | Design | ☐ |
| Acceptance Criteria validated | QA | ☐ |
| A11y audit passed | QA | ☐ |
| Performance metrics within limits | DevOps | ☐ |
| Analytics events firing correctly | Eng | ☐ |
| Documentation updated | PO | ☐ |

---

> ✅ **Outcome:**  
When all above guidelines are implemented, the Cargoes Shield AI Assistant frontend will deliver a consistent, explainable, and auditable experience aligned with enterprise-grade insurance workflows.

