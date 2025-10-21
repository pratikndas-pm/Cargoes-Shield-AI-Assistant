# Cargoes Shield AI Assistant — Streamlit Demo

## Run Locally
```bash
pip install -r requirements.txt
streamlit run app.py
```
Open the URL shown in terminal (usually http://localhost:8501).

## Deploy to Streamlit Community Cloud
1. Push these files to a GitHub repo.
2. Go to https://share.streamlit.io/ → **New app**
3. Select your repo, branch, and `app.py` as the entrypoint.
4. Add secrets (if any) via the app's **Settings → Secrets**.

## Features
- Dashboard with KPIs
- Upload & Extract risk scoring
- Instant Quotes (3 plan options)
- Policy QnA (demo)
- Underwriter Console (±15% adjustment)

*Note:* This is a mock demo. Replace risk and QnA logic with production services.