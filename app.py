import streamlit as st
import base64
import os
from streamlit_option_menu import option_menu
from advanced_analysis import render_advanced_analysis
from design import inject_global_css, get_logo_svg
from learning_game import render_learning_game

st.set_page_config(
    page_title="DECIDE",
    page_icon="\U0001f3e5",
    layout="wide",
    initial_sidebar_state="collapsed"
)

def load_image_base64(filename):
    filepath = os.path.join(os.path.dirname(os.path.abspath(__file__)), filename)
    if os.path.exists(filepath):
        with open(filepath, "rb") as f:
            return base64.b64encode(f.read()).decode()
    return None

logo_data = load_image_base64("logo.png")

if "show_login" not in st.session_state:
    st.session_state["show_login"] = False
if "show_signup" not in st.session_state:
    st.session_state["show_signup"] = False

inject_global_css()

head_left, head_center, head_right = st.columns([3, 4, 3])

with head_left:
    st.markdown("""
    <div style="padding: 5px 10px;">
        <div style="font-family: 'Times New Roman', serif; font-size: 26px; font-weight: bold; color: #3E2723;">DECIDE</div>
        <div style="font-family: 'Times New Roman', serif; font-size: 11px; color: #6D4C41; text-decoration: underline;">Digital Evaluation for Community Implementation Decisions</div>
    </div>
    """, unsafe_allow_html=True)

with head_right:
    r1, r2, r3 = st.columns([2, 1, 1])
    with r2:
        if st.button("Login", key="login_btn"):
            st.session_state["show_login"] = not st.session_state["show_login"]
            st.session_state["show_signup"] = False
            st.rerun()
    with r3:
        if st.button("Sign Up", key="signup_btn"):
            st.session_state["show_signup"] = not st.session_state["show_signup"]
            st.session_state["show_login"] = False
            st.rerun()

page = option_menu(
    menu_title=None,
    options=["Home", "About Us", "Solutions", "Security & HIPAA", "Blogs", "Contact Us", "Evaluate Tool", "Advanced Analysis", "Learn", "Results"],
    icons=["house", "info-circle", "lightbulb", "shield-lock", "journal-text", "envelope", "clipboard-check", "calculator", "controller", "bar-chart"],
    default_index=0,
    orientation="horizontal",
    styles={
        "container": {
            "padding": "0px",
            "background-color": "#C4A882",
            "border-radius": "0px",
            "margin": "0px",
        },
        "icon": {
            "color": "#3E2723",
            "font-size": "14px",
        },
        "nav-link": {
            "font-family": "'Times New Roman', serif",
            "font-size": "14px",
            "color": "#3E2723",
            "text-align": "center",
            "padding": "10px 14px",
            "border-radius": "0px",
            "margin": "0px",
        },
        "nav-link-selected": {
            "background-color": "#A68B6B",
            "color": "#FFFFFF",
            "font-weight": "bold",
        },
    }
)

if st.session_state["show_login"]:
    st.markdown("---")
    col_l, col_form, col_r = st.columns([1, 2, 1])
    with col_form:
        st.markdown("<h3 style='font-family:Times New Roman,serif; text-align:center;'>Login</h3>", unsafe_allow_html=True)
        st.text_input("Email", key="login_email")
        st.text_input("Password", type="password", key="login_pass")
        if st.button("Log In", key="do_login", use_container_width=True):
            st.success("Login successful! (Demo mode)")
            st.session_state["show_login"] = False
        st.markdown("<p style='font-family:Times New Roman,serif; font-size:12px; text-align:center; text-decoration:underline;'>Don't have an account? Click Sign Up above</p>", unsafe_allow_html=True)

elif st.session_state["show_signup"]:
    st.markdown("---")
    col_l, col_form, col_r = st.columns([1, 2, 1])
    with col_form:
        st.markdown("<h3 style='font-family:Times New Roman,serif; text-align:center;'>Create Account</h3>", unsafe_allow_html=True)
        st.text_input("Full Name", key="signup_name")
        st.text_input("Email", key="signup_email")
        st.text_input("Password", type="password", key="signup_pass")
        st.text_input("Organization / CHC Name", key="signup_org")
        if st.button("Create Account", key="do_signup", use_container_width=True):
            st.success("Account created! (Demo mode)")
            st.session_state["show_signup"] = False
        st.markdown("<p style='font-family:Times New Roman,serif; font-size:12px; text-align:center; text-decoration:underline;'>Already have an account? Click Login above</p>", unsafe_allow_html=True)

if not st.session_state["show_login"] and not st.session_state["show_signup"]:

    if page == "Home":

        # SVG Logo
        logo_svg = get_logo_svg(140)
        st.markdown(f'<div style="text-align:center; margin-top:40px; animation: fadeInUp 0.6s ease-out;">{logo_svg}</div>', unsafe_allow_html=True)

        # Main heading
        st.markdown("""
        <div style="animation: fadeInUp 0.8s ease-out;">
            <div class="heading-xl" style="margin-top:24px;">DECIDE</div>
            <div style="font-family:'Times New Roman',serif; font-size:13px; color:#6D4C41; text-align:center; letter-spacing:3px; margin-top:4px;">DIGITAL EVALUATION FOR COMMUNITY IMPLEMENTATION DECISIONS</div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown('<div class="gold-divider" style="margin-top:24px;"></div>', unsafe_allow_html=True)

        # Hero text
        st.markdown("""
        <div class="glass-card" style="max-width:800px; margin:0 auto; animation: fadeInUp 0.9s ease-out;">
            <div class="body-text" style="font-size:20px; color:#333; line-height:1.8;">
                Making healthcare innovation practical, not overwhelming.
                Our platform guides healthcare organizations in navigating complex
                technology choices with clarity, helping them adopt solutions
                that truly make a difference.
            </div>
        </div>
        """, unsafe_allow_html=True)

        # Stats row
        st.markdown("")
        s1, s2, s3, s4 = st.columns(4)
        with s1:
            st.markdown('<div class="stat-card"><div class="stat-number">5</div><div class="stat-label">Evaluation Pillars</div></div>', unsafe_allow_html=True)
        with s2:
            st.markdown('<div class="stat-card"><div class="stat-number">1,000</div><div class="stat-label">Monte Carlo Iterations</div></div>', unsafe_allow_html=True)
        with s3:
            st.markdown('<div class="stat-card"><div class="stat-number">15 min</div><div class="stat-label">Time to Evaluate</div></div>', unsafe_allow_html=True)
        with s4:
            st.markdown('<div class="stat-card"><div class="stat-number">PDF</div><div class="stat-label">Downloadable Report</div></div>', unsafe_allow_html=True)

        # Tagline section
        st.markdown("")
        st.markdown("""
        <div class="glass-card" style="max-width:800px; margin:20px auto 0 auto; text-align:center; animation: fadeInUp 1.1s ease-out;">
            <div class="heading-md">Simple inputs, reliable decisions</div>
            <div class="body-text">
                DECIDE reimagines how digital health tools are evaluated\u2014making
                the process fast, intuitive, and accessible. By using a small set
                of meaningful inputs, it transforms everyday operational data into
                clear, actionable insights. No complex models or technical expertise
                needed\u2014just straightforward outputs you can trust.
            </div>
            <div class="pillar-row" style="margin-top:24px;">
                <span class="pillar-chip">\U0001f4b0 Cost & Value</span>
                <span class="pillar-chip">\U0001f469\u200d\u2695\ufe0f Staff Readiness</span>
                <span class="pillar-chip">\U0001f91d Patient Trust & Equity</span>
                <span class="pillar-chip">\U0001f512 Privacy & Security</span>
                <span class="pillar-chip">\U0001f504 Sustainability</span>
            </div>
        </div>
        """, unsafe_allow_html=True)

        # How it works
        st.markdown("")
        st.markdown('<div class="heading-lg" style="margin-top:30px;">How It Works</div>', unsafe_allow_html=True)
        st.markdown('<div class="gold-divider"></div>', unsafe_allow_html=True)

        h1, h2, h3 = st.columns(3)
        with h1:
            st.markdown("""
            <div class="glass-card" style="text-align:center; min-height:200px; animation: fadeInLeft 1s ease-out;">
                <div class="float-icon">\U0001f4cb</div>
                <div class="heading-md">1. Screen</div>
                <div class="body-text">5 deal-breaker questions catch obvious non-starters in under 2 minutes.</div>
            </div>
            """, unsafe_allow_html=True)
        with h2:
            st.markdown("""
            <div class="glass-card" style="text-align:center; min-height:200px; animation: fadeInUp 1.1s ease-out;">
                <div class="float-icon">\U0001f50d</div>
                <div class="heading-md">2. Evaluate</div>
                <div class="body-text">Score across 5 evidence-based pillars with built-in confidence adjustments.</div>
            </div>
            """, unsafe_allow_html=True)
        with h3:
            st.markdown("""
            <div class="glass-card" style="text-align:center; min-height:200px; animation: fadeInRight 1.2s ease-out;">
                <div class="float-icon">\U0001f4ca</div>
                <div class="heading-md">3. Decide</div>
                <div class="body-text">Get a clear Adopt / Pilot / Reject recommendation with a downloadable PDF report.</div>
            </div>
            """, unsafe_allow_html=True)

        # Footer
        st.markdown("""
        <div style="text-align:center; margin-top:50px; padding:20px; animation: fadeInUp 1.3s ease-out;">
            <div style="font-family:'Times New Roman',serif; font-size:18px; font-style:italic; color:#6D4C41;">\u201cBefore you adopt, evaluate.\u201d</div>
            <div style="font-family:'Times New Roman',serif; font-size:12px; color:#aaa; margin-top:12px;">Built for the Hack the Health Gap Hackathon 2026</div>
        </div>
        """, unsafe_allow_html=True)

    elif page == "About Us":

        st.markdown('<div class="heading-lg" style="margin-top:40px;">About Us</div>', unsafe_allow_html=True)
        st.markdown('<div class="gold-divider"></div>', unsafe_allow_html=True)

        # Introduction
        st.markdown(f"""
        <div class="glass-card" style="border-left: 5px solid #C4A882; animation: fadeInUp 0.9s ease-out;">
            <div class="float-icon">\U0001f3e5</div>
            <div class="heading-md">Introduction</div>
            <div class="body-text">
                Community Health Centers (CHCs) are increasingly presented with a wide range of digital health solutions
                promising to improve care delivery, efficiency, and patient outcomes. However, selecting the right tools
                is often challenging due to limited resources, uncertainty in vendor claims, and the need to balance
                financial, operational, and ethical considerations.
            </div>
            <br>
            <div class="body-text">
                DECIDE (Digital Evaluation for Community Implementation Decision) is designed to address this challenge.
                It provides a structured, evidence-informed framework that enables CHC leaders to systematically evaluate
                digital health technologies across key domains.
            </div>
            <br>
            <div class="body-text">
                By translating complex information into clear, actionable insights, DECIDE supports more consistent,
                transparent, and informed decision-making\u2014helping health centers adopt solutions that truly meet
                the needs of their patients and communities.
            </div>
            <div class="pillar-row">
                <span class="pillar-chip">\U0001f4b0 Cost & Value</span>
                <span class="pillar-chip">\U0001f469\u200d\u2695\ufe0f Staff Readiness</span>
                <span class="pillar-chip">\U0001f91d Patient Trust & Equity</span>
                <span class="pillar-chip">\U0001f512 Privacy & Security</span>
                <span class="pillar-chip">\U0001f504 Sustainability</span>
            </div>
        </div>
        """, unsafe_allow_html=True)

        col_m, col_g = st.columns(2)
        with col_m:
            st.markdown("""
            <div class="glass-card" style="border-left: 5px solid #6D4C41; min-height:280px; animation: fadeInLeft 1s ease-out;">
                <div class="float-icon">\U0001f3af</div>
                <div class="heading-md">Our Mission</div>
                <div class="quote-mark">\u201c</div>
                <div style="font-family:'Times New Roman',serif; font-size:17px; color:#3E2723; text-align:center; font-style:italic; padding:10px 20px; line-height:1.8;">
                    Our mission is to make digital health adoption smarter, fairer, and more accountable
                    for community health centers through clear, evidence-driven decision support.
                </div>
                <div class="quote-mark">\u201d</div>
            </div>
            """, unsafe_allow_html=True)
        with col_g:
            st.markdown("""
            <div class="glass-card" style="border-left: 5px solid #3E2723; min-height:280px; animation: fadeInRight 1.1s ease-out;">
                <div class="float-icon">\U0001f4c8</div>
                <div class="heading-md">Our Goal</div>
                <div class="quote-mark">\u201c</div>
                <div style="font-family:'Times New Roman',serif; font-size:17px; color:#3E2723; text-align:center; font-style:italic; padding:10px 20px; line-height:1.8;">
                    To increase the adoption of effective and equitable digital health solutions in community
                    health centers while minimizing the risk of implementing low-value or unsuitable technologies.
                </div>
                <div class="quote-mark">\u201d</div>
            </div>
            """, unsafe_allow_html=True)

    elif page == "Solutions":

        st.markdown("""
        <style>
            @keyframes fadeInUp {
                from { opacity: 0; transform: translateY(30px); }
                to { opacity: 1; transform: translateY(0); }
            }
            @keyframes fadeInScale {
                from { opacity: 0; transform: scale(0.92); }
                to { opacity: 1; transform: scale(1); }
            }
            .sol-header {
                font-family: 'Times New Roman', serif;
                font-size: 36px;
                font-weight: bold;
                text-align: center;
                color: #3E2723;
                margin-top: 40px;
                margin-bottom: 10px;
                animation: fadeInUp 0.8s ease-out;
            }
            .sol-divider {
                width: 80px;
                height: 3px;
                background: linear-gradient(90deg, #C4A882, #6D4C41);
                margin: 0 auto 40px auto;
                border-radius: 2px;
            }
            .sol-card {
                background: rgba(255,255,255,0.96);
                border-radius: 16px;
                padding: 28px 32px;
                margin-bottom: 20px;
                box-shadow: 0 4px 18px rgba(62,39,35,0.07);
                border: 1px solid #E8E0D8;
                border-left: 5px solid #C4A882;
                animation: fadeInScale 0.8s ease-out;
            }
            .sol-card-num {
                font-family: 'Times New Roman', serif;
                font-size: 28px;
                font-weight: bold;
                color: #C4A882;
                margin-bottom: 4px;
            }
            .sol-card-title {
                font-family: 'Times New Roman', serif;
                font-size: 20px;
                font-weight: bold;
                color: #3E2723;
                text-decoration: underline;
                margin-bottom: 10px;
            }
            .sol-card-text {
                font-family: 'Times New Roman', serif;
                font-size: 15px;
                color: #444;
                line-height: 1.8;
            }
            .sol-card-list {
                font-family: 'Times New Roman', serif;
                font-size: 14px;
                color: #555;
                line-height: 1.8;
                padding-left: 20px;
            }
            .decision-box {
                background: #FBF7F2;
                border-radius: 14px;
                padding: 28px 32px;
                margin-top: 30px;
                margin-bottom: 20px;
                box-shadow: 0 4px 18px rgba(62,39,35,0.07);
                border: 2px solid #C4A882;
                animation: fadeInUp 1s ease-out;
            }
            .decision-title {
                font-family: 'Times New Roman', serif;
                font-size: 22px;
                font-weight: bold;
                color: #3E2723;
                text-align: center;
                text-decoration: underline;
                margin-bottom: 16px;
            }
            .decision-rule {
                font-family: 'Times New Roman', serif;
                font-size: 16px;
                color: #333;
                line-height: 2;
                text-align: center;
            }
        </style>
        """, unsafe_allow_html=True)

        st.markdown('<div class="sol-header">Our Solutions</div>', unsafe_allow_html=True)
        st.markdown('<div class="sol-divider"></div>', unsafe_allow_html=True)

        solutions = [
            ("01", "Structured Decision-Making Framework",
             "Provides a clear, step-by-step approach to evaluate digital health tools across key domains, reducing guesswork and inconsistency in decision-making.", None),
            ("02", "Evidence-Based Evaluation",
             "Incorporates data, research, and confidence adjustments to critically assess vendor claims and avoid overestimation of benefits.", None),
            ("03", "Multi-Dimensional Assessment",
             "Evaluates tools beyond cost by considering:",
             ["Staff readiness", "Patient trust and equity", "Privacy and security", "Long-term sustainability"]),
            ("04", "Simplification of Complex Information",
             "Transforms complex financial and operational data into clear, understandable insights for non-technical decision-makers.", None),
            ("05", "Risk Reduction in Adoption",
             "Helps identify low-value or unsuitable technologies before implementation, minimizing wasted resources and failed deployments.", None),
            ("06", "Transparency and Accountability",
             "Creates a transparent evaluation process that can be shared with leadership, stakeholders, and funders.", None),
            ("07", "Scenario and Uncertainty Handling",
             "Accounts for uncertainty in outcomes through confidence adjustments and scenario-based thinking.", None),
        ]

        for num, title, text, bullet_list in solutions:
            list_html = ""
            if bullet_list:
                items = "".join([f"<li>{item}</li>" for item in bullet_list])
                list_html = f'<ul class="sol-card-list">{items}</ul>'
            st.markdown(f"""
            <div class="sol-card">
                <div class="sol-card-num">{num}</div>
                <div class="sol-card-title">{title}</div>
                <div class="sol-card-text">{text}</div>
                {list_html}
            </div>
            """, unsafe_allow_html=True)

        st.markdown("""
        <div class="decision-box">
            <div class="decision-title">\u201cSo\u2026 should we adopt this or not?\u201d</div>
            <div class="decision-rule">
                \u2705 <strong>Adopt</strong> \u2192 ROI > 20% AND break-even < 12 months<br>
                \u26a0\ufe0f <strong>Pilot</strong> \u2192 ROI positive but uncertainty is high<br>
                \u274c <strong>Do not adopt</strong> \u2192 Negative net value<br><br>
                <em>This simple, transparent rule replaces complex health economic models (CEAC, CEAF, decision thresholds) with clear, actionable guidance that any CHC leader can understand and trust.</em>
            </div>
        </div>
        """, unsafe_allow_html=True)

    elif page == "Security & HIPAA":

        st.markdown("""
        <style>
            .sec-header {
                font-family: 'Times New Roman', serif;
                font-size: 36px;
                font-weight: bold;
                text-align: center;
                color: #3E2723;
                margin-top: 40px;
                margin-bottom: 10px;
            }
            .sec-divider {
                width: 80px;
                height: 3px;
                background: linear-gradient(90deg, #C4A882, #6D4C41);
                margin: 0 auto 40px auto;
                border-radius: 2px;
            }
            .sec-card {
                background: rgba(255,255,255,0.96);
                border-radius: 16px;
                padding: 28px 32px;
                margin-bottom: 20px;
                box-shadow: 0 4px 18px rgba(62,39,35,0.07);
                border: 1px solid #E8E0D8;
                border-left: 5px solid #6D4C41;
            }
            .sec-card-title {
                font-family: 'Times New Roman', serif;
                font-size: 20px;
                font-weight: bold;
                color: #3E2723;
                text-decoration: underline;
                text-align: center;
                margin-bottom: 12px;
            }
            .sec-card-text {
                font-family: 'Times New Roman', serif;
                font-size: 15px;
                color: #444;
                line-height: 1.8;
                text-align: center;
            }
        </style>
        """, unsafe_allow_html=True)

        st.markdown('<div class="sec-header">Security & HIPAA Compliance</div>', unsafe_allow_html=True)
        st.markdown('<div class="sec-divider"></div>', unsafe_allow_html=True)

        security_sections = [
            ("\U0001f512", "HIPAA Compliance",
             "DECIDE is designed with HIPAA (Health Insurance Portability and Accountability Act) compliance at its core. The tool does not collect, store, or transmit any Protected Health Information (PHI). All evaluation data entered by users relates to operational metrics and vendor assessments \u2014 not individual patient records."),
            ("\U0001f6e1\ufe0f", "Data Privacy",
             "No patient data is ever entered into DECIDE. The tool evaluates digital health technologies using aggregate organizational data such as costs, staffing hours, and workflow estimates. All data remains local to the user\u2019s session and is not stored on external servers."),
            ("\U0001f510", "Business Associate Agreements (BAA)",
             "A BAA is a legal contract required under HIPAA between a covered entity (like a CHC) and a vendor that handles PHI. DECIDE helps CHC leaders assess whether a digital health vendor has a proper BAA in place as part of the Privacy & Security pillar evaluation."),
            ("\U0001f4cb", "Privacy by Design",
             "DECIDE follows Privacy by Design principles \u2014 a framework developed by Dr. Ann Cavoukian that embeds privacy into the design of technology from the start, not as an afterthought. The 7 foundational principles include proactive prevention, privacy as the default, full lifecycle protection, and transparency."),
            ("\U0001f5c4\ufe0f", "Data Storage & Security",
             "DECIDE evaluates whether vendors store data on encrypted, US-based servers, whether patients can request data deletion, and whether vendors use patient data to train AI models. These are critical questions that CHCs must ask before adopting any digital health tool."),
            ("\u2696\ufe0f", "Regulatory Landscape",
             "The digital health regulatory environment is rapidly evolving. The FDA, FTC, and ONC are all developing frameworks for AI governance in healthcare. DECIDE helps CHCs stay ahead by building regulatory awareness into the evaluation process, ensuring that adopted tools meet current and emerging compliance standards."),
        ]

        for icon, title, text in security_sections:
            st.markdown(f"""
            <div class="sec-card">
                <div style="font-size:36px; text-align:center; margin-bottom:10px;">{icon}</div>
                <div class="sec-card-title">{title}</div>
                <div class="sec-card-text">{text}</div>
            </div>
            """, unsafe_allow_html=True)

    elif page == "Blogs":

        st.markdown("""
        <style>
            .blog-header {
                font-family: 'Times New Roman', serif;
                font-size: 36px;
                font-weight: bold;
                text-align: center;
                color: #3E2723;
                margin-top: 40px;
                margin-bottom: 10px;
            }
            .blog-divider {
                width: 80px;
                height: 3px;
                background: linear-gradient(90deg, #C4A882, #6D4C41);
                margin: 0 auto 40px auto;
                border-radius: 2px;
            }
            .blog-card {
                background: rgba(255,255,255,0.96);
                border-radius: 16px;
                padding: 24px 28px;
                margin-bottom: 18px;
                box-shadow: 0 4px 18px rgba(62,39,35,0.07);
                border: 1px solid #E8E0D8;
                border-left: 5px solid #C4A882;
            }
            .blog-card-title {
                font-family: 'Times New Roman', serif;
                font-size: 18px;
                font-weight: bold;
                color: #3E2723;
                margin-bottom: 8px;
            }
            .blog-card-meta {
                font-family: 'Times New Roman', serif;
                font-size: 12px;
                color: #888;
                margin-bottom: 10px;
            }
            .blog-card-text {
                font-family: 'Times New Roman', serif;
                font-size: 14px;
                color: #444;
                line-height: 1.7;
            }
        </style>
        """, unsafe_allow_html=True)

        st.markdown('<div class="blog-header">Blogs</div>', unsafe_allow_html=True)
        st.markdown('<div class="blog-divider"></div>', unsafe_allow_html=True)

        blogs = [
            ("Why Nearly Half of Digital Health Implementations Fail",
             "March 2026",
             "A systematic review of 221 eHealth studies found that 46.5% reported failure outcomes, with cost being the number one contributing factor. For community health centers with limited budgets, the stakes of a failed implementation are even higher."),
            ("The EHR Burnout Crisis: Lessons for Digital Health Adoption",
             "February 2026",
             "Electronic health records were supposed to save money and improve care. Instead, primary care physicians now spend up to 6 hours per day on EHR tasks, and 74.5% of burned-out physicians identify EHR as a contributor. What can CHCs learn from this before adopting the next wave of digital tools?"),
            ("AI Bias in Healthcare: The Obermeyer Algorithm Scandal",
             "January 2026",
             "A landmark study in Science revealed that a widely used commercial algorithm systematically under-referred Black patients for care management programs. The algorithm used healthcare costs as a proxy for needs \u2014 but Black patients historically spend less due to structural barriers. This is why equity evaluation matters."),
            ("Privacy by Design: 7 Principles Every CHC Should Know",
             "December 2025",
             "Dr. Ann Cavoukian\u2019s Privacy by Design framework offers 7 foundational principles for embedding privacy into technology from the ground up. For CHCs handling sensitive patient data, understanding these principles is essential before adopting any new digital tool."),
            ("The NASSS Framework: Why Digital Health Tools Get Abandoned",
             "November 2025",
             "The NASSS framework by Greenhalgh et al. identifies key reasons why digital health innovations fail to scale or sustain \u2014 from technology complexity to organizational readiness. DECIDE incorporates these insights into its Sustainability pillar."),
        ]

        for title, date, text in blogs:
            st.markdown(f"""
            <div class="blog-card">
                <div class="blog-card-title">{title}</div>
                <div class="blog-card-meta">{date}</div>
                <div class="blog-card-text">{text}</div>
            </div>
            """, unsafe_allow_html=True)

    elif page == "Contact Us":

        st.markdown("""
        <style>
            .contact-header {
                font-family: 'Times New Roman', serif;
                font-size: 36px;
                font-weight: bold;
                text-align: center;
                color: #3E2723;
                margin-top: 40px;
                margin-bottom: 10px;
            }
            .contact-divider {
                width: 80px;
                height: 3px;
                background: linear-gradient(90deg, #C4A882, #6D4C41);
                margin: 0 auto 40px auto;
                border-radius: 2px;
            }
            .contact-card {
                background: rgba(255,255,255,0.96);
                border-radius: 16px;
                padding: 36px 40px;
                box-shadow: 0 4px 18px rgba(62,39,35,0.07);
                border: 1px solid #E8E0D8;
                border-left: 5px solid #C4A882;
                max-width: 600px;
                margin: 0 auto;
            }
            .contact-text {
                font-family: 'Times New Roman', serif;
                font-size: 16px;
                color: #444;
                line-height: 2;
                text-align: center;
            }
        </style>
        """, unsafe_allow_html=True)

        st.markdown('<div class="contact-header">Contact Us</div>', unsafe_allow_html=True)
        st.markdown('<div class="contact-divider"></div>', unsafe_allow_html=True)

        st.markdown("""
        <div class="contact-card">
            <div style="font-size:48px; text-align:center; margin-bottom:16px;">\U0001f4e9</div>
            <div class="contact-text">
                <strong>Email:</strong> skish1@stu.mcphs.edu<br><br>
                <strong>Phone:</strong> Available upon request<br><br>
                <strong>Built for:</strong> Hack the Health Gap Hackathon 2026<br><br>
                <em>We welcome feedback, collaboration inquiries, and questions about DECIDE.</em>
            </div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("")
        col_l, col_form, col_r = st.columns([1, 2, 1])
        with col_form:
            st.markdown("<h4 style='font-family:Times New Roman,serif; text-align:center; margin-top:30px; text-decoration:underline;'>Send Us a Message</h4>", unsafe_allow_html=True)
            st.text_input("Your Name", key="contact_name")
            st.text_input("Your Email", key="contact_email")
            st.text_area("Message", key="contact_msg", height=120)
            if st.button("Send Message", key="send_msg", use_container_width=True):
                st.success("Message sent! (Demo mode) We'll get back to you soon.")


    elif page == "Evaluate Tool":
        st.markdown("""
        <style>
            @keyframes slideDown {
                from { opacity: 0; transform: translateY(-20px); }
                to { opacity: 1; transform: translateY(0); }
            }
            @keyframes pulseGlow {
                0% { box-shadow: 0 0 5px rgba(196,168,130,0.3); }
                50% { box-shadow: 0 0 20px rgba(196,168,130,0.5); }
                100% { box-shadow: 0 0 5px rgba(196,168,130,0.3); }
            }
            .eval-header {
                font-family: 'Times New Roman', serif;
                font-size: 36px;
                font-weight: bold;
                text-align: center;
                color: #3E2723;
                margin-top: 30px;
                margin-bottom: 5px;
                animation: slideDown 0.7s ease-out;
            }
            .eval-subtitle {
                font-family: 'Times New Roman', serif;
                font-size: 16px;
                text-align: center;
                color: #6D4C41;
                margin-bottom: 25px;
                animation: slideDown 0.9s ease-out;
            }
            .eval-divider {
                width: 80px;
                height: 3px;
                background: linear-gradient(90deg, #C4A882, #6D4C41);
                margin: 0 auto 30px auto;
                border-radius: 2px;
            }
            .pillar-header {
                font-family: 'Times New Roman', serif;
                font-size: 24px;
                font-weight: bold;
                color: #3E2723;
                text-align: center;
                margin-bottom: 5px;
            }
            .pillar-desc {
                font-family: 'Times New Roman', serif;
                font-size: 14px;
                color: #6D4C41;
                text-align: center;
                font-style: italic;
                margin-bottom: 20px;
            }
            .pillar-framework {
                background: #FBF7F2;
                border-radius: 10px;
                padding: 12px 18px;
                margin-bottom: 20px;
                border: 1px solid #E8E0D8;
                font-family: 'Times New Roman', serif;
                font-size: 13px;
                color: #6D4C41;
                text-align: center;
            }
            .result-metric {
                background: rgba(255,255,255,0.96);
                border-radius: 14px;
                padding: 22px;
                text-align: center;
                box-shadow: 0 4px 16px rgba(62,39,35,0.07);
                border: 1px solid #E8E0D8;
                animation: pulseGlow 3s ease-in-out infinite;
            }
            .result-label {
                font-family: 'Times New Roman', serif;
                font-size: 13px;
                color: #888;
                margin-bottom: 6px;
            }
            .result-value {
                font-family: 'Times New Roman', serif;
                font-size: 30px;
                font-weight: bold;
            }
            .score-badge {
                display: inline-block;
                padding: 8px 24px;
                border-radius: 30px;
                font-family: 'Times New Roman', serif;
                font-size: 16px;
                font-weight: bold;
                margin-top: 10px;
            }
        </style>
        """, unsafe_allow_html=True)

        st.markdown('<div class="eval-header">\U0001f50d Evaluate a Digital Health Tool</div>', unsafe_allow_html=True)
        st.markdown('<div class="eval-subtitle">Complete each section to receive your DECIDE recommendation</div>', unsafe_allow_html=True)
        st.markdown('<div class="eval-divider"></div>', unsafe_allow_html=True)

        screening, p1, p2, p3, p4, p5 = st.tabs([
            "\U0001f6a6 Quick Screening",
            "\U0001f4b0 Pillar 1: Cost & Value",
            "\U0001f469\u200d\u2695\ufe0f Pillar 2: Staff Readiness",
            "\U0001f91d Pillar 3: Patient Trust & Equity",
            "\U0001f512 Pillar 4: Privacy & Security",
            "\U0001f504 Pillar 5: Sustainability"
        ])

        # ===================== QUICK SCREENING =====================
        with screening:
            st.markdown('<div class="pillar-header">\U0001f6a6 Quick Screening</div>', unsafe_allow_html=True)
            st.markdown('<div class="pillar-desc">5 deal-breaker questions to determine if this tool is worth evaluating further</div>', unsafe_allow_html=True)

            st.markdown("""
            <div class="pillar-framework">
                \U0001f4a1 <strong>Why this matters:</strong> Before investing 20 minutes in a full evaluation, these 5 questions catch obvious non-starters \u2014 saving your team time and protecting your CHC from avoidable risks.
            </div>
            """, unsafe_allow_html=True)

            tool_name = st.text_input("\U0001f3e5 What is the name of the digital health tool you are evaluating?", key="tool_name_input")

            st.markdown("---")

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
                st.error("\U0001f6d1 **STOP:** Multiple deal-breakers detected. This tool may not be appropriate for your CHC. Proceed with extreme caution or consider alternatives.")
            elif no_count == 1:
                st.warning("\u26a0\ufe0f **One deal-breaker flagged.** You can proceed, but address this issue before making a final decision.")
            elif unsure_count >= 2:
                st.warning("\u26a0\ufe0f **Multiple uncertainties.** Gather more information from the vendor before proceeding.")
            else:
                st.success("\u2705 **No deal-breakers found!** Proceed to the 5-pillar evaluation using the tabs above.")

        # ===================== PILLAR 1: COST & VALUE =====================
        with p1:
            st.markdown('<div class="pillar-header">\U0001f4b0 Pillar 1: Cost & Value</div>', unsafe_allow_html=True)
            st.markdown('<div class="pillar-desc">Will this tool save or cost your CHC money?</div>', unsafe_allow_html=True)

            st.markdown("""
            <div class="pillar-framework">
                \U0001f4da <strong>Based on:</strong> Net Monetary Benefit (NMB) \u2014 a health economic evaluation method that compares the monetary value of benefits against costs. Used by ICER, NICE, and the Peterson Health Technology Institute.
            </div>
            """, unsafe_allow_html=True)

            st.markdown("#### \U0001f4c9 Costs")
            c1_left, c1_right = st.columns(2)
            with c1_left:
                annual_cost = st.number_input("Annual subscription / licensing fee ($)", min_value=0, value=15000, step=500, key="c1")
                implementation_cost = st.number_input("One-time implementation / setup cost ($)", min_value=0, value=5000, step=500, key="c2")
            with c1_right:
                training_hours = st.number_input("Total staff training hours needed", min_value=0, value=20, step=1, key="c3")
                staff_wage = st.number_input("Average staff hourly wage ($)", min_value=0.0, value=25.0, step=0.5, key="c4")

            st.markdown("#### \U0001f4c8 Benefits")

            st.markdown("""
            <div class="pillar-framework">
                \u26a0\ufe0f <strong>Vendor claims vs. your estimates:</strong> Vendors often overstate benefits. Enter YOUR conservative estimate, not the vendor's marketing numbers. DECIDE works best with honest inputs.
            </div>
            """, unsafe_allow_html=True)

            b1_left, b1_right = st.columns(2)
            with b1_left:
                hours_saved_week = st.number_input("Estimated staff hours saved per week", min_value=0.0, value=8.0, step=0.5, key="b1")
                noshow_reduction = st.slider("Expected no-show reduction (percentage points)", 0, 30, 5, key="b2")
            with b1_right:
                patients_year = st.number_input("Total patients per year", min_value=0, value=10000, step=500, key="b3")
                visit_value = st.number_input("Average revenue / value per completed visit ($)", min_value=0.0, value=85.0, step=5.0, key="b4")

            visit_rate = st.slider("Approximate visits per patient per year", 1, 10, 3, key="b5")

            # Confidence adjustment
            st.markdown("#### \U0001f3af Confidence Adjustment")
            st.markdown("""
            <div class="pillar-framework">
                How confident are you in the benefit estimates above? This adjusts the calculation to account for uncertainty \u2014 lower confidence = more conservative result.
            </div>
            """, unsafe_allow_html=True)
            confidence = st.slider("Your confidence in benefit estimates (%)", 30, 100, 70, key="conf")
            conf_factor = confidence / 100

            st.markdown("---")

            # Calculations
            training_cost = training_hours * staff_wage
            total_annual_cost = annual_cost + (implementation_cost / 3) + training_cost
            time_savings = hours_saved_week * staff_wage * 52 * conf_factor
            noshow_value = (noshow_reduction / 100) * patients_year * visit_rate * visit_value * conf_factor
            total_annual_benefit = time_savings + noshow_value
            net_value = total_annual_benefit - total_annual_cost
            roi = (net_value / total_annual_cost * 100) if total_annual_cost > 0 else 0
            breakeven_months = (total_annual_cost / (total_annual_benefit / 12)) if total_annual_benefit > 0 else float('inf')

            # Score
            if roi > 20 and breakeven_months < 12:
                p1_score = 5
                p1_decision = "adopt"
            elif net_value > 0:
                p1_score = 4 if roi > 10 else 3
                p1_decision = "pilot"
            elif net_value > -2000:
                p1_score = 2
                p1_decision = "pilot"
            else:
                p1_score = 1
                p1_decision = "reject"
            st.session_state["p1_score"] = p1_score

            # Display
            st.markdown("### \U0001f4ca Results")
            r1, r2, r3 = st.columns(3)
            with r1:
                nv_color = "#2A9D8F" if net_value >= 0 else "#E76F51"
                st.markdown(f'<div class="result-metric"><div class="result-label">Net Annual Value</div><div class="result-value" style="color:{nv_color};">${net_value:,.0f}</div></div>', unsafe_allow_html=True)
            with r2:
                roi_color = "#2A9D8F" if roi > 0 else "#E76F51"
                st.markdown(f'<div class="result-metric"><div class="result-label">Return on Investment</div><div class="result-value" style="color:{roi_color};">{roi:.0f}%</div></div>', unsafe_allow_html=True)
            with r3:
                be_text = f"{breakeven_months:.1f} mo" if breakeven_months < 100 else "N/A"
                st.markdown(f'<div class="result-metric"><div class="result-label">Break-even</div><div class="result-value" style="color:#3E2723;">{be_text}</div></div>', unsafe_allow_html=True)

            st.markdown("")

            # Decision rule
            if p1_decision == "adopt":
                st.markdown('<div style="text-align:center;"><span class="score-badge" style="background:#2A9D8F; color:white;">\u2705 ADOPT \u2014 Strong financial case (ROI > 20%, break-even < 12 months)</span></div>', unsafe_allow_html=True)
            elif p1_decision == "pilot":
                st.markdown('<div style="text-align:center;"><span class="score-badge" style="background:#E9C46A; color:#3E2723;">\u26a0\ufe0f PILOT \u2014 Positive value but consider a trial period to validate estimates</span></div>', unsafe_allow_html=True)
            else:
                st.markdown('<div style="text-align:center;"><span class="score-badge" style="background:#E76F51; color:white;">\u274c DO NOT ADOPT \u2014 Negative net value at current estimates</span></div>', unsafe_allow_html=True)

            # Breakdown
            with st.expander("\U0001f4cb View detailed cost breakdown"):
                st.markdown(f"""
                | Item | Amount |
                |------|--------|
                | Annual subscription | ${annual_cost:,.0f} |
                | Implementation (amortized 3yr) | ${implementation_cost/3:,.0f} |
                | Training cost | ${training_cost:,.0f} |
                | **Total annual cost** | **${total_annual_cost:,.0f}** |
                | | |
                | Time savings (confidence-adjusted) | ${time_savings:,.0f} |
                | No-show recovery (confidence-adjusted) | ${noshow_value:,.0f} |
                | **Total annual benefit** | **${total_annual_benefit:,.0f}** |
                | | |
                | **Net value** | **${net_value:,.0f}** |
                | Confidence level used | {confidence}% |
                """)

        # ===================== PILLAR 2: STAFF READINESS =====================
        with p2:
            st.markdown('<div class="pillar-header">\U0001f469\u200d\u2695\ufe0f Pillar 2: Staff Readiness</div>', unsafe_allow_html=True)
            st.markdown('<div class="pillar-desc">Can your staff realistically adopt this tool?</div>', unsafe_allow_html=True)

            st.markdown("""
            <div class="pillar-framework">
                \U0001f4da <strong>Based on:</strong> Consolidated Framework for Implementation Research (CFIR) \u2014 the most widely used implementation science framework, covering inner setting, intervention characteristics, and process factors.
            </div>
            """, unsafe_allow_html=True)

            p2q1 = st.slider("1. How much training is required? (1 = Extensive retraining, 5 = Minimal/none)", 1, 5, 3, key="p2q1")
            p2q2 = st.slider("2. Does this tool reduce or add to daily workflow burden? (1 = Adds significant burden, 5 = Significantly reduces)", 1, 5, 3, key="p2q2")
            p2q3 = st.slider("3. Have frontline staff been consulted? (1 = Not at all, 5 = Deeply involved)", 1, 5, 3, key="p2q3")
            p2q4 = st.slider("4. Does the vendor provide onboarding and ongoing support? (1 = None, 5 = Comprehensive)", 1, 5, 3, key="p2q4")
            p2q5 = st.slider("5. Is your team currently experiencing burnout? (1 = Severe burnout, 5 = Stable and well-staffed)", 1, 5, 3, key="p2q5")

            p2_score = round((p2q1 + p2q2 + p2q3 + p2q4 + p2q5) / 5, 1)
            st.session_state["p2_score"] = p2_score

            st.markdown("---")
            if p2_score >= 4:
                st.markdown(f'<div style="text-align:center;"><span class="score-badge" style="background:#2A9D8F; color:white;">\u2705 Score: {p2_score}/5 \u2014 Team is ready for adoption</span></div>', unsafe_allow_html=True)
            elif p2_score >= 3:
                st.markdown(f'<div style="text-align:center;"><span class="score-badge" style="background:#E9C46A; color:#3E2723;">\u26a0\ufe0f Score: {p2_score}/5 \u2014 Address training and workflow gaps first</span></div>', unsafe_allow_html=True)
            else:
                st.markdown(f'<div style="text-align:center;"><span class="score-badge" style="background:#E76F51; color:white;">\u274c Score: {p2_score}/5 \u2014 High risk of adoption failure</span></div>', unsafe_allow_html=True)

            if p2q3 < 3:
                st.info("\U0001f4a1 **Tip:** Implementation research shows frontline staff buy-in is the #1 predictor of whether digital tools get used. Consider involving staff before committing.")

        # ===================== PILLAR 3: PATIENT TRUST & EQUITY =====================
        with p3:
            st.markdown('<div class="pillar-header">\U0001f91d Pillar 3: Patient Trust & Equity</div>', unsafe_allow_html=True)
            st.markdown('<div class="pillar-desc">Will this tool serve ALL your patients equitably?</div>', unsafe_allow_html=True)

            st.markdown("""
            <div class="pillar-framework">
                \U0001f4da <strong>Based on:</strong> HEAL Framework (eClinicalMedicine, 2024) for performance equity assessment + Aequitas open-source fairness audit toolkit. CHCs serve America's most vulnerable populations \u2014 equity isn't optional.
            </div>
            """, unsafe_allow_html=True)

            p3q1 = st.slider("1. Does the tool support all primary languages of your patients? (1 = English only, 5 = Full multilingual)", 1, 5, 3, key="p3q1")
            p3q2 = st.slider("2. Is it accessible across digital literacy levels? (1 = Requires tech-savvy users, 5 = Designed for low literacy)", 1, 5, 3, key="p3q2")
            p3q3 = st.slider("3. Has the vendor provided evidence of equitable performance across demographics? (1 = No data, 5 = Published bias audit)", 1, 5, 3, key="p3q3")
            p3q4 = st.slider("4. Has your patient advisory board been consulted? (1 = Not at all, 5 = Actively involved)", 1, 5, 3, key="p3q4")
            p3q5 = st.slider("5. Does it work without a smartphone or reliable internet? (1 = Requires both, 5 = Works via SMS/phone/offline)", 1, 5, 3, key="p3q5")

            p3_score = round((p3q1 + p3q2 + p3q3 + p3q4 + p3q5) / 5, 1)
            st.session_state["p3_score"] = p3_score

            st.markdown("---")
            if p3_score >= 4:
                st.markdown(f'<div style="text-align:center;"><span class="score-badge" style="background:#2A9D8F; color:white;">\u2705 Score: {p3_score}/5 \u2014 Strong equity profile</span></div>', unsafe_allow_html=True)
            elif p3_score >= 3:
                st.markdown(f'<div style="text-align:center;"><span class="score-badge" style="background:#E9C46A; color:#3E2723;">\u26a0\ufe0f Score: {p3_score}/5 \u2014 Equity gaps detected. Request bias audit from vendor.</span></div>', unsafe_allow_html=True)
            else:
                st.markdown(f'<div style="text-align:center;"><span class="score-badge" style="background:#E76F51; color:white;">\u274c Score: {p3_score}/5 \u2014 Significant equity concerns. May exclude vulnerable patients.</span></div>', unsafe_allow_html=True)

            if p3q3 < 3:
                st.info("\U0001f4a1 **Did you know?** A widely used healthcare algorithm was found to systematically under-refer Black patients for care (Obermeyer et al., Science, 2019). Always ask vendors for bias audit data.")

        # ===================== PILLAR 4: PRIVACY & SECURITY =====================
        with p4:
            st.markdown('<div class="pillar-header">\U0001f512 Pillar 4: Privacy & Security</div>', unsafe_allow_html=True)
            st.markdown('<div class="pillar-desc">Is patient data protected?</div>', unsafe_allow_html=True)

            st.markdown("""
            <div class="pillar-framework">
                \U0001f4da <strong>Based on:</strong> Privacy by Design (Cavoukian) \u2014 7 foundational principles for embedding privacy into technology + HIPAA Security Rule requirements.
            </div>
            """, unsafe_allow_html=True)

            p4q1 = st.slider("1. Is a signed HIPAA BAA in place? (1 = No, 5 = Yes, fully executed)", 1, 5, 3, key="p4q1")
            p4q2 = st.slider("2. Where is patient data stored? (1 = Unknown/overseas, 5 = US-based, encrypted, documented)", 1, 5, 3, key="p4q2")
            p4q3 = st.slider("3. Can the CHC delete patient data on request? (1 = No/unclear, 5 = Yes, documented process)", 1, 5, 3, key="p4q3")
            p4q4 = st.slider("4. Does the vendor use patient data to train AI? (1 = Yes without consent, 5 = No, or explicit consent only)", 1, 5, 3, key="p4q4")
            p4q5 = st.slider("5. Has the vendor had any data breaches? (1 = Yes, multiple, 5 = None, security audit available)", 1, 5, 3, key="p4q5")

            p4_score = round((p4q1 + p4q2 + p4q3 + p4q4 + p4q5) / 5, 1)
            st.session_state["p4_score"] = p4_score

            st.markdown("---")
            if p4_score >= 4:
                st.markdown(f'<div style="text-align:center;"><span class="score-badge" style="background:#2A9D8F; color:white;">\u2705 Score: {p4_score}/5 \u2014 Strong privacy posture</span></div>', unsafe_allow_html=True)
            elif p4_score >= 3:
                st.markdown(f'<div style="text-align:center;"><span class="score-badge" style="background:#E9C46A; color:#3E2723;">\u26a0\ufe0f Score: {p4_score}/5 \u2014 Clarify data practices with vendor</span></div>', unsafe_allow_html=True)
            else:
                st.markdown(f'<div style="text-align:center;"><span class="score-badge" style="background:#E76F51; color:white;">\u274c Score: {p4_score}/5 \u2014 Do NOT proceed until privacy issues are resolved</span></div>', unsafe_allow_html=True)

            if p4q1 < 3:
                st.error("\U0001f6a8 **Critical:** No HIPAA BAA means your CHC may be legally liable if patient data is compromised. This should be a non-negotiable requirement.")

        # ===================== PILLAR 5: SUSTAINABILITY =====================
        with p5:
            st.markdown('<div class="pillar-header">\U0001f504 Pillar 5: Sustainability</div>', unsafe_allow_html=True)
            st.markdown('<div class="pillar-desc">Can your CHC maintain this long-term?</div>', unsafe_allow_html=True)

            st.markdown("""
            <div class="pillar-framework">
                \U0001f4da <strong>Based on:</strong> NASSS Framework (Greenhalgh et al., JMIR, 2017) \u2014 Non-Adoption, Abandonment, Scale-up, Spread, and Sustainability. Explains why digital health tools get abandoned after initial enthusiasm fades.
            </div>
            """, unsafe_allow_html=True)

            p5q1 = st.slider("1. Funding source? (1 = Time-limited grant only, 5 = Sustainable operating budget)", 1, 5, 3, key="p5q1")
            p5q2 = st.slider("2. What if the vendor shuts down? (1 = Total data loss, 5 = Full export + alternatives exist)", 1, 5, 3, key="p5q2")
            p5q3 = st.slider("3. Contract flexibility? (1 = Multi-year lock-in, 5 = Month-to-month or easy exit)", 1, 5, 3, key="p5q3")
            p5q4 = st.slider("4. Can the tool scale if your CHC grows? (1 = Fixed capacity, 5 = Easily scalable)", 1, 5, 3, key="p5q4")
            p5q5 = st.slider("5. Vendor track record? (1 = New/unproven, 5 = Multi-year proven support history)", 1, 5, 3, key="p5q5")

            p5_score = round((p5q1 + p5q2 + p5q3 + p5q4 + p5q5) / 5, 1)
            st.session_state["p5_score"] = p5_score

            st.markdown("---")
            if p5_score >= 4:
                st.markdown(f'<div style="text-align:center;"><span class="score-badge" style="background:#2A9D8F; color:white;">\u2705 Score: {p5_score}/5 \u2014 Sustainable for long-term use</span></div>', unsafe_allow_html=True)
            elif p5_score >= 3:
                st.markdown(f'<div style="text-align:center;"><span class="score-badge" style="background:#E9C46A; color:#3E2723;">\u26a0\ufe0f Score: {p5_score}/5 \u2014 Plan an exit strategy before committing</span></div>', unsafe_allow_html=True)
            else:
                st.markdown(f'<div style="text-align:center;"><span class="score-badge" style="background:#E76F51; color:white;">\u274c Score: {p5_score}/5 \u2014 High risk of abandonment. Consider alternatives.</span></div>', unsafe_allow_html=True)

            if p5q1 < 3:
                st.info("\U0001f4a1 **Tip:** Grant-funded tools often get abandoned when funding ends. Have a plan for how this tool will be sustained beyond the grant period.")
    elif page == "Advanced Analysis":
        render_advanced_analysis()

    elif page == "Learn":
        render_learning_game()

    elif page == "Results":

        import plotly.graph_objects as go

        st.markdown("""
        <style>
            @keyframes fadeInUp {
                from { opacity: 0; transform: translateY(30px); }
                to { opacity: 1; transform: translateY(0); }
            }
            @keyframes bounceIn {
                0% { opacity: 0; transform: scale(0.5); }
                60% { opacity: 1; transform: scale(1.05); }
                100% { transform: scale(1); }
            }
            @keyframes shimmer {
                0% { background-position: -200px 0; }
                100% { background-position: 200px 0; }
            }
            .res-header {
                font-family: 'Times New Roman', serif;
                font-size: 36px;
                font-weight: bold;
                text-align: center;
                color: #3E2723;
                margin-top: 30px;
                margin-bottom: 10px;
                animation: fadeInUp 0.7s ease-out;
            }
            .res-divider {
                width: 80px;
                height: 3px;
                background: linear-gradient(90deg, #C4A882, #6D4C41);
                margin: 0 auto 30px auto;
                border-radius: 2px;
            }
            .verdict-box {
                border-radius: 20px;
                padding: 40px;
                text-align: center;
                margin-bottom: 30px;
                animation: bounceIn 0.8s ease-out;
            }
            .verdict-icon {
                font-size: 64px;
                margin-bottom: 10px;
            }
            .verdict-text {
                font-family: 'Times New Roman', serif;
                font-size: 36px;
                font-weight: bold;
                letter-spacing: 3px;
            }
            .verdict-score {
                font-family: 'Times New Roman', serif;
                font-size: 52px;
                font-weight: bold;
                margin: 10px 0;
            }
            .verdict-desc {
                font-family: 'Times New Roman', serif;
                font-size: 16px;
                max-width: 600px;
                margin: 10px auto 0 auto;
                line-height: 1.7;
            }
            .pillar-bar-card {
                background: rgba(255,255,255,0.96);
                border-radius: 14px;
                padding: 18px 22px;
                margin-bottom: 12px;
                box-shadow: 0 3px 14px rgba(62,39,35,0.06);
                border: 1px solid #E8E0D8;
                animation: fadeInUp 0.6s ease-out;
            }
            .pillar-bar-name {
                font-family: 'Times New Roman', serif;
                font-size: 16px;
                font-weight: bold;
                color: #3E2723;
            }
            .pillar-bar-weight {
                font-family: 'Times New Roman', serif;
                font-size: 12px;
                color: #888;
            }
            .pillar-bar-score {
                font-family: 'Times New Roman', serif;
                font-size: 15px;
                font-weight: bold;
            }
            .bar-outer {
                background: #E8E0D8;
                border-radius: 8px;
                height: 12px;
                overflow: hidden;
                margin-top: 8px;
            }
            .bar-inner {
                height: 100%;
                border-radius: 8px;
                transition: width 1s ease-out;
            }
            .action-card {
                background: rgba(255,255,255,0.96);
                border-radius: 14px;
                padding: 24px 28px;
                margin-top: 24px;
                box-shadow: 0 4px 18px rgba(62,39,35,0.07);
                border-left: 5px solid #C4A882;
                animation: fadeInUp 0.9s ease-out;
            }
            .action-title {
                font-family: 'Times New Roman', serif;
                font-size: 20px;
                font-weight: bold;
                color: #3E2723;
                text-decoration: underline;
                text-align: center;
                margin-bottom: 14px;
            }
            .action-text {
                font-family: 'Times New Roman', serif;
                font-size: 15px;
                color: #444;
                line-height: 1.9;
            }
        </style>
        """, unsafe_allow_html=True)

        st.markdown('<div class="res-header">\U0001f4ca DECIDE Results Dashboard</div>', unsafe_allow_html=True)
        st.markdown('<div class="res-divider"></div>', unsafe_allow_html=True)

        # Get scores
        tool_name = st.session_state.get("tool_name", "the tool")
        if not tool_name:
            tool_name = "the tool"
        p1 = st.session_state.get("p1_score", 3)
        p2 = st.session_state.get("p2_score", 3.0)
        p3 = st.session_state.get("p3_score", 3.0)
        p4 = st.session_state.get("p4_score", 3.0)
        p5 = st.session_state.get("p5_score", 3.0)

        # Weighted overall score
        weights = {"Cost & Value": 0.25, "Staff Readiness": 0.20, "Patient Trust & Equity": 0.25, "Privacy & Security": 0.15, "Sustainability": 0.15}
        scores = {"Cost & Value": float(p1), "Staff Readiness": float(p2), "Patient Trust & Equity": float(p3), "Privacy & Security": float(p4), "Sustainability": float(p5)}
        overall = sum(scores[k] * weights[k] for k in weights) / 5 * 100

        # Verdict
        if overall >= 70:
            verdict_icon = "\u2705"
            verdict_text = "ADOPT"
            verdict_color = "#2A9D8F"
            verdict_bg = "linear-gradient(135deg, #E8F5F0, #D4EDDA)"
            verdict_desc = f"<strong>{tool_name}</strong> scores well across all five pillars. The evidence supports moving forward with adoption or a full-scale implementation."
        elif overall >= 45:
            verdict_icon = "\u26a0\ufe0f"
            verdict_text = "PILOT WITH CONDITIONS"
            verdict_color = "#B8860B"
            verdict_bg = "linear-gradient(135deg, #FFF8E1, #FFEEBA)"
            verdict_desc = f"<strong>{tool_name}</strong> shows promise but has gaps in one or more pillars. Address the flagged issues and run a time-limited pilot (3-6 months) before full commitment."
        else:
            verdict_icon = "\u274c"
            verdict_text = "DO NOT ADOPT"
            verdict_color = "#E76F51"
            verdict_bg = "linear-gradient(135deg, #FDE8E4, #F8D7DA)"
            verdict_desc = f"<strong>{tool_name}</strong> has significant weaknesses across multiple pillars. The risks currently outweigh the potential benefits. Consider alternative tools or revisit after the vendor addresses key concerns."

        # Verdict display
        st.markdown(f"""
        <div class="verdict-box" style="background: {verdict_bg}; border: 2px solid {verdict_color};">
            <div class="verdict-icon">{verdict_icon}</div>
            <div class="verdict-text" style="color: {verdict_color};">{verdict_text}</div>
            <div class="verdict-score" style="color: {verdict_color};">{overall:.0f}/100</div>
            <div class="verdict-desc" style="color: #333;">{verdict_desc}</div>
        </div>
        """, unsafe_allow_html=True)

        # Radar Chart + Pillar Bars side by side
        col_chart, col_bars = st.columns([1, 1])

        with col_chart:
            categories = list(scores.keys())
            values = list(scores.values())
            values_plot = values + [values[0]]
            categories_plot = categories + [categories[0]]

            fig = go.Figure(data=go.Scatterpolar(
                r=values_plot,
                theta=categories_plot,
                fill='toself',
                fillcolor='rgba(196, 168, 130, 0.25)',
                line=dict(color='#6D4C41', width=2.5),
                marker=dict(size=8, color='#C4A882')
            ))

            fig.update_layout(
                polar=dict(
                    radialaxis=dict(visible=True, range=[0, 5], tickfont=dict(size=11, family="Times New Roman")),
                    angularaxis=dict(tickfont=dict(size=11, family="Times New Roman"))
                ),
                showlegend=False,
                margin=dict(l=50, r=50, t=30, b=30),
                paper_bgcolor='rgba(0,0,0,0)',
                plot_bgcolor='rgba(0,0,0,0)',
                height=400
            )

            st.plotly_chart(fig, use_container_width=True)

        with col_bars:
            pillar_info = [
                ("\U0001f4b0", "Cost & Value", float(p1), 0.25),
                ("\U0001f469\u200d\u2695\ufe0f", "Staff Readiness", float(p2), 0.20),
                ("\U0001f91d", "Patient Trust & Equity", float(p3), 0.25),
                ("\U0001f512", "Privacy & Security", float(p4), 0.15),
                ("\U0001f504", "Sustainability", float(p5), 0.15),
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
                <div class="pillar-bar-card">
                    <div style="display:flex; justify-content:space-between; align-items:center;">
                        <span class="pillar-bar-name">{icon} {name} <span class="pillar-bar-weight">(Weight: {int(weight*100)}%)</span></span>
                        <span class="pillar-bar-score" style="color:{bar_color};">{score}/5 \u2014 {status}</span>
                    </div>
                    <div class="bar-outer">
                        <div class="bar-inner" style="background:{bar_color}; width:{pct}%;"></div>
                    </div>
                </div>
                """, unsafe_allow_html=True)

        # Recommended Actions
        st.markdown("""
        <div class="action-card">
            <div class="action-title">\U0001f4cb Recommended Next Steps</div>
        """, unsafe_allow_html=True)

        actions = []
        if float(p1) < 3:
            actions.append("\u2022 <strong>Cost & Value:</strong> Re-evaluate the financial case. Request detailed cost breakdowns and independent ROI estimates from the vendor.")
        if float(p2) < 3:
            actions.append("\u2022 <strong>Staff Readiness:</strong> Consult frontline staff before proceeding. Assess training needs, workflow impact, and current burnout levels.")
        if float(p3) < 3:
            actions.append("\u2022 <strong>Patient Trust & Equity:</strong> Request a bias/fairness audit from the vendor. Verify language support and accessibility for your patient population.")
        if float(p4) < 3:
            actions.append("\u2022 <strong>Privacy & Security:</strong> Do NOT proceed until HIPAA compliance, BAA, and data handling practices are fully documented and verified.")
        if float(p5) < 3:
            actions.append("\u2022 <strong>Sustainability:</strong> Develop an exit strategy. Ensure data portability, avoid vendor lock-in, and plan for post-grant sustainability.")
        if not actions:
            actions.append("\u2022 All pillars are in good shape. Proceed with a pilot phase (3-6 months) and re-evaluate with DECIDE after the pilot concludes.")

        actions_html = "<br>".join(actions)
        st.markdown(f"""
            <div class="action-text">{actions_html}</div>
        </div>
        """, unsafe_allow_html=True)

        # Summary for board
        st.markdown("")
        st.markdown("")

        st.markdown(f"""
        <div style="background:rgba(255,255,255,0.96); border-radius:14px; padding:28px; margin-top:20px; box-shadow:0 4px 18px rgba(62,39,35,0.07); border:2px solid #C4A882; text-align:center; animation: fadeInUp 1s ease-out;">
            <div style="font-family:'Times New Roman',serif; font-size:20px; font-weight:bold; color:#3E2723; text-decoration:underline; margin-bottom:16px;">\U0001f4c4 Board Summary</div>
            <div style="font-family:'Times New Roman',serif; font-size:15px; color:#444; line-height:1.8; text-align:left; max-width:700px; margin:0 auto;">
                <strong>Tool Evaluated:</strong> {tool_name}<br>
                <strong>Overall Score:</strong> {overall:.0f}/100<br>
                <strong>Recommendation:</strong> {verdict_text}<br><br>
                <strong>Pillar Scores:</strong><br>
                \u2022 Cost & Value: {p1}/5<br>
                \u2022 Staff Readiness: {p2}/5<br>
                \u2022 Patient Trust & Equity: {p3}/5<br>
                \u2022 Privacy & Security: {p4}/5<br>
                \u2022 Sustainability: {p5}/5<br><br>
                <em>This evaluation was conducted using DECIDE (Digital Evaluation for Community Implementation Decisions), a structured framework grounded in health economic evaluation, implementation science, algorithmic fairness, privacy by design, and sustainability research.</em>
            </div>
        </div>
        """, unsafe_allow_html=True)

        # Download Report
        from report_generator import generate_report_pdf

        st.markdown("")
        st.markdown("")
        st.markdown("""
        <div style="text-align:center; animation: fadeInUp 1.2s ease-out;">
            <div style="font-family:'Times New Roman',serif; font-size:20px; font-weight:bold; color:#3E2723; margin-bottom:10px;">\U0001f4e5 Download Full Report</div>
            <div style="font-family:'Times New Roman',serif; font-size:14px; color:#6D4C41; margin-bottom:16px;">Generate a comprehensive PDF evaluation report to share with your board, leadership, or funders.</div>
        </div>
        """, unsafe_allow_html=True)

        pdf_bytes = generate_report_pdf()
        dl_col1, dl_col2, dl_col3 = st.columns([1, 2, 1])
        with dl_col2:
            st.download_button(
                label="\U0001f4c4 Download DECIDE Report (.pdf)",
                data=pdf_bytes,
                file_name=f"DECIDE_Report_{st.session_state.get('tool_name', 'tool')}.pdf",
                mime="application/pdf",
                use_container_width=True,
            )