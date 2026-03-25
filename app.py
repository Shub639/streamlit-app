

import streamlit as st
import base64
import os

# ---- Page Config ----
st.set_page_config(
    page_title="DECIDE",
    page_icon="\U0001f3e5",
    layout="centered",
    initial_sidebar_state="expanded"
)

# ---- Helper: Load image as base64 ----
def load_image_base64(filename):
    filepath = os.path.join(os.path.dirname(os.path.abspath(__file__)), filename)
    if os.path.exists(filepath):
        with open(filepath, "rb") as f:
            return base64.b64encode(f.read()).decode()
    return None

# ---- Load background and logo ----
bg_data = load_image_base64("background.jpg")
logo_data = load_image_base64("logo.png")

# ---- Custom CSS Styling ----
bg_css = ""
if bg_data:
    bg_css = f"""
    .stApp {{
        background-image: url("data:image/jpeg;base64,{bg_data}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}
    .stApp::before {{
        content: '';
        position: fixed;
        top: 0; left: 0; right: 0; bottom: 0;
        background: rgba(247, 250, 250, 0.88);
        z-index: 0;
    }}
    .stApp > div {{
        position: relative;
        z-index: 1;
    }}
    """

st.markdown(f"""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;600;700&family=Inter:wght@300;400;500;600&display=swap');

    {bg_css}

    /* Sidebar styling */
    [data-testid="stSidebar"] {{
        background: linear-gradient(180deg, #0D2B45 0%, #1B4D72 100%);
    }}
    [data-testid="stSidebar"] * {{
        color: white !important;
    }}

    /* Headings */
    .main-title {{
        font-family: 'Playfair Display', serif;
        font-size: 80px;
        font-weight: 700;
        text-align: center;
        color: #0D2B45;
        margin-bottom: 0px;
        letter-spacing: 6px;
    }}
    .subtitle {{
        font-family: 'Inter', sans-serif;
        font-size: 18px;
        font-weight: 400;
        text-align: center;
        color: #1B4D72;
        letter-spacing: 3px;
        text-transform: uppercase;
        margin-top: 0px;
    }}
    .tagline {{
        font-family: 'Playfair Display', serif;
        font-size: 22px;
        font-style: italic;
        text-align: center;
        color: #2A9D8F;
        margin-top: 10px;
        margin-bottom: 30px;
    }}
    .description {{
        font-family: 'Inter', sans-serif;
        font-size: 17px;
        text-align: center;
        color: #555;
        max-width: 700px;
        margin: 0 auto;
        line-height: 1.7;
    }}
    .section-title {{
        font-family: 'Playfair Display', serif;
        font-size: 32px;
        font-weight: 600;
        text-align: center;
        color: #0D2B45;
        margin-top: 40px;
        margin-bottom: 30px;
    }}

    /* Step Cards */
    .step-card {{
        background: rgba(255, 255, 255, 0.95);
        border-radius: 16px;
        padding: 30px 20px;
        text-align: center;
        box-shadow: 0 4px 20px rgba(13, 43, 69, 0.08);
        border: 1px solid #E8F0F2;
        transition: transform 0.2s ease;
        min-height: 220px;
    }}
    .step-card:hover {{
        transform: translateY(-4px);
        box-shadow: 0 8px 30px rgba(13, 43, 69, 0.12);
    }}
    .step-icon {{
        font-size: 48px;
        margin-bottom: 10px;
    }}
    .step-number {{
        font-family: 'Playfair Display', serif;
        font-size: 20px;
        font-weight: 600;
        color: #2A9D8F;
        margin-bottom: 8px;
    }}
    .step-text {{
        font-family: 'Inter', sans-serif;
        font-size: 15px;
        color: #555;
        line-height: 1.5;
    }}

    /* Divider */
    .custom-divider {{
        width: 80px;
        height: 3px;
        background: linear-gradient(90deg, #2A9D8F, #1B4D72);
        margin: 30px auto;
        border-radius: 2px;
    }}

    /* Footer */
    .footer {{
        font-family: 'Inter', sans-serif;
        text-align: center;
        color: #aaa;
        font-size: 13px;
        margin-top: 50px;
        padding-bottom: 20px;
    }}

    /* Button styling */
    .stButton > button[kind="primary"] {{
        background: linear-gradient(135deg, #1B4D72, #2A9D8F) !important;
        color: white !important;
        border: none !important;
        border-radius: 12px !important;
        padding: 12px 40px !important;
        font-family: 'Inter', sans-serif !important;
        font-size: 16px !important;
        font-weight: 500 !important;
        letter-spacing: 1px !important;
    }}
</style>
""", unsafe_allow_html=True)

# ---- Sidebar Navigation ----
page = st.sidebar.radio(
    "Navigate",
    ["Home", "About DECIDE", "Start Evaluation", "Results", "Resources"]
)

# ---- Home Page ----
if page == "Home":

    # Logo
    if logo_data:
        st.markdown(f'<div style="text-align:center; margin-bottom:20px;"><img src="data:image/png;base64,{logo_data}" width="160"></div>', unsafe_allow_html=True)

    st.markdown("")

    # Title
    st.markdown('<div class="main-title">DECIDE</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">Digital Evaluation for Community Implementation Decisions</div>', unsafe_allow_html=True)
    st.markdown('<div class="tagline">"Before you adopt, evaluate."</div>', unsafe_allow_html=True)

    # Divider
    st.markdown('<div class="custom-divider"></div>', unsafe_allow_html=True)

    # Description
    st.markdown('<div class="description">A free, evidence-based tool that helps community health centers evaluate digital health technologies before adoption \u2014 protecting your patients, your staff, and your budget.</div>', unsafe_allow_html=True)

    # How It Works
    st.markdown('<div class="section-title">How It Works</div>', unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div class="step-card">
            <div class="step-icon">\U0001f6a6</div>
            <div class="step-number">Step 1</div>
            <div class="step-text">Screen for deal-breakers with 5 quick yes/no questions</div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="step-card">
            <div class="step-icon">\U0001f4cb</div>
            <div class="step-number">Step 2</div>
            <div class="step-text">Evaluate across 5 evidence-based pillars: Cost, Staff, Equity, Privacy, Sustainability</div>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="step-card">
            <div class="step-icon">\u2705</div>
            <div class="step-number">Step 3</div>
            <div class="step-text">Get a scored recommendation with an actionable report for your board</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("")
    st.markdown("")

    # Start Button
    col_left, col_center, col_right = st.columns([1, 2, 1])
    with col_center:
        if st.button("Start Evaluation", use_container_width=True, type="primary"):
            st.session_state["nav"] = "eval"

    # Footer
    st.markdown('<div class="footer">Built for the Hack the Health Gap Hackathon 2026</div>', unsafe_allow_html=True)

# ---- Placeholder pages ----
elif page == "About DECIDE":

    # Logo
    if logo_data:
        st.markdown(f'<div style="text-align:center; margin-bottom:20px;"><img src="data:image/png;base64,{logo_data}" width="120"></div>', unsafe_allow_html=True)

    st.markdown('<div class="section-title">About DECIDE</div>', unsafe_allow_html=True)

    # The Problem
    st.markdown("""
    <div style="background: rgba(255,255,255,0.95); border-radius:14px; padding:28px; margin-bottom:24px; box-shadow: 0 2px 12px rgba(13,43,69,0.06); border-left: 4px solid #E76F51;">
        <h3 style="font-family:'Playfair Display',serif; color:#0D2B45; margin-top:0;">The Problem</h3>
        <p style="font-family:'Inter',sans-serif; font-size:15px; color:#444; line-height:1.7;">
            Digital health tools promise to transform community health centers. But the reality is alarming:<br><br>
            <strong>\u2022 Nearly 50%</strong> of digital health implementations fail, with cost being the #1 reason.<br>
            <strong>\u2022 EHR adoption</strong> was supposed to save money \u2014 instead it costs billions and became a leading cause of physician burnout. Primary care doctors now spend up to 6 hours per day on EHR tasks.<br>
            <strong>\u2022 AI algorithms</strong> have been shown to systematically under-serve Black patients. A widely used risk prediction tool was found to require Black patients to be considerably sicker than white patients to receive the same level of care.<br>
            <strong>\u2022 Community health centers</strong> \u2014 serving America's most vulnerable populations \u2014 are the least equipped to evaluate these tools and the least able to absorb losses when they fail.
        </p>
    </div>
    """, unsafe_allow_html=True)

    # Our Mission
    st.markdown("""
    <div style="background: rgba(255,255,255,0.95); border-radius:14px; padding:28px; margin-bottom:24px; box-shadow: 0 2px 12px rgba(13,43,69,0.06); border-left: 4px solid #2A9D8F;">
        <h3 style="font-family:'Playfair Display',serif; color:#0D2B45; margin-top:0;">Our Mission</h3>
        <p style="font-family:'Inter',sans-serif; font-size:15px; color:#444; line-height:1.7;">
            To give every community health center a free, evidence-based framework to evaluate digital health tools <strong>before</strong> adoption \u2014 so no clinic wastes scarce resources on technology that doesn't serve its patients.
        </p>
    </div>
    """, unsafe_allow_html=True)

    # Our Goal
    st.markdown("""
    <div style="background: rgba(255,255,255,0.95); border-radius:14px; padding:28px; margin-bottom:24px; box-shadow: 0 2px 12px rgba(13,43,69,0.06); border-left: 4px solid #1B4D72;">
        <h3 style="font-family:'Playfair Display',serif; color:#0D2B45; margin-top:0;">Our Goal</h3>
        <p style="font-family:'Inter',sans-serif; font-size:15px; color:#444; line-height:1.7;">
            Ensure every CHC can make informed technology decisions that protect their <strong>patients</strong>, support their <strong>staff</strong>, respect <strong>privacy</strong>, promote <strong>equity</strong>, and remain <strong>sustainable</strong> long-term.
        </p>
    </div>
    """, unsafe_allow_html=True)

    # The Five Pillars
    st.markdown('<div class="section-title">The Five Pillars</div>', unsafe_allow_html=True)

    pillars = [
        ("\U0001f4b0", "Cost & Value", "Can the CHC afford this tool? Will it save money or time? Grounded in health economic evaluation methods."),
        ("\U0001f469\u200d\u2695\ufe0f", "Staff Readiness", "Do staff have the time and skills to use this? Based on the Consolidated Framework for Implementation Research (CFIR)."),
        ("\U0001f91d", "Patient Trust & Equity", "Will patients accept this? Does it work across languages, ages, and demographics? Built on the HEAL fairness framework."),
        ("\U0001f512", "Privacy & Security", "Does it meet HIPAA? Who controls the data? Mapped to Privacy by Design principles."),
        ("\U0001f504", "Sustainability", "Can this be maintained long-term? Based on the NASSS framework for digital health sustainability."),
    ]

    for icon, title, desc in pillars:
        st.markdown(f"""
        <div style="background: rgba(255,255,255,0.95); border-radius:14px; padding:20px 24px; margin-bottom:14px; box-shadow: 0 2px 12px rgba(13,43,69,0.06); display:flex; align-items:center;">
            <div style="font-size:36px; margin-right:20px;">{icon}</div>
            <div>
                <div style="font-family:'Playfair Display',serif; font-size:18px; font-weight:600; color:#0D2B45;">{title}</div>
                <div style="font-family:'Inter',sans-serif; font-size:14px; color:#555; margin-top:4px;">{desc}</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    # Who Is This For
    st.markdown("""
    <div style="background: rgba(255,255,255,0.95); border-radius:14px; padding:28px; margin-top:30px; margin-bottom:24px; box-shadow: 0 2px 12px rgba(13,43,69,0.06); border-left: 4px solid #264653;">
        <h3 style="font-family:'Playfair Display',serif; color:#0D2B45; margin-top:0;">Who Is This For?</h3>
        <p style="font-family:'Inter',sans-serif; font-size:15px; color:#444; line-height:1.7;">
            \u2022 CHC Executive Directors & CFOs<br>
            \u2022 Clinical Directors & Medical Directors<br>
            \u2022 Project Directors & Grant Managers<br>
            \u2022 Patient Advisory Board Members<br>
            \u2022 State Primary Care Associations & FQHC Networks
        </p>
    </div>
    """, unsafe_allow_html=True)


elif page == "Start Evaluation":

    if logo_data:
        st.markdown(f'<div style="text-align:center; margin-bottom:10px;"><img src="data:image/png;base64,{logo_data}" width="80"></div>', unsafe_allow_html=True)

    st.markdown('<div class="section-title">Evaluate a Digital Health Tool</div>', unsafe_allow_html=True)

    screening, p1, p2, p3, p4, p5 = st.tabs([
        "Quick Screening",
        "Pillar 1: Cost & Value",
        "Pillar 2: Staff Readiness",
        "Pillar 3: Patient Trust & Equity",
        "Pillar 4: Privacy & Security",
        "Pillar 5: Sustainability"
    ])

    # ===================== QUICK SCREENING =====================
    with screening:
        st.markdown("<h3 style='font-family:Playfair Display,serif; color:#0D2B45;'>Quick Screening</h3>", unsafe_allow_html=True)
        st.markdown("<p style='font-family:Inter,sans-serif; color:#555;'>Answer these 5 deal-breaker questions first. If any answer is <strong>No</strong>, the tool flags it as a potential non-starter.</p>", unsafe_allow_html=True)

        tool_name = st.text_input("What is the name of the digital health tool you are evaluating?")

        s1 = st.radio("1. Does the vendor provide a HIPAA Business Associate Agreement (BAA)?", ["Yes", "No", "Not sure"], horizontal=True, key="s1")
        s2 = st.radio("2. Does the tool work on mobile devices and low-bandwidth connections?", ["Yes", "No", "Not sure"], horizontal=True, key="s2")
        s3 = st.radio("3. Does the tool support your patients' primary languages?", ["Yes", "No", "Not sure"], horizontal=True, key="s3")
        s4 = st.radio("4. Does the vendor offer a free trial or pilot period?", ["Yes", "No", "Not sure"], horizontal=True, key="s4")
        s5 = st.radio("5. Can this tool be used without hiring additional staff?", ["Yes", "No", "Not sure"], horizontal=True, key="s5")

        screening_answers = [s1, s2, s3, s4, s5]
        st.session_state["tool_name"] = tool_name
        st.session_state["screening"] = screening_answers

        st.markdown("---")

        no_count = screening_answers.count("No")
        unsure_count = screening_answers.count("Not sure")

        if no_count >= 2:
            st.error("\U0001f6d1 STOP: Multiple deal-breakers detected. This tool may not be appropriate for your CHC. Proceed with extreme caution or consider alternatives.")
        elif no_count == 1:
            st.warning("\u26a0\ufe0f One deal-breaker flagged. You can proceed, but address this issue before making a final decision.")
        elif unsure_count >= 2:
            st.warning("\u26a0\ufe0f Multiple uncertainties. Gather more information from the vendor before proceeding.")
        else:
            st.success("\u2705 No deal-breakers found. Proceed to the 5-pillar evaluation.")

    # ===================== PILLAR 1: COST & VALUE =====================
    with p1:
        st.markdown("<h3 style='font-family:Playfair Display,serif; color:#0D2B45;'>Pillar 1: Cost & Value</h3>", unsafe_allow_html=True)
        st.markdown("<p style='font-family:Inter,sans-serif; color:#555;'>Estimate whether this tool will save or cost your CHC money. Enter your best estimates below.</p>", unsafe_allow_html=True)

        st.markdown("**Costs**")
        annual_cost = st.number_input("Annual subscription / licensing fee ($)", min_value=0, value=15000, step=500, key="c1")
        implementation_cost = st.number_input("One-time implementation / setup cost ($)", min_value=0, value=5000, step=500, key="c2")
        training_hours = st.number_input("Total staff training hours needed", min_value=0, value=20, step=1, key="c3")
        staff_wage = st.number_input("Average staff hourly wage ($)", min_value=0.0, value=25.0, step=0.5, key="c4")

        st.markdown("**Benefits**")
        hours_saved_week = st.number_input("Estimated staff hours saved per week", min_value=0.0, value=8.0, step=0.5, key="b1")
        noshow_reduction = st.slider("Expected no-show reduction (percentage points)", 0, 30, 5, key="b2")
        patients_year = st.number_input("Total patients per year", min_value=0, value=10000, step=500, key="b3")
        visit_value = st.number_input("Average revenue / value per completed visit ($)", min_value=0.0, value=85.0, step=5.0, key="b4")
        visit_rate = st.slider("Approximate visits per patient per year", 1, 10, 3, key="b5")

        st.markdown("---")

        # Calculations
        training_cost = training_hours * staff_wage
        total_annual_cost = annual_cost + (implementation_cost / 3) + training_cost  # amortize implementation over 3 years
        time_savings = hours_saved_week * staff_wage * 52
        noshow_value = (noshow_reduction / 100) * patients_year * visit_rate * visit_value
        total_annual_benefit = time_savings + noshow_value
        net_value = total_annual_benefit - total_annual_cost
        roi = (net_value / total_annual_cost * 100) if total_annual_cost > 0 else 0
        breakeven_months = (total_annual_cost / (total_annual_benefit / 12)) if total_annual_benefit > 0 else float('inf')

        # Store for results page
        if net_value > 5000:
            p1_score = 5
        elif net_value > 0:
            p1_score = 4
        elif net_value > -2000:
            p1_score = 3
        elif net_value > -5000:
            p1_score = 2
        else:
            p1_score = 1
        st.session_state["p1_score"] = p1_score

        # Display results
        st.markdown("<h4 style='font-family:Playfair Display,serif; color:#0D2B45;'>Results</h4>", unsafe_allow_html=True)

        r1, r2, r3 = st.columns(3)
        with r1:
            color = "#2A9D8F" if net_value >= 0 else "#E76F51"
            st.markdown(f"<div style='background:rgba(255,255,255,0.95); border-radius:12px; padding:20px; text-align:center; box-shadow:0 2px 10px rgba(0,0,0,0.06);'><div style='font-family:Inter,sans-serif; font-size:13px; color:#888;'>Net Annual Value</div><div style='font-family:Playfair Display,serif; font-size:28px; font-weight:700; color:{color};'>${net_value:,.0f}</div></div>", unsafe_allow_html=True)
        with r2:
            st.markdown(f"<div style='background:rgba(255,255,255,0.95); border-radius:12px; padding:20px; text-align:center; box-shadow:0 2px 10px rgba(0,0,0,0.06);'><div style='font-family:Inter,sans-serif; font-size:13px; color:#888;'>ROI</div><div style='font-family:Playfair Display,serif; font-size:28px; font-weight:700; color:#1B4D72;'>{roi:.0f}%</div></div>", unsafe_allow_html=True)
        with r3:
            be_text = f"{breakeven_months:.1f} months" if breakeven_months < 100 else "N/A"
            st.markdown(f"<div style='background:rgba(255,255,255,0.95); border-radius:12px; padding:20px; text-align:center; box-shadow:0 2px 10px rgba(0,0,0,0.06);'><div style='font-family:Inter,sans-serif; font-size:13px; color:#888;'>Break-even</div><div style='font-family:Playfair Display,serif; font-size:28px; font-weight:700; color:#1B4D72;'>{be_text}</div></div>", unsafe_allow_html=True)

        st.markdown("")
        if net_value > 5000:
            st.success("\U0001f4b0 Strong financial case. This tool is likely worth the investment.")
        elif net_value > 0:
            st.success("\u2705 Positive value, but the margin is small. Consider a pilot first.")
        elif net_value > -2000:
            st.warning("\u26a0\ufe0f Roughly break-even. Non-financial benefits (quality, equity) may tip the balance.")
        else:
            st.error("\u274c Negative financial value. This tool costs more than it saves. Strong non-financial justification needed.")

    # ===================== PILLAR 2: STAFF READINESS =====================
    with p2:
        st.markdown("<h3 style='font-family:Playfair Display,serif; color:#0D2B45;'>Pillar 2: Staff Readiness</h3>", unsafe_allow_html=True)
        st.markdown("<p style='font-family:Inter,sans-serif; color:#555;'>Assess whether your staff can realistically adopt this tool. Based on implementation science (CFIR framework).</p>", unsafe_allow_html=True)

        p2q1 = st.slider("1. How much training is required? (1 = Extensive retraining, 5 = Minimal/no training)", 1, 5, 3, key="p2q1")
        p2q2 = st.slider("2. Does this tool reduce or add to daily workflow burden? (1 = Adds significant burden, 5 = Significantly reduces burden)", 1, 5, 3, key="p2q2")
        p2q3 = st.slider("3. Have frontline staff been consulted about this tool? (1 = Not at all, 5 = Deeply involved in selection)", 1, 5, 3, key="p2q3")
        p2q4 = st.slider("4. Does the vendor provide onboarding and ongoing support? (1 = No support, 5 = Comprehensive support)", 1, 5, 3, key="p2q4")
        p2q5 = st.slider("5. Is your team currently experiencing burnout or turnover? (1 = Severe burnout, 5 = Stable and well-staffed)", 1, 5, 3, key="p2q5")

        p2_score = round((p2q1 + p2q2 + p2q3 + p2q4 + p2q5) / 5, 1)
        st.session_state["p2_score"] = p2_score

        st.markdown("---")
        if p2_score >= 4:
            st.success(f"\u2705 Staff Readiness Score: {p2_score}/5 \u2014 Your team is well-positioned to adopt this tool.")
        elif p2_score >= 3:
            st.warning(f"\u26a0\ufe0f Staff Readiness Score: {p2_score}/5 \u2014 Some concerns. Address training and workflow before committing.")
        else:
            st.error(f"\u274c Staff Readiness Score: {p2_score}/5 \u2014 High risk of adoption failure. Staff capacity is a major barrier.")

    # ===================== PILLAR 3: PATIENT TRUST & EQUITY =====================
    with p3:
        st.markdown("<h3 style='font-family:Playfair Display,serif; color:#0D2B45;'>Pillar 3: Patient Trust & Equity</h3>", unsafe_allow_html=True)
        st.markdown("<p style='font-family:Inter,sans-serif; color:#555;'>Evaluate whether this tool serves all your patients equitably. Based on the HEAL equity framework.</p>", unsafe_allow_html=True)

        p3q1 = st.slider("1. Does the tool support all primary languages of your patient population? (1 = English only, 5 = Full multilingual support)", 1, 5, 3, key="p3q1")
        p3q2 = st.slider("2. Is the tool accessible across digital literacy levels? (1 = Requires tech-savvy users, 5 = Designed for low digital literacy)", 1, 5, 3, key="p3q2")
        p3q3 = st.slider("3. Has the vendor provided evidence of equitable performance across racial/ethnic groups? (1 = No data, 5 = Published bias audit)", 1, 5, 3, key="p3q3")
        p3q4 = st.slider("4. Has your patient advisory board or community been consulted? (1 = Not at all, 5 = Actively involved)", 1, 5, 3, key="p3q4")
        p3q5 = st.slider("5. Does the tool work without a smartphone or reliable internet? (1 = Requires smartphone + WiFi, 5 = Works via SMS/phone/offline)", 1, 5, 3, key="p3q5")

        p3_score = round((p3q1 + p3q2 + p3q3 + p3q4 + p3q5) / 5, 1)
        st.session_state["p3_score"] = p3_score

        st.markdown("---")
        if p3_score >= 4:
            st.success(f"\u2705 Equity Score: {p3_score}/5 \u2014 This tool appears to serve your patient population equitably.")
        elif p3_score >= 3:
            st.warning(f"\u26a0\ufe0f Equity Score: {p3_score}/5 \u2014 Some gaps in equity. Request bias audit data from the vendor.")
        else:
            st.error(f"\u274c Equity Score: {p3_score}/5 \u2014 Significant equity concerns. This tool may exclude or harm vulnerable patients.")

    # ===================== PILLAR 4: PRIVACY & SECURITY =====================
    with p4:
        st.markdown("<h3 style='font-family:Playfair Display,serif; color:#0D2B45;'>Pillar 4: Privacy & Security</h3>", unsafe_allow_html=True)
        st.markdown("<p style='font-family:Inter,sans-serif; color:#555;'>Assess data protection and compliance. Mapped to Privacy by Design principles and HIPAA requirements.</p>", unsafe_allow_html=True)

        p4q1 = st.slider("1. Is a signed HIPAA Business Associate Agreement in place? (1 = No, 5 = Yes, fully executed)", 1, 5, 3, key="p4q1")
        p4q2 = st.slider("2. Where is patient data stored? (1 = Unknown/overseas, 5 = US-based, encrypted, documented)", 1, 5, 3, key="p4q2")
        p4q3 = st.slider("3. Can the CHC delete patient data on request? (1 = No/unclear, 5 = Yes, with documented process)", 1, 5, 3, key="p4q3")
        p4q4 = st.slider("4. Does the vendor use patient data to train AI models? (1 = Yes without consent, 5 = No, or only with explicit consent)", 1, 5, 3, key="p4q4")
        p4q5 = st.slider("5. Has the vendor had any reported data breaches? (1 = Yes, multiple, 5 = None, with security audit available)", 1, 5, 3, key="p4q5")

        p4_score = round((p4q1 + p4q2 + p4q3 + p4q4 + p4q5) / 5, 1)
        st.session_state["p4_score"] = p4_score

        st.markdown("---")
        if p4_score >= 4:
            st.success(f"\u2705 Privacy Score: {p4_score}/5 \u2014 Strong privacy and security posture.")
        elif p4_score >= 3:
            st.warning(f"\u26a0\ufe0f Privacy Score: {p4_score}/5 \u2014 Some gaps. Clarify data practices with the vendor before proceeding.")
        else:
            st.error(f"\u274c Privacy Score: {p4_score}/5 \u2014 Serious privacy concerns. Do not proceed without resolving these issues.")

    # ===================== PILLAR 5: SUSTAINABILITY =====================
    with p5:
        st.markdown("<h3 style='font-family:Playfair Display,serif; color:#0D2B45;'>Pillar 5: Sustainability</h3>", unsafe_allow_html=True)
        st.markdown("<p style='font-family:Inter,sans-serif; color:#555;'>Can your CHC maintain this tool long-term? Based on the NASSS framework for digital health sustainability.</p>", unsafe_allow_html=True)

        p5q1 = st.slider("1. Is this funded from operating budget or a time-limited grant? (1 = Grant-only, 5 = Sustainable operating budget)", 1, 5, 3, key="p5q1")
        p5q2 = st.slider("2. What happens if the vendor goes out of business? (1 = Total data loss, 5 = Full data export + alternatives available)", 1, 5, 3, key="p5q2")
        p5q3 = st.slider("3. Does the contract lock you in? (1 = Multi-year, no exit, 5 = Month-to-month or easy cancellation)", 1, 5, 3, key="p5q3")
        p5q4 = st.slider("4. Can the tool scale if your CHC grows? (1 = No, fixed capacity, 5 = Easily scalable)", 1, 5, 3, key="p5q4")
        p5q5 = st.slider("5. Does the vendor have a track record of updates and long-term support? (1 = No track record, 5 = Proven multi-year support history)", 1, 5, 3, key="p5q5")

        p5_score = round((p5q1 + p5q2 + p5q3 + p5q4 + p5q5) / 5, 1)
        st.session_state["p5_score"] = p5_score

        st.markdown("---")
        if p5_score >= 4:
            st.success(f"\u2705 Sustainability Score: {p5_score}/5 \u2014 This tool looks sustainable for long-term use.")
        elif p5_score >= 3:
            st.warning(f"\u26a0\ufe0f Sustainability Score: {p5_score}/5 \u2014 Some risks. Plan an exit strategy before committing.")
        else:
            st.error(f"\u274c Sustainability Score: {p5_score}/5 \u2014 High risk of abandonment. Consider alternatives with better long-term viability.")


elif page == "Results":

    if logo_data:
        st.markdown(f'<div style="text-align:center; margin-bottom:10px;"><img src="data:image/png;base64,{logo_data}" width="80"></div>', unsafe_allow_html=True)

    st.markdown('<div class="section-title">Results Dashboard</div>', unsafe_allow_html=True)

    tool_name = st.session_state.get("tool_name", "the tool")
    p1 = st.session_state.get("p1_score", 3)
    p2 = st.session_state.get("p2_score", 3)
    p3 = st.session_state.get("p3_score", 3)
    p4 = st.session_state.get("p4_score", 3)
    p5 = st.session_state.get("p5_score", 3)

    # Weighted overall score (out of 100)
    weights = {"Cost & Value": 0.25, "Staff Readiness": 0.20, "Patient Trust & Equity": 0.25, "Privacy & Security": 0.15, "Sustainability": 0.15}
    scores = {"Cost & Value": p1, "Staff Readiness": p2, "Patient Trust & Equity": p3, "Privacy & Security": p4, "Sustainability": p5}
    overall = sum(scores[k] * weights[k] for k in weights) / 5 * 100

    # Traffic light
    if overall >= 70:
        light = "\U0001f7e2"
        recommendation = "ADOPT"
        rec_color = "#2A9D8F"
        rec_text = f"Based on the evaluation, <strong>{tool_name}</strong> scores well across the five pillars. Consider moving forward with adoption or a full-scale pilot."
    elif overall >= 45:
        light = "\U0001f7e1"
        recommendation = "PILOT WITH CONDITIONS"
        rec_color = "#E9C46A"
        rec_text = f"<strong>{tool_name}</strong> shows promise but has gaps. Address the flagged issues and run a time-limited pilot before committing."
    else:
        light = "\U0001f534"
        recommendation = "DO NOT ADOPT"
        rec_color = "#E76F51"
        rec_text = f"<strong>{tool_name}</strong> has significant weaknesses. The risks outweigh the benefits at this time. Consider alternatives."

    # Overall Score Display
    st.markdown(f"""
    <div style="background:rgba(255,255,255,0.95); border-radius:16px; padding:30px; text-align:center; box-shadow:0 4px 20px rgba(13,43,69,0.08); margin-bottom:24px;">
        <div style="font-size:48px; margin-bottom:8px;">{light}</div>
        <div style="font-family:'Playfair Display',serif; font-size:36px; font-weight:700; color:{rec_color};">{recommendation}</div>
        <div style="font-family:'Inter',sans-serif; font-size:40px; font-weight:700; color:#0D2B45; margin:10px 0;">{overall:.0f}/100</div>
        <div style="font-family:'Inter',sans-serif; font-size:15px; color:#555; max-width:500px; margin:0 auto; line-height:1.6;">{rec_text}</div>
    </div>
    """, unsafe_allow_html=True)

    # Radar Chart
    import plotly.graph_objects as go

    categories = list(scores.keys())
    values = list(scores.values())
    values.append(values[0])  # close the polygon
    categories.append(categories[0])

    fig = go.Figure(data=go.Scatterpolar(
        r=values,
        theta=categories,
        fill='toself',
        fillcolor='rgba(42, 157, 143, 0.25)',
        line=dict(color='#1B4D72', width=2),
        marker=dict(size=8, color='#2A9D8F')
    ))

    fig.update_layout(
        polar=dict(
            radialaxis=dict(visible=True, range=[0, 5], tickfont=dict(size=11)),
            angularaxis=dict(tickfont=dict(size=12, family="Inter"))
        ),
        showlegend=False,
        margin=dict(l=60, r=60, t=40, b=40),
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        height=420
    )

    st.plotly_chart(fig, use_container_width=True)

    # Pillar Breakdown
    st.markdown("<h4 style='font-family:Playfair Display,serif; color:#0D2B45; text-align:center;'>Pillar Breakdown</h4>", unsafe_allow_html=True)

    pillar_info = [
        ("\U0001f4b0", "Cost & Value", p1, 0.25),
        ("\U0001f469\u200d\u2695\ufe0f", "Staff Readiness", p2, 0.20),
        ("\U0001f91d", "Patient Trust & Equity", p3, 0.25),
        ("\U0001f512", "Privacy & Security", p4, 0.15),
        ("\U0001f504", "Sustainability", p5, 0.15),
    ]

    for icon, name, score, weight in pillar_info:
        if score >= 4:
            bar_color = "#2A9D8F"
            status = "Strong"
        elif score >= 3:
            bar_color = "#E9C46A"
            status = "Moderate"
        else:
            bar_color = "#E76F51"
            status = "Weak"

        pct = score / 5 * 100
        st.markdown(f"""
        <div style="background:rgba(255,255,255,0.95); border-radius:12px; padding:16px 20px; margin-bottom:10px; box-shadow:0 2px 10px rgba(0,0,0,0.04);">
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px;">
                <span style="font-family:'Inter',sans-serif; font-size:15px; font-weight:500; color:#0D2B45;">{icon} {name} <span style="color:#888; font-weight:400;">(Weight: {int(weight*100)}%)</span></span>
                <span style="font-family:'Inter',sans-serif; font-size:14px; font-weight:600; color:{bar_color};">{score}/5 - {status}</span>
            </div>
            <div style="background:#E8F0F2; border-radius:6px; height:10px; overflow:hidden;">
                <div style="background:{bar_color}; width:{pct}%; height:100%; border-radius:6px;"></div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    # Action Items
    st.markdown("")
    st.markdown("<h4 style='font-family:Playfair Display,serif; color:#0D2B45; text-align:center;'>Recommended Next Steps</h4>", unsafe_allow_html=True)

    actions = []
    if p1 < 3:
        actions.append("\u2022 Re-evaluate the financial case. Request detailed cost breakdowns from the vendor.")
    if p2 < 3:
        actions.append("\u2022 Consult frontline staff before proceeding. Assess training needs and workflow impact.")
    if p3 < 3:
        actions.append("\u2022 Request a bias/fairness audit from the vendor. Verify language and accessibility support.")
    if p4 < 3:
        actions.append("\u2022 Do NOT proceed until HIPAA compliance and data practices are fully documented.")
    if p5 < 3:
        actions.append("\u2022 Develop an exit strategy. Ensure data portability and avoid vendor lock-in.")
    if not actions:
        actions.append("\u2022 All pillars are in good shape. Proceed to a pilot phase and re-evaluate after 3 months.")

    actions_html = "<br>".join(actions)
    st.markdown(f"""
    <div style="background:rgba(255,255,255,0.95); border-radius:14px; padding:24px; box-shadow:0 2px 12px rgba(13,43,69,0.06); border-left:4px solid #1B4D72;">
        <p style="font-family:'Inter',sans-serif; font-size:15px; color:#444; line-height:1.8;">{actions_html}</p>
    </div>
    """, unsafe_allow_html=True)

elif page == "Resources":

    if logo_data:
        st.markdown(f'<div style="text-align:center; margin-bottom:10px;"><img src="data:image/png;base64,{logo_data}" width="80"></div>', unsafe_allow_html=True)

    st.markdown('<div class="section-title">Resources & References</div>', unsafe_allow_html=True)

    # Evidence by Pillar
    st.markdown("""
    <div style="background:rgba(255,255,255,0.95); border-radius:14px; padding:28px; margin-bottom:20px; box-shadow:0 2px 12px rgba(13,43,69,0.06); border-left:4px solid #2A9D8F;">
        <h3 style="font-family:'Playfair Display',serif; color:#0D2B45; margin-top:0;">Pillar 1: Cost & Value</h3>
        <p style="font-family:'Inter',sans-serif; font-size:14px; color:#444; line-height:1.8;">
            \u2022 Gentili et al. (2022). Systematic review on cost-effectiveness of digital health interventions. <em>PharmacoEconomics.</em><br>
            \u2022 Tuffaha et al. Value of Information analysis for health technology adoption decisions.<br>
            \u2022 Lewkowicz et al. (2023). Monte Carlo simulation for economic evaluation of digital therapeutics.<br>
            \u2022 ICER \u2013 Peterson Health Technology Institute. Digital health value assessment framework.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div style="background:rgba(255,255,255,0.95); border-radius:14px; padding:28px; margin-bottom:20px; box-shadow:0 2px 12px rgba(13,43,69,0.06); border-left:4px solid #1B4D72;">
        <h3 style="font-family:'Playfair Display',serif; color:#0D2B45; margin-top:0;">Pillar 2: Staff Readiness</h3>
        <p style="font-family:'Inter',sans-serif; font-size:14px; color:#444; line-height:1.8;">
            \u2022 Damschroder et al. (2009). Consolidated Framework for Implementation Research (CFIR). <em>Implementation Science.</em><br>
            \u2022 Granja et al. (2018). Factors determining success and failure of eHealth interventions. <em>Journal of Medical Internet Research.</em><br>
            \u2022 Collier (2017). Electronic health records contributing to physician burnout. <em>CMAJ.</em><br>
            \u2022 Muhiyaddin et al. (2022). EHR and physician burnout: a scoping review.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div style="background:rgba(255,255,255,0.95); border-radius:14px; padding:28px; margin-bottom:20px; box-shadow:0 2px 12px rgba(13,43,69,0.06); border-left:4px solid #E76F51;">
        <h3 style="font-family:'Playfair Display',serif; color:#0D2B45; margin-top:0;">Pillar 3: Patient Trust & Equity</h3>
        <p style="font-family:'Inter',sans-serif; font-size:14px; color:#444; line-height:1.8;">
            \u2022 Obermeyer et al. (2019). Dissecting racial bias in an algorithm used to manage the health of populations. <em>Science.</em><br>
            \u2022 HEAL Framework (2024). Performance equity assessment for clinical AI. <em>eClinicalMedicine.</em><br>
            \u2022 McCradden et al. (2020). Ethical limitations of algorithmic fairness solutions in health care. <em>The Lancet Digital Health.</em><br>
            \u2022 Aequitas \u2013 Open-source bias and fairness audit toolkit.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div style="background:rgba(255,255,255,0.95); border-radius:14px; padding:28px; margin-bottom:20px; box-shadow:0 2px 12px rgba(13,43,69,0.06); border-left:4px solid #264653;">
        <h3 style="font-family:'Playfair Display',serif; color:#0D2B45; margin-top:0;">Pillar 4: Privacy & Security</h3>
        <p style="font-family:'Inter',sans-serif; font-size:14px; color:#444; line-height:1.8;">
            \u2022 Cavoukian, A. Privacy by Design: The 7 Foundational Principles.<br>
            \u2022 U.S. Department of Health & Human Services. HIPAA Privacy Rule and Business Associate Agreements.<br>
            \u2022 Office of the National Coordinator for Health IT. Guide to Privacy and Security of Electronic Health Information.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div style="background:rgba(255,255,255,0.95); border-radius:14px; padding:28px; margin-bottom:20px; box-shadow:0 2px 12px rgba(13,43,69,0.06); border-left:4px solid #E9C46A;">
        <h3 style="font-family:'Playfair Display',serif; color:#0D2B45; margin-top:0;">Pillar 5: Sustainability</h3>
        <p style="font-family:'Inter',sans-serif; font-size:14px; color:#444; line-height:1.8;">
            \u2022 Greenhalgh et al. (2017). NASSS Framework: Non-adoption, Abandonment, Scale-up, Spread, and Sustainability. <em>Journal of Medical Internet Research.</em><br>
            \u2022 Keogh et al. (2024). Breaking down the Digital Fortress: Unseen challenges in healthcare technology. <em>Sensors.</em><br>
            \u2022 Dendere et al. (2021). Evaluating current approaches for implementation of digital health systems. <em>Australian Health Review.</em>
        </p>
    </div>
    """, unsafe_allow_html=True)

    # The Problem - Key Stats
    st.markdown("""
    <div style="background:rgba(255,255,255,0.95); border-radius:14px; padding:28px; margin-bottom:20px; box-shadow:0 2px 12px rgba(13,43,69,0.06); border-left:4px solid #2A9D8F;">
        <h3 style="font-family:'Playfair Display',serif; color:#0D2B45; margin-top:0;">Key Statistics</h3>
        <p style="font-family:'Inter',sans-serif; font-size:14px; color:#444; line-height:1.8;">
            \u2022 ~46.5% of digital health implementations report failure (Granja et al., 2018)<br>
            \u2022 EHR implementation estimated at $168 billion nationwide (Essin, 2011)<br>
            \u2022 74.5% of burned-out physicians identified EHR as a contributor (Tajirian et al., 2020)<br>
            \u2022 1,500+ CHC organizations, 17,000+ sites, serving 30+ million patients (NACHC)<br>
            \u2022 Over 70% of CHCs report workforce shortages (Commonwealth Fund, 2024)
        </p>
    </div>
    """, unsafe_allow_html=True)

    # About the Team
    st.markdown("""
    <div style="background:rgba(255,255,255,0.95); border-radius:14px; padding:28px; margin-bottom:20px; box-shadow:0 2px 12px rgba(13,43,69,0.06); border-left:4px solid #1B4D72;">
        <h3 style="font-family:'Playfair Display',serif; color:#0D2B45; margin-top:0;">About the Team</h3>
        <p style="font-family:'Inter',sans-serif; font-size:14px; color:#444; line-height:1.8;">
            DECIDE was built for the Hack the Health Gap Hackathon 2026.<br><br>
            <strong>Team Members:</strong><br>
            \u2022 [Your Name]<br>
            \u2022 [Team Member 2]<br>
            \u2022 [Team Member 3]<br>
            \u2022 [Team Member 4]<br><br>
            <strong>Contact:</strong> [your email]
        </p>
    </div>
    """, unsafe_allow_html=True)