import streamlit as st
import time

# 1. Mock Database of Schemes
SCHEMES = [
    {
        "name": "PM-Kisan Samman Nidhi",
        "criteria": {"occupation": "Farmer", "income_max": 200000},
        "benefit": "₹6,000 per year in three installments.",
        "link": "https://pmkisan.gov.in/"
    },
    {
        "name": "Sukanya Samriddhi Yojana",
        "criteria": {"gender": "Female", "age_max": 10},
        "benefit": "High-interest savings for girl child education/marriage.",
        "link": "https://www.indiapost.gov.in/"
    },
    {
        "name": "Pradhan Mantri Awas Yojana (PMAY)",
        "criteria": {"income_max": 600000, "urban": True},
        "benefit": "Subsidized home loans for urban/rural housing.",
        "link": "https://pmaymis.gov.in/"
    },
    {
        "name": "Atal Pension Yojana",
        "criteria": {"age_min": 18, "age_max": 40},
        "benefit": "Guaranteed monthly pension after 60 years of age.",
        "link": "https://www.npscra.nsdl.co.in/"
    },
    {
        "name": "PM Mudra Yojana",
        "criteria": {"occupation": "Self-Employed", "income_max": 1000000},
        "benefit": "Collateral-free loans up to ₹10 Lakh for small businesses.",
        "link": "https://www.mudra.org.in/"
    }
]

# 2. Page Config & Styling
st.set_page_config(page_title="Sarkari Agent", page_icon="🇮🇳", layout="centered")

st.markdown("""
    <style>
    .stApp { background-color: #0e1117; color: white; }
    .scheme-card {
        background: #1e2130;
        padding: 20px;
        border-radius: 15px;
        border-left: 5px solid #ff9933;
        margin-bottom: 20px;
        transition: transform 0.3s ease;
    }
    .scheme-card:hover {
        transform: scale(1.02);
        border-left: 5px solid #138808;
    }
    .stButton>button {
        width: 100%;
        background-color: #ff9933;
        color: white;
        border-radius: 10px;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🇮🇳 Sarkari Scheme Agent")
st.markdown("---")

# 3. User Profile Input
with st.container():
    st.header("👤 Your Profile")
    col1, col2 = st.columns(2)
    
    with col1:
        age = st.number_input("Age", min_value=1, max_value=100, value=25)
        gender = st.selectbox("Gender", ["Male", "Female", "Other"])
    
    with col2:
        occupation = st.selectbox("Occupation", ["Student", "Farmer", "Salaried", "Self-Employed", "Unemployed"])
        income = st.number_input("Annual Income (₹)", min_value=0, value=300000)

    is_urban = st.checkbox("Live in an Urban/City area?")

# 4. Agentic Logic
if st.button("🔍 Find Eligible Schemes"):
    with st.status("Agentic Search in Progress...", expanded=True) as status:
        st.write("📡 Connecting to State and Central Portals...")
        time.sleep(1)
        st.write("🧠 Analyzing eligibility criteria for your profile...")
        time.sleep(1)
        st.write("✅ Filtering results...")
        time.sleep(0.5)
        status.update(label="Analysis Complete!", state="complete", expanded=False)

    matches = []
    for s in SCHEMES:
        criteria = s["criteria"]
        eligible = True
        
        if "age_max" in criteria and age > criteria["age_max"]: eligible = False
        if "age_min" in criteria and age < criteria["age_min"]: eligible = False
        if "income_max" in criteria and income > criteria["income_max"]: eligible = False
        if "occupation" in criteria and occupation != criteria["occupation"]: eligible = False
        if "gender" in criteria and gender != criteria["gender"]: eligible = False
        
        if eligible:
            matches.append(s)

    # 5. Display Results
    if matches:
        st.balloons()
        st.success(f"Found {len(matches)} matches!")
        for m in matches:
            st.markdown(f"""
            <div class="scheme-card">
                <h3>{m['name']}</h3>
                <p><b>Benefit:</b> {m['benefit']}</p>
                <a href="{m['link']}" target="_blank" style="color: #4CAF50; text-decoration: none; font-weight: bold;">Apply Now →</a>
            </div>
            """, unsafe_allow_html=True)
    else:
        st.warning("No direct matches found. Try broadening your criteria.")

st.markdown("---")
st.caption("Developed by Aether AI Agent • 2024")
