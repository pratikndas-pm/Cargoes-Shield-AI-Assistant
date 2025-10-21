
import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime
import io

st.set_page_config(page_title="Cargoes Shield AI Assistant", page_icon="🛡️", layout="wide")

# --------------------------
# Utilities
# --------------------------
def load_sample_shipments():
    df = pd.read_csv("data/shipments_sample.csv")
    return df

def compute_risk(row):
    # Simple deterministic risk model (0-100)
    route_risk = {
        "ASIA-EU": 55, "EU-NA": 40, "ASIA-AFRICA": 65, "NA-SA": 45, "EU-AFRICA": 50
    }
    cargo_risk = {"Electronics": 65, "Textiles": 35, "Machinery": 50, "Pharmaceuticals": 40, "Automotive Parts": 55}
    base = 30
    r1 = route_risk.get(row.get("route","EU-NA"), 45)
    r2 = cargo_risk.get(row.get("cargo_type","Machinery"), 50)
    value_factor = min(30, (row.get("cargo_value_aed", 10000) / 100000) * 30)  # cap at 30
    score = np.clip(base*0.2 + r1*0.4 + r2*0.3 + value_factor*0.1, 0, 100)
    return round(score, 1)

def premium_from_risk(risk, cargo_value):
    # Premium as % of cargo value, scaled by risk
    base_rate = 0.004  # 0.4%
    rate = base_rate * (0.6 + risk/100*0.8)  # 0.24% to ~0.72%
    premium = cargo_value * rate
    return max(100.0, round(premium, 2))

def make_quote_options(risk, cargo_value):
    std = premium_from_risk(risk, cargo_value)
    prem = round(std * 1.25, 2)
    plus = round(std * 1.5, 2)
    return [
        {"plan": "Standard", "coverage_pct": 85, "deductible_aed": 2500, "premium_aed": std},
        {"plan": "Premium", "coverage_pct": 92, "deductible_aed": 1500, "premium_aed": prem},
        {"plan": "Shield-Plus", "coverage_pct": 96, "deductible_aed": 1000, "premium_aed": plus},
    ]

def simple_qna(policy_text, query):
    q = query.lower()
    # naive retrieval: return first matching line(s) + section title hint
    lines = policy_text.splitlines()
    for ln in lines:
        if q in ln.lower():
            return ln.strip(), "Matched policy clause", 0.92
    # fallback: keywords
    keywords = {
        "deductible": "Deductible: The insured bears the initial portion of any loss up to the deductible amount.",
        "coverage": "Coverage: The policy covers physical loss or damage to cargo during transit.",
        "exclusion": "Exclusions: War, nuclear incidents, inherent vice, and willful misconduct are excluded."
    }
    for k,v in keywords.items():
        if k in q:
            return v, "Knowledge base", 0.75
    return "I couldn’t find this information in your document.", "No match", 0.35

# --------------------------
# Sidebar Navigation
# --------------------------
st.sidebar.title("🛡️ Cargoes Shield")
page = st.sidebar.radio("Navigate", ["Dashboard", "Upload & Extract", "Get Quotes", "Policy QnA", "Underwriter Console", "About"])

# --------------------------
# Page: Dashboard
# --------------------------
if page == "Dashboard":
    st.title("📊 Cargoes Shield AI Assistant — Demo Dashboard")

    df = load_sample_shipments()
    df["risk_score"] = df.apply(compute_risk, axis=1)
    df["std_premium_aed"] = df.apply(lambda r: premium_from_risk(r["risk_score"], r["cargo_value_aed"]), axis=1)

    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Shipments", len(df))
    c2.metric("Avg Risk Score", f"{df['risk_score'].mean():.1f}")
    c3.metric("Avg Premium (AED)", f"{df['std_premium_aed'].mean():.0f}")
    conv = 0.34
    c4.metric("Quote→Policy Conversion", f"{int(conv*100)}%")

    st.subheader("Recent Shipments")
    st.dataframe(df.head(20), use_container_width=True)

# --------------------------
# Page: Upload & Extract
# --------------------------
elif page == "Upload & Extract":
    st.title("📥 Upload Shipment Data")
    st.write("Upload Excel/CSV with columns: origin, destination, route, cargo_type, cargo_value_aed, weight_kg")

    uploaded = st.file_uploader("Choose a CSV/Excel file", type=["csv","xlsx"])
    if uploaded:
        if uploaded.name.endswith(".csv"):
            udf = pd.read_csv(uploaded)
        else:
            udf = pd.read_excel(uploaded)
        st.success(f"Loaded {len(udf)} rows.")
        st.dataframe(udf.head(50), use_container_width=True)

        if set(["origin","destination","route","cargo_type","cargo_value_aed"]).issubset(udf.columns):
            udf["risk_score"] = udf.apply(compute_risk, axis=1)
            st.info("Calculated risk scores.")
            st.dataframe(udf.head(50), use_container_width=True)

            csv = udf.to_csv(index=False).encode("utf-8")
            st.download_button("⬇️ Download with Risk Scores (CSV)", csv, file_name="shipments_with_risk.csv", mime="text/csv")
        else:
            st.warning("Missing required columns. Please check your template.")

    st.divider()
    st.caption("Tip: Try the sample file on the Dashboard page in /data.")

# --------------------------
# Page: Get Quotes
# --------------------------
elif page == "Get Quotes":
    st.title("⚙️ Instant Quotes")
    st.write("Enter shipment details or pick one from the sample dataset.")

    df = load_sample_shipments()
    sample = st.selectbox("Pick a sample shipment", options=range(len(df)), format_func=lambda i: f"{df.iloc[i]['origin']} → {df.iloc[i]['destination']} • {df.iloc[i]['cargo_type']}")
    srow = df.iloc[sample].to_dict()

    c1, c2, c3 = st.columns(3)
    origin = c1.text_input("Origin", srow["origin"])
    destination = c2.text_input("Destination", srow["destination"])
    route = c3.selectbox("Route", ["ASIA-EU","EU-NA","ASIA-AFRICA","NA-SA","EU-AFRICA"], index=["ASIA-EU","EU-NA","ASIA-AFRICA","NA-SA","EU-AFRICA"].index(srow["route"]) if srow["route"] in ["ASIA-EU","EU-NA","ASIA-AFRICA","NA-SA","EU-AFRICA"] else 1)
    c4, c5 = st.columns(2)
    cargo_type = c4.selectbox("Cargo Type", ["Electronics","Textiles","Machinery","Pharmaceuticals","Automotive Parts"], index=["Electronics","Textiles","Machinery","Pharmaceuticals","Automotive Parts"].index(srow["cargo_type"]) if srow["cargo_type"] in ["Electronics","Textiles","Machinery","Pharmaceuticals","Automotive Parts"] else 2)
    cargo_value_aed = c5.number_input("Cargo Value (AED)", min_value=1000, value=int(srow["cargo_value_aed"]), step=500)

    if st.button("Get Quote"):
        row = {"route": route, "cargo_type": cargo_type, "cargo_value_aed": cargo_value_aed}
        risk = compute_risk(row)
        st.metric("Calculated Risk Score", risk)
        plans = make_quote_options(risk, cargo_value_aed)
        st.subheader("Available Plans")
        cols = st.columns(3)
        for i, p in enumerate(plans):
            with cols[i]:
                st.markdown(f"#### {p['plan']}")
                st.write(f"**Coverage:** {p['coverage_pct']}%")
                st.write(f"**Deductible:** AED {p['deductible_aed']:,}")
                st.write(f"**Premium:** **AED {p['premium_aed']:,}**")
                if i==2:
                    st.success("Recommended")

# --------------------------
# Page: Policy QnA
# --------------------------
elif page == "Policy QnA":
    st.title("❓ Policy Document QnA (Demo)")
    st.write("Ask a question about the sample policy text.")

    with open("data/policy_sample.txt","r",encoding="utf-8") as f:
        policy_text = f.read()

    query = st.text_input("Your question", "What is the deductible?")
    if st.button("Ask"):
        answer, source, conf = simple_qna(policy_text, query)
        st.markdown("**Answer:** " + answer)
        st.caption(f"Source: {source} • Confidence: {int(conf*100)}%")

    with st.expander("View Sample Policy Text"):
        st.code(policy_text[:2000] + ("\n...\n" if len(policy_text)>2000 else ""))

# --------------------------
# Page: Underwriter Console
# --------------------------
elif page == "Underwriter Console":
    st.title("🧑‍⚖️ Underwriter Console (Demo)")
    st.write("Adjust premium within ±15% and approve a quote.")

    df = load_sample_shipments()
    df["risk_score"] = df.apply(compute_risk, axis=1)
    pick = st.selectbox("Select shipment", options=range(len(df)), format_func=lambda i: f"#{i+1} {df.iloc[i]['origin']} → {df.iloc[i]['destination']} ({df.iloc[i]['cargo_type']})")
    row = df.iloc[pick]
    base_premium = premium_from_risk(row["risk_score"], row["cargo_value_aed"])

    st.write(f"Base Premium: **AED {base_premium:,.2f}**")
    adj = st.slider("Adjust premium (%)", -15, 15, 0, 1)
    final = round(base_premium * (1 + adj/100.0), 2)
    st.metric("Final Premium", f"AED {final:,.2f}", f"{adj}%")

    approved = st.checkbox("Approve quote")
    if approved:
        st.success(f"Approved at AED {final:,.2f} on {datetime.utcnow().strftime('%Y-%m-%d %H:%M UTC')}")
        st.caption("Version: v1.1 • Change log recorded (demo).")

# --------------------------
# Page: About
# --------------------------
else:
    st.title("About this Demo")
    st.markdown("""
This is a **Streamlit** demonstration of the Cargoes Shield AI Assistant.
It showcases: uploading shipments, instant quotes, a simple risk model, policy QnA, and an underwriter console.
For production, connect to real **RAG/LLM services**, **insurer APIs**, and **payments/CRM**.
""")
    st.info("Repo docs recommended: /docs/PRD.md, /docs/UserStories.md, /docs/TestingCriteria.md, /docs/FrontendGuide.md")
