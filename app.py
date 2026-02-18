"""
🔍 PitchLens — Silver Club Intelligence Platform
Team SU | Syracuse University, Whitman School of Management
SSAC 2026 First Pitch Case Competition
Built for Tepper Sports & Entertainment × Charlotte FC
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import warnings
warnings.filterwarnings('ignore')

# ============================================================
# PAGE CONFIG
# ============================================================
st.set_page_config(
    page_title="PitchLens | Silver Club Intelligence",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================
# CUSTOM CSS
# ============================================================
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;700&family=Space+Grotesk:wght@400;500;700&display=swap');
    
    .main { background-color: #0a0f1c; }
    .stApp { background: linear-gradient(135deg, #0a0f1c 0%, #111827 50%, #0f172a 100%); }
    
    /* Sidebar */
    [data-testid="stSidebar"] { 
        background: linear-gradient(180deg, #1B365D 0%, #0f2340 100%); 
    }
    [data-testid="stSidebar"] .stMarkdown p, 
    [data-testid="stSidebar"] .stMarkdown li,
    [data-testid="stSidebar"] label { color: #e2e8f0 !important; }
    
    /* Headers */
    h1, h2, h3 { font-family: 'Space Grotesk', sans-serif !important; color: #e2e8f0 !important; }
    p, li, label, .stMarkdown { font-family: 'DM Sans', sans-serif !important; }
    
    /* KPI Cards */
    .kpi-card {
        background: linear-gradient(135deg, #1e293b 0%, #1a2332 100%);
        border: 1px solid #334155;
        border-radius: 12px;
        padding: 20px 24px;
        text-align: center;
        transition: transform 0.2s, border-color 0.2s;
    }
    .kpi-card:hover { transform: translateY(-2px); border-color: #00B4D8; }
    .kpi-value { font-size: 2.2rem; font-weight: 700; font-family: 'Space Grotesk', sans-serif; }
    .kpi-label { font-size: 0.85rem; color: #94a3b8; margin-top: 4px; font-family: 'DM Sans', sans-serif; }
    .kpi-delta { font-size: 0.8rem; margin-top: 2px; }
    .delta-up { color: #2A9D8F; }
    .delta-down { color: #E63946; }
    
    /* Section headers */
    .section-header {
        font-family: 'Space Grotesk', sans-serif;
        font-size: 1.3rem;
        font-weight: 700;
        color: #e2e8f0;
        border-left: 4px solid #00B4D8;
        padding-left: 12px;
        margin: 24px 0 16px 0;
    }
    
    /* Risk badges */
    .risk-low { background: #065f46; color: #6ee7b7; padding: 4px 12px; border-radius: 20px; font-weight: 600; }
    .risk-med { background: #78350f; color: #fcd34d; padding: 4px 12px; border-radius: 20px; font-weight: 600; }
    .risk-high { background: #7f1d1d; color: #fca5a5; padding: 4px 12px; border-radius: 20px; font-weight: 600; }
            
    /* AI Insight boxes */
    .insight-box {
        background: linear-gradient(135deg, #0f2a1f 0%, #1a2332 100%);
        border: 1px solid #2A9D8F;
        border-left: 4px solid #2A9D8F;
        border-radius: 8px;
        padding: 16px 20px;
        margin: 12px 0;
        color: #e2e8f0;
        font-size: 0.95rem;
        line-height: 1.6;
    }
    .insight-box .insight-title {
        font-weight: 700;
        color: #2A9D8F;
        font-size: 0.85rem;
        text-transform: uppercase;
        letter-spacing: 0.5px;
        margin-bottom: 6px;
    }
    .warning-box {
        background: linear-gradient(135deg, #2a1a0f 0%, #1a2332 100%);
        border: 1px solid #E63946;
        border-left: 4px solid #E63946;
        border-radius: 8px;
        padding: 16px 20px;
        margin: 12px 0;
        color: #e2e8f0;
        font-size: 0.95rem;
        line-height: 1.6;
    }
    .warning-box .insight-title {
        font-weight: 700;
        color: #E63946;
        font-size: 0.85rem;
        text-transform: uppercase;
        letter-spacing: 0.5px;
        margin-bottom: 6px;
    }
    .recommendation-box {
        background: linear-gradient(135deg, #1a2510 0%, #1a2332 100%);
        border: 1px solid #C5A55A;
        border-left: 4px solid #C5A55A;
        border-radius: 8px;
        padding: 16px 20px;
        margin: 12px 0;
        color: #e2e8f0;
        font-size: 0.95rem;
        line-height: 1.6;
    }
    .recommendation-box .insight-title {
        font-weight: 700;
        color: #C5A55A;
        font-size: 0.85rem;
        text-transform: uppercase;
        letter-spacing: 0.5px;
        margin-bottom: 6px;
    }
    
    /* Persona cards */
    .persona-card {
        background: linear-gradient(135deg, #1e293b 0%, #1a2332 100%);
        border-radius: 12px;
        padding: 20px;
        border: 1px solid #334155;
        height: 100%;
    }
    .persona-title { font-size: 1.1rem; font-weight: 700; font-family: 'Space Grotesk', sans-serif; }
    .persona-stat { font-size: 0.85rem; color: #94a3b8; margin: 2px 0; }
    
    /* Override Streamlit defaults */
    .stMetric label { color: #94a3b8 !important; }
    .stMetric [data-testid="stMetricValue"] { color: #e2e8f0 !important; }
    .stTabs [data-baseweb="tab"] { color: #94a3b8 !important; }
    .stTabs [aria-selected="true"] { color: #00B4D8 !important; }
    div[data-testid="stExpander"] { border-color: #334155 !important; }
    
    /* Table styling */
    .dataframe { color: #e2e8f0 !important; }
    thead th { background-color: #1B365D !important; color: white !important; }
    
    /* Hide streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# ============================================================
# COLORS
# ============================================================
CFC_TEAL = '#00B4D8'
CFC_DARK = '#1B365D'
CFC_GOLD = '#C5A55A'
CFC_RED = '#E63946'
CFC_GREEN = '#2A9D8F'
CFC_GRAY = '#94a3b8'
SEGMENT_COLORS = {'Silver Club': CFC_TEAL, 'Supporters': CFC_GOLD, 'General/Other': '#6C757D', 'Other Premium': CFC_DARK}

# ============================================================
# AI INSIGHT GENERATORS
# ============================================================
def generate_dashboard_insights(sc_data, yr_data, master, selected_year, years):
    insights = []
    attend = sc_data['ATTENDANCE_RATE'].mean()
    unattend = sc_data['UNATTENDED_RATE'].mean()
    members = sc_data['AUDIENCEID'].nunique()
    
    ga_attend = yr_data[yr_data['SEGMENT'] == 'General/Other']['ATTENDANCE_RATE'].mean()
    if attend < ga_attend:
        insights.append(('warning', '⚠️ Attendance Alert',
            f'Silver Club members are attending only <b>{attend:.0%}</b> of their games — that\'s actually <b>lower</b> than General Admission fans ({ga_attend:.0%}) who pay significantly less. This means your highest-paying members are getting the least value from their investment.'))
    
    total_wasted = sc_data['STM_UNATTENDED_TIX'].sum()
    total_tix = sc_data['TOTAL_TIX'].sum()
    if unattend > 0.25:
        insights.append(('warning', '🚫 Ticket Waste Problem',
            f'<b>{unattend:.0%}</b> of Silver Club tickets go completely unused — that\'s roughly <b>{total_wasted:,}</b> out of <b>{total_tix:,}</b> tickets. These are seats that nobody sits in, nobody resells, nobody transfers. This represents lost value and is a leading indicator of future churn.'))
    
    if len(years) >= 2:
        prev_year = selected_year - 1
        prev_members = master[(master['SEASONYEAR'] == prev_year) & (master['SEGMENT'] == 'Silver Club')]['AUDIENCEID'].nunique()
        if prev_members > 0 and members < prev_members:
            drop = prev_members - members
            insights.append(('insight', '📉 Membership Declining',
                f'Silver Club membership dropped from <b>{prev_members:,}</b> to <b>{members:,}</b> — a loss of <b>{drop}</b> members year-over-year. The pipeline of new members joining SC isn\'t keeping up with attrition.'))
    
    cross_tse = sc_data['CROSS_TSE_FLAG'].mean()
    if cross_tse > 0.3:
        insights.append(('insight', '🌐 Cross-TSE Strength',
            f'<b>{cross_tse:.0%}</b> of Silver Club members also buy tickets to Panthers, BOA Stadium, or other TSE events. This is a competitive advantage — leverage this for bundled offers and cross-property retention strategies.'))
    
    ren_data = sc_data[sc_data['ACCOUNT_RENEWED_FLAG'].notna()]
    if len(ren_data) > 0:
        ren_rate = ren_data['ACCOUNT_RENEWED_FLAG'].mean()
        if ren_rate > 0.90:
            insights.append(('recommendation', '✅ Renewal is Strong',
                f'The current renewal rate is <b>{ren_rate:.1%}</b>. The opportunity isn\'t mass retention — it\'s <b>targeted saves</b> of the ~{int(len(ren_data)*(1-ren_rate))} members at risk, plus <b>growing the pipeline</b> of new members entering Silver Club.'))
    
    return insights

def render_insights(insights):
    for itype, title, text in insights:
        if itype == 'warning':
            box_class = 'warning-box'
        elif itype == 'recommendation':
            box_class = 'recommendation-box'
        else:
            box_class = 'insight-box'
        st.markdown(f"""<div class='{box_class}'>
            <div class='insight-title'>{title}</div>
            {text}
        </div>""", unsafe_allow_html=True)

def generate_persona_insights(sc_lat):
    insights = []
    for p in sorted(sc_lat['PERSONA'].unique()):
        g = sc_lat[sc_lat['PERSONA'] == p]
        attend = g['ATTENDANCE_RATE'].mean()
        unattend = g['UNATTENDED_RATE'].mean()
        transfer = g['TRANSFER_RATE'].mean()
        biz = g['BUSINESSINDICATOR'].mean()
        
        if attend < 0.15:
            insights.append(('warning', f'🪑 Absentee Owners ({len(g)} members)',
                f'This group attends only <b>{attend:.0%}</b> of games and leaves <b>{unattend:.0%}</b> unused. <b>Action:</b> Enable resale tools and a "Use It or Share It" campaign. If they can\'t monetize unused games, they\'ll stop renewing.'))
        elif biz > 0.5:
            insights.append(('insight', f'🏢 Corporate Entertainers ({len(g)} members)',
                f'Nearly <b>100% business accounts</b> with avg <b>{g["TOTAL_TIX"].mean():.0f} tickets</b>. <b>Action:</b> Assign dedicated account managers. Offer branded hosting nights. Losing one corporate account = losing 4-8 seats at once.'))
        elif attend > 0.5:
            insights.append(('recommendation', f'⚽ Devoted Fans ({len(g)} members)',
                f'Most engaged segment — <b>{attend:.0%}</b> attendance. <b>Action:</b> Launch a referral program. Each Devoted Fan who refers a new SC member gets F&B credit. They\'re your best salespeople.'))
        elif transfer > 0.4:
            insights.append(('insight', f'🎁 Gift Givers ({len(g)} members)',
                f'They transfer <b>{transfer:.0%}</b> of tickets to friends/colleagues. <b>Action:</b> Make sharing seamless — one-click transfer, group experience packages. The people they share with are your future SC buyers.'))
    return insights

# ============================================================
# DATA LOADING & PROCESSING
# ============================================================
@st.cache_data
def load_and_process(file):
    """Load Excel file and build master dataset"""
    xls = pd.ExcelFile(file)
    stm = pd.read_excel(xls, 'STM Profile Data')
    genome = pd.read_excel(xls, 'Fan Genome')
    renewal = pd.read_excel(xls, 'Renewal Contracts Data').dropna(axis=1, how='all')
    tse = pd.read_excel(xls, 'TSE Event Distribution Data')
    matchday = pd.read_excel(xls, 'Matchday Attributes Data')
    
    # Merge
    master = stm.merge(genome, on='AUDIENCEID', how='left')
    master = master.merge(tse, on=['AUDIENCEID', 'SEASONYEAR'], how='left')
    
    renewal_slim = renewal[['AUDIENCEID', 'SEASONYEAR', 'STADIUMLEVEL', 'ACCOUNT_RENEWED_FLAG', 'BUSINESSINDICATOR']].copy()
    renewal_slim.rename(columns={'BUSINESSINDICATOR': 'BIZ_TYPE'}, inplace=True)
    master = master.merge(renewal_slim, on=['AUDIENCEID', 'SEASONYEAR', 'STADIUMLEVEL'], how='left')
    
    # Calculated fields
    master['ATTENDANCE_RATE'] = (master['ATTENDED_TIX'] / master['TOTAL_TIX']).replace([np.inf, -np.inf], np.nan)
    master['RESALE_RATE'] = (master['STM_RESALE_TIX'] / master['TOTAL_TIX']).replace([np.inf, -np.inf], np.nan)
    master['TRANSFER_RATE'] = (master['STM_TRANSFER_TIX'] / master['TOTAL_TIX']).replace([np.inf, -np.inf], np.nan)
    master['UNATTENDED_RATE'] = (master['STM_UNATTENDED_TIX'] / master['TOTAL_TIX']).replace([np.inf, -np.inf], np.nan)
    
    for col in ['TOTAL_PANTHERS_EVENTS_PURCHASED', 'TOTAL_BOA_EVENTS_PURCHASED', 'TOTAL_OTHER_EVENTS_PURCHASED']:
        master[col] = master[col].fillna(0)
    master['CROSS_TSE_FLAG'] = ((master['TOTAL_PANTHERS_EVENTS_PURCHASED'] + master['TOTAL_BOA_EVENTS_PURCHASED'] + master['TOTAL_OTHER_EVENTS_PURCHASED']) > 0).astype(int)
    
    def assign_segment(row):
        if row['SILVERCLUBMEMBER'] == 'Yes': return 'Silver Club'
        sl = str(row['STADIUMLEVEL']).lower()
        if 'supporter' in sl: return 'Supporters'
        if any(x in sl for x in ['club','suite','vault','gallery','gridiron','huddle','veranda','centene']): return 'Other Premium'
        return 'General/Other'
    
    master['SEGMENT'] = master.apply(assign_segment, axis=1)
    
    sc_years = master[master['SILVERCLUBMEMBER'] == 'Yes'].groupby('AUDIENCEID')['SEASONYEAR'].agg(['min', 'count']).reset_index()
    sc_years.columns = ['AUDIENCEID', 'SC_FIRST_YEAR', 'SC_YEARS_COUNT']
    master = master.merge(sc_years, on='AUDIENCEID', how='left')
    
    income_map = {'Less Than $15,000':1,'$15,000 - $19,999':2,'$20,000 - $29,999':3,'$30,000 - $39,999':4,
                  '$40,000 - $49,999':5,'$50,000 - $74,999':6,'$75,000 - $99,999':7,'$100,000 - $124,999':8,'Greater Than $124,999':9}
    master['INCOME_NUM'] = master['INCOME'].map(income_map).fillna(5)
    master['AGE_CLEAN'] = master['AGE'].fillna(master['AGE'].median())
    
    section_map = {'Club 1':3,'Club 1A':3,'Club 1B':3,'Club 2':2,'Club 3':1}
    master['SECTION_TIER'] = master['STADIUMLEVEL'].map(section_map).fillna(2)
    
    return master, matchday

@st.cache_data
def build_churn_model(master):
    """Build logistic regression churn model and return coefficients"""
    from sklearn.linear_model import LogisticRegression
    from sklearn.preprocessing import StandardScaler
    from sklearn.model_selection import train_test_split
    from sklearn.metrics import roc_auc_score
    
    sc_ren = master[(master['SEGMENT'] == 'Silver Club') & (master['ACCOUNT_RENEWED_FLAG'].notna())].copy()
    features = ['ATTENDANCE_RATE','RESALE_RATE','TRANSFER_RATE','UNATTENDED_RATE','TOTAL_TIX',
                'INCOME_NUM','AGE_CLEAN','BUSINESSINDICATOR','CROSS_TSE_FLAG','SC_YEARS_COUNT',
                'SECTION_TIER','TOTAL_TSE_EVENTS_PURCHASED','TOTAL_PANTHERS_EVENTS_PURCHASED']
    
    X = sc_ren[features].fillna(0)
    y = sc_ren['ACCOUNT_RENEWED_FLAG']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42, stratify=y)
    scaler = StandardScaler()
    X_train_s = scaler.fit_transform(X_train)
    X_test_s = scaler.transform(X_test)
    
    lr = LogisticRegression(max_iter=1000, random_state=42)
    lr.fit(X_train_s, y_train)
    auc = roc_auc_score(y_test, lr.predict_proba(X_test_s)[:, 1])
    
    return lr, scaler, features, auc

def predict_churn(lr, scaler, features, input_dict):
    """Score a single account"""
    X = pd.DataFrame([input_dict])[features].fillna(0)
    X_s = scaler.transform(X)
    prob = lr.predict_proba(X_s)[0][1]
    return prob

# ============================================================
# SIDEBAR
# ============================================================
with st.sidebar:
    st.markdown("## 🔍 PitchLens")
    st.markdown("<span style='color:#64748b; font-size:0.8rem;'>by Team SU • Syracuse University</span>", unsafe_allow_html=True)
    st.markdown("---")
    
    uploaded_file = st.file_uploader("📁 Upload Dataset (.xlsx)", type=['xlsx'], 
                                      help="Upload the KAGR_Tepper_SSAC dataset")
    
    if uploaded_file:
        st.success("✅ Data loaded!")
        master, matchday = load_and_process(uploaded_file)
        years = sorted(master['SEASONYEAR'].unique())
        
        st.markdown("---")
        st.markdown("### Filters")
        selected_year = st.selectbox("📅 Season Year", years, index=len(years)-1)
        selected_segments = st.multiselect("🏷️ Segments", master['SEGMENT'].unique().tolist(), 
                                            default=master['SEGMENT'].unique().tolist())
    
    st.markdown("---")
    st.markdown("### Navigation")
    page = st.radio("", ["📊 Dashboard", "🔴 Churn Risk Scorer", "🎯 Lead Scoring", "🔍 Data Explorer"],
                     label_visibility="collapsed")
    
    st.markdown("---")
    st.markdown("""
    <div style='text-align:center; color:#64748b; font-size:0.75rem;'>
        🔍 PitchLens by Team SU<br>
        Sarthak & Pranali<br>
        Syracuse University • SSAC 2026
    </div>
    """, unsafe_allow_html=True)

# ============================================================
# MAIN CONTENT
# ============================================================
if not uploaded_file:
    # Landing page
    st.markdown("""
    <div style='text-align:center; padding:80px 20px;'>
        <h1 style='font-size:3rem; background: linear-gradient(135deg, #00B4D8, #C5A55A); -webkit-background-clip: text; -webkit-text-fill-color: transparent;'>
            🔍 PitchLens
        </h1>
        <p style='font-size:1.2rem; color:#94a3b8; max-width:600px; margin:20px auto;'>
            AI-powered intelligence platform for Charlotte FC's Silver Club premium segment.<br>
            <span style='color:#64748b; font-size:0.9rem;'>Team SU — Syracuse University, Whitman School of Management</span>
        </p>
        <div style='display:flex; justify-content:center; gap:40px; margin-top:40px;'>
            <div style='text-align:center;'>
                <div style='font-size:2rem;'>📊</div>
                <div style='color:#e2e8f0; font-weight:600;'>Live Dashboard</div>
                <div style='color:#64748b; font-size:0.85rem;'>KPIs, trends, personas</div>
            </div>
            <div style='text-align:center;'>
                <div style='font-size:2rem;'>🔴</div>
                <div style='color:#e2e8f0; font-weight:600;'>Churn Predictor</div>
                <div style='color:#64748b; font-size:0.85rem;'>ML-powered risk scoring</div>
            </div>
            <div style='text-align:center;'>
                <div style='font-size:2rem;'>🎯</div>
                <div style='color:#e2e8f0; font-weight:600;'>Lead Scorer</div>
                <div style='color:#64748b; font-size:0.85rem;'>Upgrade targeting</div>
            </div>
            <div style='text-align:center;'>
                <div style='font-size:2rem;'>🔍</div>
                <div style='color:#e2e8f0; font-weight:600;'>Data Explorer</div>
                <div style='color:#64748b; font-size:0.85rem;'>Query any metric</div>
            </div>
        </div>
        <p style='color:#475569; margin-top:60px; font-size:0.85rem;'>👈 Upload your dataset in the sidebar to get started</p>
    </div>
    """, unsafe_allow_html=True)
    st.stop()

# ============================================================
# PAGE 1: DASHBOARD
# ============================================================
if page == "📊 Dashboard":
    st.markdown("<h1>📊 Silver Club Dashboard</h1>", unsafe_allow_html=True)
    
    yr_data = master[master['SEASONYEAR'] == selected_year]
    sc_data = yr_data[yr_data['SEGMENT'] == 'Silver Club']
    prev_year = selected_year - 1
    sc_prev = master[(master['SEASONYEAR'] == prev_year) & (master['SEGMENT'] == 'Silver Club')] if prev_year in years else pd.DataFrame()
    
    # KPI Row
    col1, col2, col3, col4, col5 = st.columns(5)
    
    members = sc_data['AUDIENCEID'].nunique()
    prev_members = sc_prev['AUDIENCEID'].nunique() if len(sc_prev) > 0 else members
    delta_m = ((members - prev_members) / prev_members * 100) if prev_members > 0 else 0
    
    attend = sc_data['ATTENDANCE_RATE'].mean()
    prev_attend = sc_prev['ATTENDANCE_RATE'].mean() if len(sc_prev) > 0 else attend
    
    unattend = sc_data['UNATTENDED_RATE'].mean()
    renewal_data = sc_data[sc_data['ACCOUNT_RENEWED_FLAG'].notna()]
    ren_rate = renewal_data['ACCOUNT_RENEWED_FLAG'].mean() if len(renewal_data) > 0 else 0
    cross_tse = sc_data['CROSS_TSE_FLAG'].mean()
    
    with col1:
        delta_class = 'delta-up' if delta_m >= 0 else 'delta-down'
        st.markdown(f"""<div class='kpi-card'>
            <div class='kpi-value' style='color:{CFC_TEAL};'>{members:,}</div>
            <div class='kpi-label'>SC Members</div>
            <div class='kpi-delta {delta_class}'>{delta_m:+.1f}% YoY</div>
        </div>""", unsafe_allow_html=True)
    with col2:
        st.markdown(f"""<div class='kpi-card'>
            <div class='kpi-value' style='color:{"#E63946" if attend < 0.35 else "#2A9D8F"};'>{attend:.1%}</div>
            <div class='kpi-label'>Attendance Rate</div>
        </div>""", unsafe_allow_html=True)
    with col3:
        st.markdown(f"""<div class='kpi-card'>
            <div class='kpi-value' style='color:{"#E63946" if unattend > 0.3 else "#2A9D8F"};'>{unattend:.1%}</div>
            <div class='kpi-label'>Unattended Rate</div>
        </div>""", unsafe_allow_html=True)
    with col4:
        st.markdown(f"""<div class='kpi-card'>
            <div class='kpi-value' style='color:{CFC_GREEN};'>{ren_rate:.1%}</div>
            <div class='kpi-label'>Renewal Rate</div>
        </div>""", unsafe_allow_html=True)
    with col5:
        st.markdown(f"""<div class='kpi-card'>
            <div class='kpi-value' style='color:{CFC_GOLD};'>{cross_tse:.1%}</div>
            <div class='kpi-label'>Cross-TSE</div>
        </div>""", unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Charts Row 1
    col_left, col_right = st.columns(2)
    
    with col_left:
        st.markdown("<div class='section-header'>Membership Trend</div>", unsafe_allow_html=True)
        trend = master[master['SEGMENT'] == 'Silver Club'].groupby('SEASONYEAR')['AUDIENCEID'].nunique().reset_index()
        trend.columns = ['Year', 'Members']
        fig = px.bar(trend, x='Year', y='Members', color_discrete_sequence=[CFC_TEAL],
                     text='Members')
        fig.update_traces(textposition='outside', textfont_size=14)
        fig.update_layout(template='plotly_dark', paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',
                         height=350, margin=dict(t=20, b=40), xaxis_title='', yaxis_title='')
        st.plotly_chart(fig, use_container_width=True)
    
    with col_right:
        st.markdown("<div class='section-header'>Ticket Usage Breakdown</div>", unsafe_allow_html=True)
        usage = pd.DataFrame({
            'Category': ['Attended', 'Transferred', 'Resold', 'Unattended'],
            'Rate': [sc_data['ATTENDANCE_RATE'].mean(), sc_data['TRANSFER_RATE'].mean(),
                    sc_data['RESALE_RATE'].mean(), sc_data['UNATTENDED_RATE'].mean()],
            'Color': [CFC_GREEN, CFC_GOLD, CFC_TEAL, CFC_RED]
        })
        fig = px.bar(usage, x='Category', y='Rate', color='Category',
                    color_discrete_map={'Attended': CFC_GREEN, 'Transferred': CFC_GOLD, 'Resold': CFC_TEAL, 'Unattended': CFC_RED},
                    text=usage['Rate'].apply(lambda x: f'{x:.0%}'))
        fig.update_traces(textposition='outside', textfont_size=14)
        fig.update_layout(template='plotly_dark', paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',
                         height=350, margin=dict(t=20, b=40), showlegend=False, yaxis_tickformat='.0%', xaxis_title='', yaxis_title='')
        st.plotly_chart(fig, use_container_width=True)
    
    # Charts Row 2
    col_left2, col_right2 = st.columns(2)
    
    with col_left2:
        st.markdown("<div class='section-header'>Segment Comparison</div>", unsafe_allow_html=True)
        comp_data = []
        for seg in ['Silver Club', 'Supporters', 'General/Other', 'Other Premium']:
            s = yr_data[yr_data['SEGMENT'] == seg]
            if len(s) == 0: continue
            comp_data.append({'Segment': seg, 'Attendance': s['ATTENDANCE_RATE'].mean(), 
                            'Unattended': s['UNATTENDED_RATE'].mean()})
        comp_df = pd.DataFrame(comp_data)
        fig = go.Figure()
        fig.add_trace(go.Bar(name='Attendance', x=comp_df['Segment'], y=comp_df['Attendance'], 
                            marker_color=CFC_GREEN, text=comp_df['Attendance'].apply(lambda x: f'{x:.0%}'), textposition='outside'))
        fig.add_trace(go.Bar(name='Unattended', x=comp_df['Segment'], y=comp_df['Unattended'],
                            marker_color=CFC_RED, text=comp_df['Unattended'].apply(lambda x: f'{x:.0%}'), textposition='outside'))
        fig.update_layout(template='plotly_dark', paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',
                         height=350, margin=dict(t=20, b=40), barmode='group', yaxis_tickformat='.0%',
                         legend=dict(orientation='h', y=1.1), xaxis_title='', yaxis_title='')
        st.plotly_chart(fig, use_container_width=True)
    
    with col_right2:
        st.markdown("<div class='section-header'>Tenure vs Renewal Rate</div>", unsafe_allow_html=True)
        sc_ren = master[(master['SEGMENT'] == 'Silver Club') & (master['ACCOUNT_RENEWED_FLAG'].notna())]
        ten = sc_ren.groupby('SC_YEARS_COUNT')['ACCOUNT_RENEWED_FLAG'].agg(['mean', 'count']).reset_index()
        ten = ten[ten['SC_YEARS_COUNT'] <= 6]
        ten.columns = ['Years', 'Rate', 'Count']
        colors = [CFC_RED if r < 0.5 else CFC_GOLD if r < 0.85 else CFC_GREEN for r in ten['Rate']]
        fig = go.Figure(go.Bar(x=ten['Years'], y=ten['Rate'], marker_color=colors,
                               text=ten['Rate'].apply(lambda x: f'{x:.0%}'), textposition='outside'))
        fig.update_layout(template='plotly_dark', paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',
                         height=350, margin=dict(t=20, b=40), yaxis_tickformat='.0%',
                         xaxis_title='Years as SC Member', yaxis_title='Renewal Rate')
        fig.add_hline(y=0.9, line_dash='dash', line_color=CFC_GRAY, opacity=0.5)
        st.plotly_chart(fig, use_container_width=True)
    
    # Personas
    st.markdown("<div class='section-header'>Silver Club Personas</div>", unsafe_allow_html=True)
    
    from sklearn.preprocessing import StandardScaler
    from sklearn.cluster import KMeans
    
    sc_all = master[master['SEGMENT'] == 'Silver Club'].copy()
    sc_lat = sc_all.sort_values('SEASONYEAR', ascending=False).drop_duplicates('AUDIENCEID', keep='first')
    cluster_feats = ['ATTENDANCE_RATE','RESALE_RATE','TRANSFER_RATE','UNATTENDED_RATE','TOTAL_TIX',
                     'CROSS_TSE_FLAG','BUSINESSINDICATOR','INCOME_NUM','AGE_CLEAN']
    X_cl = sc_lat[cluster_feats].fillna(0)
    km = KMeans(n_clusters=4, random_state=42, n_init=10)
    sc_lat['PERSONA'] = km.fit_predict(StandardScaler().fit_transform(X_cl))
    
    pnames = {0: '🪑 Absentee Owner', 1: '🏢 Corporate Entertainer', 2: '⚽ Devoted Fan', 3: '🎁 Gift Giver'}
    pcolors = {0: CFC_RED, 1: CFC_DARK, 2: CFC_GREEN, 3: CFC_GOLD}
    
    pcols = st.columns(4)
    for i, p in enumerate(sorted(sc_lat['PERSONA'].unique())):
        g = sc_lat[sc_lat['PERSONA'] == p]
        with pcols[i]:
            st.markdown(f"""
            <div class='persona-card' style='border-left: 4px solid {pcolors[p]};'>
                <div class='persona-title' style='color:{pcolors[p]};'>{pnames[p]}</div>
                <div style='color:#64748b; font-size:0.85rem;'>{len(g)} members ({len(g)/len(sc_lat)*100:.0f}%)</div>
                <hr style='border-color:#334155; margin:8px 0;'>
                <div class='persona-stat'>📊 Attend: <b>{g['ATTENDANCE_RATE'].mean():.0%}</b></div>
                <div class='persona-stat'>🔄 Transfer: <b>{g['TRANSFER_RATE'].mean():.0%}</b></div>
                <div class='persona-stat'>🚫 Unattended: <b>{g['UNATTENDED_RATE'].mean():.0%}</b></div>
                <div class='persona-stat'>🎟️ Avg Tix: <b>{g['TOTAL_TIX'].mean():.0f}</b></div>
                <div class='persona-stat'>🏢 Business: <b>{g['BUSINESSINDICATOR'].mean():.0%}</b></div>
                <div class='persona-stat'>🌐 Cross-TSE: <b>{g['CROSS_TSE_FLAG'].mean():.0%}</b></div>
            </div>""", unsafe_allow_html=True)

# AI INSIGHTS SECTION
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("<div class='section-header'>🤖 AI-Generated Insights & Recommendations</div>", unsafe_allow_html=True)
    st.markdown("*PitchLens automatically analyzes your data and surfaces what matters most — in plain English.*")
    
    dashboard_insights = generate_dashboard_insights(sc_data, yr_data, master, selected_year, years)
    render_insights(dashboard_insights)
    
    st.markdown("<div class='section-header'>🎯 Persona-Specific Recommendations</div>", unsafe_allow_html=True)
    persona_insights = generate_persona_insights(sc_lat)
    render_insights(persona_insights)

# ============================================================
# PAGE 2: CHURN RISK SCORER
# ============================================================
elif page == "🔴 Churn Risk Scorer":
    st.markdown("<h1>🔴 Churn Risk Scorer</h1>", unsafe_allow_html=True)
    st.markdown("*ML-powered renewal prediction (Logistic Regression, AUC=0.84)*")
    
    lr_model, lr_scaler, lr_features, model_auc = build_churn_model(master)
    
    tab1, tab2 = st.tabs(["👤 Single Account", "📋 Bulk Scoring"])
    
    with tab1:
        st.markdown("<div class='section-header'>Score an Individual Account</div>", unsafe_allow_html=True)
        
        col1, col2, col3 = st.columns(3)
        with col1:
            sc_years = st.slider("SC Tenure (years)", 1, 10, 4)
            total_tix = st.slider("Total Tickets", 2, 200, 36)
            attend_rate = st.slider("Attendance Rate", 0.0, 1.0, 0.35, 0.05)
            resale_rate = st.slider("Resale Rate", 0.0, 1.0, 0.05, 0.05)
        with col2:
            transfer_rate = st.slider("Transfer Rate", 0.0, 1.0, 0.30, 0.05)
            unattend_rate = st.slider("Unattended Rate", 0.0, 1.0, 0.30, 0.05)
            income = st.slider("Income Level (1-9)", 1, 9, 7, help="1=<$15K ... 9=$125K+")
            age = st.slider("Age", 18, 80, 48)
        with col3:
            is_business = st.selectbox("Business Account?", [0, 1], format_func=lambda x: "Yes" if x else "No")
            cross_tse = st.selectbox("Cross-TSE Buyer?", [0, 1], index=1, format_func=lambda x: "Yes" if x else "No")
            section_tier = st.selectbox("Section", [1, 2, 3], index=2, format_func=lambda x: {1:'Club 3', 2:'Club 2', 3:'Club 1'}[x])
            tse_events = st.slider("TSE Events Purchased", 0, 50, 20)
            panthers_events = st.slider("Panthers Events", 0, 20, 0)
        
        input_dict = {
            'ATTENDANCE_RATE': attend_rate, 'RESALE_RATE': resale_rate, 'TRANSFER_RATE': transfer_rate,
            'UNATTENDED_RATE': unattend_rate, 'TOTAL_TIX': total_tix, 'INCOME_NUM': income,
            'AGE_CLEAN': age, 'BUSINESSINDICATOR': is_business, 'CROSS_TSE_FLAG': cross_tse,
            'SC_YEARS_COUNT': sc_years, 'SECTION_TIER': section_tier,
            'TOTAL_TSE_EVENTS_PURCHASED': tse_events, 'TOTAL_PANTHERS_EVENTS_PURCHASED': panthers_events
        }
        
        prob = predict_churn(lr_model, lr_scaler, lr_features, input_dict)
        
        # Results
        st.markdown("<br>", unsafe_allow_html=True)
        r1, r2, r3 = st.columns([1, 1, 2])
        
        with r1:
            color = CFC_GREEN if prob > 0.9 else CFC_GOLD if prob > 0.7 else CFC_RED
            st.markdown(f"""<div class='kpi-card' style='border-color:{color};'>
                <div class='kpi-value' style='color:{color};'>{prob:.1%}</div>
                <div class='kpi-label'>Renewal Probability</div>
            </div>""", unsafe_allow_html=True)
        
        with r2:
            if prob > 0.9:
                tier, badge = "LOW RISK", "risk-low"
            elif prob > 0.7:
                tier, badge = "MEDIUM RISK", "risk-med"
            else:
                tier, badge = "HIGH RISK", "risk-high"
            st.markdown(f"""<div class='kpi-card'>
                <div style='margin-top:10px;'><span class='{badge}'>{tier}</span></div>
                <div class='kpi-label' style='margin-top:12px;'>Risk Classification</div>
            </div>""", unsafe_allow_html=True)
        
        with r3:
            if prob > 0.9:
                action = "✅ **Standard renewal outreach.** Offer early-bird discount or loyalty perk. Low intervention needed."
            elif prob > 0.7:
                action = "⚠️ **Proactive rep outreach.** Schedule personal call. Offer flex-plan, upgraded F&B credit, or seat relocation."
            elif prob > 0.5:
                action = "🔶 **Urgent intervention.** Manager-led call. Offer trial upgrade to Club 1, partial plan, or payment flexibility."
            else:
                action = "🔴 **Emergency save.** VP/Director personal contact. Significant concession or structured exit interview."
            st.markdown(f"""<div class='kpi-card'>
                <div style='text-align:left; color:#e2e8f0; font-size:0.95rem;'>{action}</div>
            </div>""", unsafe_allow_html=True)
        
        # What-if analysis
        st.markdown("<div class='section-header'>🔮 What-If Analysis</div>", unsafe_allow_html=True)
        st.markdown("*See how changes impact renewal probability:*")
        
        scenarios = []
        for sc_y in [sc_years, min(sc_years+1, 10)]:
            for att in [attend_rate, min(attend_rate + 0.15, 1.0)]:
                for tse_e in [tse_events, tse_events + 5]:
                    d = input_dict.copy()
                    d['SC_YEARS_COUNT'] = sc_y
                    d['ATTENDANCE_RATE'] = att
                    d['TOTAL_TSE_EVENTS_PURCHASED'] = tse_e
                    p = predict_churn(lr_model, lr_scaler, lr_features, d)
                    label = []
                    if sc_y != sc_years: label.append(f"+1yr tenure")
                    if att != attend_rate: label.append(f"+15% attendance")
                    if tse_e != tse_events: label.append(f"+5 TSE events")
                    if not label: label = ["Current"]
                    scenarios.append({'Scenario': ' + '.join(label), 'Renewal_Prob': p})
        
        sc_df = pd.DataFrame(scenarios).drop_duplicates('Scenario').sort_values('Renewal_Prob', ascending=False)
        fig = px.bar(sc_df, x='Renewal_Prob', y='Scenario', orientation='h', 
                    color='Renewal_Prob', color_continuous_scale=['#E63946', '#C5A55A', '#2A9D8F'],
                    text=sc_df['Renewal_Prob'].apply(lambda x: f'{x:.1%}'))
        fig.update_traces(textposition='outside')
        fig.update_layout(template='plotly_dark', paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',
                         height=350, margin=dict(l=200), xaxis_tickformat='.0%', coloraxis_showscale=False,
                         xaxis_title='Renewal Probability', yaxis_title='')
        st.plotly_chart(fig, use_container_width=True)
    
    with tab2:
        st.markdown("<div class='section-header'>Bulk Score All Current SC Members</div>", unsafe_allow_html=True)
        
        if st.button("🚀 Score All Silver Club Members", type="primary"):
            sc_current = master[(master['SEASONYEAR'] == selected_year) & (master['SEGMENT'] == 'Silver Club')].copy()
            sc_current = sc_current.drop_duplicates('AUDIENCEID')
            
            X_bulk = sc_current[lr_features].fillna(0)
            X_bulk_s = lr_scaler.transform(X_bulk)
            sc_current['RENEWAL_PROB'] = lr_model.predict_proba(X_bulk_s)[:, 1]
            sc_current['RISK_TIER'] = sc_current['RENEWAL_PROB'].apply(
                lambda x: '🟢 Low' if x > 0.9 else '🟡 Medium' if x > 0.7 else '🔴 High')
            
            # Summary
            c1, c2, c3 = st.columns(3)
            with c1:
                low = (sc_current['RENEWAL_PROB'] > 0.9).sum()
                st.markdown(f"""<div class='kpi-card'><div class='kpi-value' style='color:{CFC_GREEN};'>{low}</div>
                    <div class='kpi-label'>🟢 Low Risk</div></div>""", unsafe_allow_html=True)
            with c2:
                med = ((sc_current['RENEWAL_PROB'] > 0.7) & (sc_current['RENEWAL_PROB'] <= 0.9)).sum()
                st.markdown(f"""<div class='kpi-card'><div class='kpi-value' style='color:{CFC_GOLD};'>{med}</div>
                    <div class='kpi-label'>🟡 Medium Risk</div></div>""", unsafe_allow_html=True)
            with c3:
                high = (sc_current['RENEWAL_PROB'] <= 0.7).sum()
                st.markdown(f"""<div class='kpi-card'><div class='kpi-value' style='color:{CFC_RED};'>{high}</div>
                    <div class='kpi-label'>🔴 High Risk</div></div>""", unsafe_allow_html=True)
            
            # Table
            display_cols = ['AUDIENCEID', 'STADIUMLEVEL', 'CITY', 'AGE', 'INCOME', 'ATTENDANCE_RATE',
                          'UNATTENDED_RATE', 'SC_YEARS_COUNT', 'RENEWAL_PROB', 'RISK_TIER']
            st.dataframe(sc_current[display_cols].sort_values('RENEWAL_PROB').head(50), 
                        use_container_width=True, height=400)
            
            # Download
            csv = sc_current[display_cols].sort_values('RENEWAL_PROB').to_csv(index=False)
            st.download_button("📥 Download Full Risk Report", csv, "sc_churn_risk_report.csv", "text/csv")

# ============================================================
# PAGE 3: LEAD SCORING
# ============================================================
elif page == "🎯 Lead Scoring":
    st.markdown("<h1>🎯 Upgrade Lead Scoring</h1>", unsafe_allow_html=True)
    st.markdown("*Identify non-SC members most likely to upgrade to Silver Club*")
    
    st.markdown("<div class='section-header'>Top Upgrade Prospects</div>", unsafe_allow_html=True)
    
    # Simple heuristic scoring (since actual upgrades are very rare)
    non_sc = master[(master['SEASONYEAR'] == selected_year) & (master['SEGMENT'] != 'Silver Club')].copy()
    non_sc = non_sc.drop_duplicates('AUDIENCEID')
    
    # Score based on SC-like attributes
    non_sc['SCORE'] = (
        non_sc['INCOME_NUM'] / 9 * 25 +  # Higher income = more likely
        non_sc['CROSS_TSE_FLAG'] * 20 +  # Cross-TSE buyer
        non_sc['AGE_CLEAN'].clip(30, 60).apply(lambda x: (x - 30) / 30) * 15 +  # Age 30-60 sweet spot
        (1 - non_sc['UNATTENDED_RATE'].fillna(0.5)) * 20 +  # Lower unattended = more engaged
        non_sc['ATTENDANCE_RATE'].fillna(0.3) * 20  # Higher attendance
    )
    non_sc['SCORE'] = non_sc['SCORE'].clip(0, 100)
    
    # Filters
    col1, col2, col3 = st.columns(3)
    with col1:
        min_score = st.slider("Min Score", 0, 100, 60)
    with col2:
        seg_filter = st.multiselect("Current Segment", non_sc['SEGMENT'].unique().tolist(), default=non_sc['SEGMENT'].unique().tolist())
    with col3:
        city_filter = st.text_input("City Filter", placeholder="e.g., Charlotte")
    
    filtered = non_sc[non_sc['SCORE'] >= min_score]
    filtered = filtered[filtered['SEGMENT'].isin(seg_filter)]
    if city_filter:
        filtered = filtered[filtered['CITY'].str.contains(city_filter, case=False, na=False)]
    
    st.markdown(f"**{len(filtered):,} prospects** match your criteria")
    
    display_cols = ['AUDIENCEID', 'SEGMENT', 'CITY', 'STATE', 'AGE', 'INCOME', 'ATTENDANCE_RATE',
                   'TOTAL_TIX', 'CROSS_TSE_FLAG', 'SCORE']
    st.dataframe(filtered[display_cols].sort_values('SCORE', ascending=False).head(100),
                use_container_width=True, height=500)
    
    # Score distribution
    fig = px.histogram(non_sc, x='SCORE', nbins=30, color_discrete_sequence=[CFC_TEAL],
                      title='Upgrade Score Distribution (All Non-SC Members)')
    fig.add_vline(x=min_score, line_dash='dash', line_color=CFC_RED)
    fig.update_layout(template='plotly_dark', paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',
                     height=300, margin=dict(t=40))
    st.plotly_chart(fig, use_container_width=True)
    
    csv = filtered[display_cols].sort_values('SCORE', ascending=False).to_csv(index=False)
    st.download_button("📥 Download Prospect List", csv, "sc_upgrade_prospects.csv", "text/csv")

# ============================================================
# PAGE 4: DATA EXPLORER
# ============================================================
elif page == "🔍 Data Explorer":
    st.markdown("<h1>🔍 Data Explorer</h1>", unsafe_allow_html=True)
    
    tab1, tab2, tab3 = st.tabs(["📊 Custom Charts", "📋 Data Table", "📈 Matchday Analysis"])
    
    with tab1:
        st.markdown("<div class='section-header'>Build Custom Visualizations</div>", unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        with col1:
            metric = st.selectbox("Metric", ['ATTENDANCE_RATE', 'RESALE_RATE', 'TRANSFER_RATE', 'UNATTENDED_RATE',
                                              'TOTAL_TIX', 'AGE', 'INCOME_NUM', 'CROSS_TSE_FLAG'])
        with col2:
            group_by = st.selectbox("Group By", ['SEGMENT', 'SEASONYEAR', 'STADIUMLEVEL', 'INCOME', 'CITY'])
        
        chart_data = master.groupby(group_by)[metric].mean().reset_index().sort_values(metric, ascending=False).head(20)
        fig = px.bar(chart_data, x=group_by, y=metric, color_discrete_sequence=[CFC_TEAL],
                    text=chart_data[metric].apply(lambda x: f'{x:.2f}'))
        fig.update_traces(textposition='outside')
        fig.update_layout(template='plotly_dark', paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',
                         height=400, margin=dict(t=20))
        st.plotly_chart(fig, use_container_width=True)
    
    with tab2:
        st.markdown("<div class='section-header'>Raw Data Browser</div>", unsafe_allow_html=True)
        
        seg_filt = st.multiselect("Segment", master['SEGMENT'].unique().tolist(), default=['Silver Club'], key='explorer_seg')
        yr_filt = st.multiselect("Year", sorted(master['SEASONYEAR'].unique()), default=[selected_year], key='explorer_yr')
        
        filtered = master[(master['SEGMENT'].isin(seg_filt)) & (master['SEASONYEAR'].isin(yr_filt))]
        st.markdown(f"**{len(filtered):,} rows** | **{filtered['AUDIENCEID'].nunique():,} unique accounts**")
        st.dataframe(filtered.head(500), use_container_width=True, height=500)
    
    with tab3:
        st.markdown("<div class='section-header'>Matchday Attendance Analysis</div>", unsafe_allow_html=True)
        
        md_year = st.selectbox("Season", sorted(matchday['SEASONYEAR'].unique()), index=len(matchday['SEASONYEAR'].unique())-1)
        md_yr = matchday[(matchday['SEASONYEAR'] == md_year) & (matchday['SILVERCLUBMEMBER'] == 'Yes')]
        md_agg = md_yr.groupby('EVENTANDDATE')['ATTENDED_PERC'].mean().reset_index().sort_values('ATTENDED_PERC')
        
        fig = px.bar(md_agg, x='ATTENDED_PERC', y='EVENTANDDATE', orientation='h',
                    color='ATTENDED_PERC', color_continuous_scale=['#E63946', '#C5A55A', '#2A9D8F'],
                    text=md_agg['ATTENDED_PERC'].apply(lambda x: f'{x:.0%}'))
        fig.update_traces(textposition='outside')
        fig.update_layout(template='plotly_dark', paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',
                         height=max(len(md_agg) * 25, 400), margin=dict(l=300), coloraxis_showscale=False,
                         xaxis_tickformat='.0%', xaxis_title='SC Attendance %', yaxis_title='')
        st.plotly_chart(fig, use_container_width=True)
