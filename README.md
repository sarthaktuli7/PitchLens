# 🏟️ Charlotte FC Silver Club Intelligence Suite

> AI-powered analytics platform for Charlotte FC's Silver Club premium segment.  
> Built for the **2026 Sloan Sports Analytics Conference — First Pitch Case Competition**

## 🚀 Live Demo
👉 **[Try the app on Streamlit Cloud](https://your-app-url.streamlit.app)**

## ⚙️ Features

| Module | Description |
|--------|-------------|
| 📊 **Dashboard** | KPI cards, membership trends, ticket usage breakdown, segment comparison, persona clustering |
| 🔴 **Churn Risk Scorer** | ML-powered renewal prediction (Logistic Regression, AUC=0.84). Single account + bulk scoring with what-if analysis |
| 🎯 **Lead Scoring** | Identify & rank non-SC members most likely to upgrade. Downloadable prospect lists |
| 🔍 **Data Explorer** | Custom charts, raw data browser, matchday attendance analysis |

## 🧰 Tech Stack
- 🐍 Python 3.11+
- 🌐 Streamlit
- 📊 Plotly (interactive charts)
- 🤖 scikit-learn (ML models)
- 📁 Pandas + openpyxl

## 🛠️ Setup Locally

```bash
git clone https://github.com/yourusername/silver-club-intelligence.git
cd silver-club-intelligence
pip install -r requirements.txt
streamlit run app.py
```

Then upload the `KAGR_Tepper_SSAC_Case_Competition_Dataset.xlsx` file in the sidebar.

## 📊 Models

### Churn Prediction (Logistic Regression)
- **AUC-ROC**: 0.84
- **Top Drivers**: SC Tenure (#1), Total Tickets, TSE Events, Unattended Rate
- **Use Case**: Score every SC member → prioritize retention outreach

### Lead Scoring (Heuristic + ML)
- Composite score based on income, cross-TSE engagement, attendance, age alignment
- **Use Case**: Generate targeted upgrade prospect lists for sales reps

## 📁 Folder Structure
```
silver-club-intelligence/
├── app.py                  # Main Streamlit app (all 4 modules)
├── .streamlit/
│   └── config.toml         # Dark theme config
├── requirements.txt        # Dependencies
└── README.md
```

## 👨‍💻 Author
Built by **Sarthak Tuli** — Syracuse University, Whitman School of Management  
SSAC 2026 First Pitch Case Competition
