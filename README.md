# 🔍 PitchLens — Silver Club Intelligence Platform

> AI-powered analytics platform for Charlotte FC's Silver Club premium segment.
> Built for the **2026 Sloan Sports Analytics Conference — First Pitch Case Competition**

## 🏟️ About

PitchLens is a deployable intelligence tool that helps Tepper Sports & Entertainment understand, retain, and grow Charlotte FC's Silver Club membership — the club's most important premium segment (~11,000 seats, ~$16M annual revenue).

## 🚀 Live Demo

👉 **[Try PitchLens](https://pitchlens.streamlit.app)**

Upload the KAGR dataset to unlock all features.

## ⚙️ Features

| Module | Description |
|--------|-------------|
| 📊 **Dashboard** | KPI cards, membership trends, ticket usage breakdown, segment comparison, persona clustering, AI-generated insights |
| 🔴 **Churn Risk Scorer** | ML-powered renewal prediction (Logistic Regression, AUC=0.84). Single account scoring with what-if analysis + bulk scoring with downloadable reports |
| 🎯 **Lead Scoring** | Identify & rank non-SC members most likely to upgrade. Filterable prospect lists with B2B opportunity detection |
| 🔍 **Data Explorer** | Custom chart builder, raw data browser, matchday attendance analysis |

## 🤖 Models

### Churn Prediction
- **Algorithm:** Logistic Regression + Random Forest
- **AUC-ROC:** 0.84 (LR) / 0.89 (RF)
- **Top Drivers:** SC Tenure (#1), Total Tickets, TSE Events, Unattended Rate
- **Use Case:** Score every SC member → prioritize retention outreach → recommended actions by risk tier

### Lead Scoring
- Composite score based on income, cross-TSE engagement, attendance, age, business indicator
- **Use Case:** Generate targeted upgrade prospect lists for sales reps

## 🧰 Tech Stack

- Python 3.11
- Streamlit
- Plotly (interactive charts)
- scikit-learn (ML models)
- Pandas + openpyxl

## 🛠️ Run Locally
```bash
git clone https://github.com/sarthaktuli7/pitchlens.git
cd pitchlens
pip install -r requirements.txt
streamlit run app.py
```

Then upload the `KAGR_Tepper_SSAC_Case_Competition_Dataset.xlsx` file in the sidebar.

## 📁 Structure
```
pitchlens/
├── app.py                  # Main Streamlit app (4 modules + AI insights)
├── .streamlit/
│   └── config.toml         # Dark theme config
├── requirements.txt        # Dependencies
└── README.md
```

## 👥 Team SU

| | |
|---|---|
| **Sarthak Tuli** | Syracuse University, Martin J. Whitman School of Management |
| **Pranali** | Syracuse University, Martin J. Whitman School of Management |

Built for the **SSAC 2026 First Pitch Case Competition**
Charlotte FC × KAGR × Tepper Sports & Entertainment
```

Save → then push:
```
git add .
git commit -m "updated README"
git push