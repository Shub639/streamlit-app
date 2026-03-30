import streamlit as st
import random
import numpy as np


def render_learning_game():

    st.markdown("""
    <style>
        .game-header { font-family: 'Times New Roman', serif; font-size: 36px; font-weight: bold; text-align:center; color:#3E2723; margin-top:30px; }
        .game-sub { font-family: 'Times New Roman', serif; font-size: 16px; text-align:center; color:#6D4C41; font-style:italic; margin-bottom:18px; }
        .game-divider { width:80px; height:3px; background: linear-gradient(90deg, #C4A882, #6D4C41); margin: 0 auto 26px auto; border-radius:2px; }
        .lesson-card { background: rgba(255,255,255,0.75); backdrop-filter: blur(12px); border-radius: 16px; padding: 24px 28px; margin-bottom: 20px; box-shadow: 0 4px 18px rgba(62,39,35,0.07); border: 1px solid #E8E0D8; border-left: 5px solid #C4A882; }
        .lesson-title { font-family: 'Times New Roman', serif; font-size: 20px; font-weight: bold; color: #3E2723; text-decoration: underline; margin-bottom: 10px; }
        .lesson-text { font-family: 'Times New Roman', serif; font-size: 14px; color: #444; line-height: 1.8; }
        .formula-box { background: #FBF7F2; border-radius: 10px; padding: 14px 18px; margin: 12px 0; border: 1px solid #E8E0D8; font-family: 'Courier New', monospace; font-size: 15px; color: #3E2723; text-align: center; }
        .example-box { background: #F0EBE3; border-radius: 10px; padding: 16px 20px; margin: 12px 0; border: 1px dashed #C4A882; font-family: 'Times New Roman', serif; font-size: 14px; color: #555; line-height: 1.7; }
        .score-display { font-family: 'Times New Roman', serif; font-size: 28px; font-weight: bold; text-align: center; color: #3E2723; padding: 20px; }
    </style>
    """, unsafe_allow_html=True)

    st.markdown('<div class="game-header">\U0001f3ae Learn Health Economics</div>', unsafe_allow_html=True)
    st.markdown('<div class="game-sub">Interactive lessons + quizzes to master digital health evaluation</div>', unsafe_allow_html=True)
    st.markdown('<div class="game-divider"></div>', unsafe_allow_html=True)

    if "game_score" not in st.session_state:
        st.session_state["game_score"] = 0
    if "game_total" not in st.session_state:
        st.session_state["game_total"] = 0
    if "game_level" not in st.session_state:
        st.session_state["game_level"] = 1

    tab_learn, tab_quiz, tab_practice = st.tabs([
        "\U0001f4d6 Lessons",
        "\U0001f9e0 Quiz Challenge",
        "\U0001f527 Practice Calculator"
    ])

    # ======================== LESSONS TAB ========================
    with tab_learn:

        lesson = st.selectbox("Choose a topic:", [
            "1. Deterministic vs Probabilistic Analysis",
            "2. Costs: What to Count",
            "3. Effectiveness: Measuring Benefits",
            "4. Net Monetary Benefit (NMB)",
            "5. Net Health Benefit (NHB)",
            "6. Incremental Cost-Effectiveness Ratio (ICER)",
            "7. Cost-Effectiveness Plane",
            "8. PSA (Probabilistic Sensitivity Analysis)",
            "9. CEAC (Cost-Effectiveness Acceptability Curve)",
            "10. EVPI (Expected Value of Perfect Information)",
            "11. Willingness-to-Pay (WTP)",
            "12. Putting It All Together"
        ])

        if "1." in lesson:
            st.markdown("""
            <div class="lesson-card">
                <div class="lesson-title">\U0001f4ca Deterministic vs Probabilistic</div>
                <div class="lesson-text">
                    <strong>Deterministic analysis</strong> uses a single "best guess" for each input. You plug in one cost,
                    one benefit, and get one answer. It's simple but <strong>ignores uncertainty</strong>.<br><br>
                    <strong>Probabilistic analysis (PSA)</strong> acknowledges that you don't know the exact values.
                    Instead of one number, you give a <strong>range</strong> (low, base, high), and the computer
                    runs 1,000 simulations, each time randomly picking values from those ranges.<br><br>
                    Think of it this way:
                </div>
            </div>
            """, unsafe_allow_html=True)

            col1, col2 = st.columns(2)
            with col1:
                st.markdown("""
                <div class="example-box">
                    <strong>\U0001f4cc Deterministic:</strong><br>
                    "This tool costs $15,000 and saves $25,000."<br>
                    Net value = $10,000. Done.<br><br>
                    <em>But what if the cost is actually $20,000?<br>
                    Or savings are only $12,000?</em>
                </div>
                """, unsafe_allow_html=True)
            with col2:
                st.markdown("""
                <div class="example-box">
                    <strong>\U0001f3b2 Probabilistic:</strong><br>
                    "Cost is between $10K-$22K. Savings are between $15K-$35K."<br>
                    Run 1,000 scenarios. Result:<br>
                    <em>"82% chance this tool is worth it."</em><br><br>
                    Much more useful for decision-making!
                </div>
                """, unsafe_allow_html=True)

        elif "2." in lesson:
            st.markdown("""
            <div class="lesson-card">
                <div class="lesson-title">\U0001f4b0 Costs: What to Count</div>
                <div class="lesson-text">
                    When evaluating a digital health tool, count ALL costs:\n\n
                    <strong>Direct costs:</strong><br>
                    \u2022 Annual subscription / license fee<br>
                    \u2022 One-time implementation / setup<br>
                    \u2022 Hardware (tablets, kiosks, etc.)<br><br>
                    <strong>Indirect costs:</strong><br>
                    \u2022 Staff training time (hours \u00d7 wage)<br>
                    \u2022 Productivity loss during transition<br>
                    \u2022 IT support / maintenance<br><br>
                    <strong>Where to find this data:</strong><br>
                    \u2022 Vendor quote or contract<br>
                    \u2022 Your IT department estimate<br>
                    \u2022 HRSA UDS report (for patient volumes)<br>
                    \u2022 Payroll data (for staff wages)
                </div>
            </div>
            """, unsafe_allow_html=True)

            st.markdown("""
            <div class="formula-box">
                Total Annual Cost = Subscription + (Implementation \u00f7 3) + (Training Hours \u00d7 Wage)
            </div>
            """, unsafe_allow_html=True)

            st.markdown("""
            <div class="example-box">
                <strong>Example:</strong> Your CHC is considering a $15,000/year scheduling tool.<br>
                Implementation: $6,000 (amortized over 3 years = $2,000/year)<br>
                Training: 20 hours \u00d7 $25/hr = $500<br><br>
                <strong>Total Annual Cost = $15,000 + $2,000 + $500 = $17,500</strong>
            </div>
            """, unsafe_allow_html=True)

        elif "3." in lesson:
            st.markdown("""
            <div class="lesson-card">
                <div class="lesson-title">\U0001f4c8 Effectiveness: Measuring Benefits</div>
                <div class="lesson-text">
                    Benefits can be measured in different units:\n\n
                    <strong>Time savings:</strong> Staff hours freed up per week<br>
                    \u2022 Source: Workflow analysis, vendor case studies (discount by 30-50%)<br><br>
                    <strong>Recovered visits:</strong> Visits gained from reduced no-shows<br>
                    \u2022 Source: Your EHR no-show rate \u00d7 expected improvement<br><br>
                    <strong>Revenue recovered:</strong> Dollar value of recovered visits<br>
                    \u2022 Source: Average Medicaid reimbursement per visit<br><br>
                    <strong>QALYs (Quality-Adjusted Life Years):</strong> Used in pharma, rare in CHC evaluations
                </div>
            </div>
            """, unsafe_allow_html=True)

            st.markdown("""
            <div class="formula-box">
                Time Savings ($) = Hours Saved/Week \u00d7 Wage \u00d7 52 weeks<br><br>
                Recovered Visits = (No-Show Reduction %) \u00d7 Patients \u00d7 Visits/Patient/Year<br><br>
                Revenue Recovered = Recovered Visits \u00d7 Value per Visit
            </div>
            """, unsafe_allow_html=True)

            st.markdown("""
            <div class="example-box">
                <strong>Example:</strong><br>
                Hours saved: 8 hrs/week \u00d7 $25 \u00d7 52 = <strong>$10,400</strong><br>
                No-show reduction: 5% \u00d7 10,000 patients \u00d7 3 visits = 1,500 visits<br>
                Revenue: 1,500 \u00d7 $85 = <strong>$127,500</strong><br>
                Total benefit = $137,900
            </div>
            """, unsafe_allow_html=True)

        elif "4." in lesson:
            st.markdown("""
            <div class="lesson-card">
                <div class="lesson-title">\U0001f4b5 Net Monetary Benefit (NMB)</div>
                <div class="lesson-text">
                    NMB converts everything into dollars. It answers:<br>
                    <em>"After accounting for costs, how much monetary value does this tool create?"</em>
                </div>
            </div>
            """, unsafe_allow_html=True)

            st.markdown("""
            <div class="formula-box">
                NMB = (\u03bb \u00d7 \u0394E) \u2212 \u0394C<br><br>
                \u03bb = Willingness-to-pay per unit of effectiveness<br>
                \u0394E = Incremental effectiveness (e.g., visits gained)<br>
                \u0394C = Incremental cost (net of savings)
            </div>
            """, unsafe_allow_html=True)

            st.markdown("""
            <div class="example-box">
                <strong>Example:</strong><br>
                \u03bb (WTP) = $85 per visit gained<br>
                \u0394E = 1,500 recovered visits<br>
                \u0394C = $17,500 \u2212 $10,400 (time savings) = $7,100<br><br>
                NMB = ($85 \u00d7 1,500) \u2212 $7,100 = $127,500 \u2212 $7,100 = <strong>$120,400</strong><br><br>
                \u2705 Positive NMB = tool is worth adopting!
            </div>
            """, unsafe_allow_html=True)

        elif "5." in lesson:
            st.markdown("""
            <div class="lesson-card">
                <div class="lesson-title">\U0001f3e5 Net Health Benefit (NHB)</div>
                <div class="lesson-text">
                    NHB is the flip side of NMB. Instead of converting to dollars, it converts to <strong>health units</strong> (visits, QALYs, etc.).<br>
                    It answers: <em>"How many effective visits does this tool gain after deducting costs?"</em>
                </div>
            </div>
            """, unsafe_allow_html=True)

            st.markdown("""
            <div class="formula-box">
                NHB = \u0394E \u2212 (\u0394C \u00f7 \u03bb)<br><br>
                Same variables, just rearranged.
            </div>
            """, unsafe_allow_html=True)

            st.markdown("""
            <div class="example-box">
                <strong>Example:</strong><br>
                \u0394E = 1,500 visits<br>
                \u0394C = $7,100<br>
                \u03bb = $85/visit<br><br>
                NHB = 1,500 \u2212 ($7,100 \u00f7 $85) = 1,500 \u2212 83.5 = <strong>1,416.5 visits</strong><br><br>
                \u2705 Positive NHB = you gain more visits than the cost "eats up."
            </div>
            """, unsafe_allow_html=True)

        elif "6." in lesson:
            st.markdown("""
            <div class="lesson-card">
                <div class="lesson-title">\U0001f4ca ICER (Incremental Cost-Effectiveness Ratio)</div>
                <div class="lesson-text">
                    ICER tells you: <em>"How much extra cost per extra unit of effectiveness?"</em><br>
                    It's the most commonly reported metric in health economics.
                </div>
            </div>
            """, unsafe_allow_html=True)

            st.markdown("""
            <div class="formula-box">
                ICER = \u0394C \u00f7 \u0394E<br><br>
                If ICER < WTP \u2192 Cost-effective \u2705<br>
                If ICER > WTP \u2192 Not cost-effective \u274c
            </div>
            """, unsafe_allow_html=True)

            st.markdown("""
            <div class="example-box">
                <strong>Example:</strong><br>
                \u0394C = $7,100<br>
                \u0394E = 1,500 visits<br><br>
                ICER = $7,100 \u00f7 1,500 = <strong>$4.73 per visit gained</strong><br><br>
                If your WTP is $85/visit, then $4.73 << $85 \u2192 <strong>Highly cost-effective!</strong>
            </div>
            """, unsafe_allow_html=True)

        elif "7." in lesson:
            st.markdown("""
            <div class="lesson-card">
                <div class="lesson-title">\U0001f4c8 The Cost-Effectiveness Plane</div>
                <div class="lesson-text">
                    A scatter plot with 4 quadrants:\n\n
                    \u2022 <strong>Bottom-right (SE):</strong> More effective AND cheaper \u2192 DOMINANT (always adopt!) \U0001f389<br>
                    \u2022 <strong>Top-right (NE):</strong> More effective but costlier \u2192 Depends on WTP<br>
                    \u2022 <strong>Bottom-left (SW):</strong> Less effective but cheaper \u2192 Depends on WTP<br>
                    \u2022 <strong>Top-left (NW):</strong> Less effective AND costlier \u2192 DOMINATED (never adopt!) \u274c<br><br>
                    Each dot in the PSA scatter represents one of the 1,000 simulated scenarios.
                    If most dots are in the SE or NE below the WTP line, the tool is likely cost-effective.
                </div>
            </div>
            """, unsafe_allow_html=True)

        elif "8." in lesson:
            st.markdown("""
            <div class="lesson-card">
                <div class="lesson-title">\U0001f3b2 PSA (Probabilistic Sensitivity Analysis)</div>
                <div class="lesson-text">
                    PSA is the engine that powers everything. Here's what happens step by step:\n\n
                    <strong>Step 1:</strong> You provide low/base/high estimates for each uncertain input<br>
                    <strong>Step 2:</strong> The computer creates a probability distribution for each input (we use triangular)<br>
                    <strong>Step 3:</strong> It randomly draws one value from each distribution<br>
                    <strong>Step 4:</strong> It calculates NMB, ICER, etc. for that draw<br>
                    <strong>Step 5:</strong> Repeat 1,000 times<br>
                    <strong>Step 6:</strong> Report the average, the spread, and the probability of cost-effectiveness<br><br>
                    <em>Why 1,000?</em> It's enough to get stable probabilities. More iterations (5,000 or 10,000) are used in published analyses but 1,000 is standard for decision-making.
                </div>
            </div>
            """, unsafe_allow_html=True)

        elif "9." in lesson:
            st.markdown("""
            <div class="lesson-card">
                <div class="lesson-title">\U0001f4c9 CEAC (Cost-Effectiveness Acceptability Curve)</div>
                <div class="lesson-text">
                    The CEAC answers: <em>"At any given WTP, what is the probability this tool is cost-effective?"</em><br><br>
                    <strong>How it's built:</strong><br>
                    1. Pick a WTP value (e.g., $50)<br>
                    2. Calculate NMB for all 1,000 PSA iterations at that WTP<br>
                    3. Count how many are positive \u2192 That's your probability<br>
                    4. Repeat for every WTP from $0 to your maximum<br>
                    5. Plot as a curve<br><br>
                    <strong>Reading the CEAC:</strong><br>
                    \u2022 If the curve reaches 90%+ early, the tool is a strong bet<br>
                    \u2022 If it barely passes 50%, there's a coin-flip chance it's worth it<br>
                    \u2022 If it stays below 50%, the tool is probably not cost-effective
                </div>
            </div>
            """, unsafe_allow_html=True)

        elif "10." in lesson:
            st.markdown("""
            <div class="lesson-card">
                <div class="lesson-title">\U0001f52e EVPI (Expected Value of Perfect Information)</div>
                <div class="lesson-text">
                    EVPI answers: <em>"How much is it worth to eliminate ALL uncertainty before deciding?"</em><br><br>
                    In practical terms: <strong>Should you run a pilot study, or just go ahead and adopt/reject?</strong>
                </div>
            </div>
            """, unsafe_allow_html=True)

            st.markdown("""
            <div class="formula-box">
                EVPI = E[max(NMB, 0)] \u2212 max(E[NMB], 0)<br><br>
                E[max(NMB, 0)] = Average of "best possible decision in each scenario"<br>
                max(E[NMB], 0) = Best decision based on average data
            </div>
            """, unsafe_allow_html=True)

            st.markdown("""
            <div class="example-box">
                <strong>Example:</strong><br>
                Mean NMB = $50,000 (positive, so we'd adopt)<br>
                But some iterations are negative \u2192 sometimes we'd be wrong<br>
                EVPI = $3,200<br><br>
                <strong>Interpretation:</strong> If a pilot costs less than $3,200, it's worth running.
                If the pilot costs $10,000, just decide now \u2014 the information isn't worth the price.
            </div>
            """, unsafe_allow_html=True)

        elif "11." in lesson:
            st.markdown("""
            <div class="lesson-card">
                <div class="lesson-title">\U0001f4b5 Willingness-to-Pay (WTP)</div>
                <div class="lesson-text">
                    WTP (\u03bb) is the <strong>maximum amount your CHC would pay for one additional unit of effectiveness</strong>.<br><br>
                    <strong>In pharma:</strong> WTP = $50,000-$150,000 per QALY (used by ICER, NICE)<br><br>
                    <strong>In CHC digital health:</strong> Effectiveness is usually visits or hours, not QALYs. So:<br>
                    \u2022 If a recovered visit generates $85 in revenue \u2192 WTP \u2248 $85/visit<br>
                    \u2022 If saving a staff hour is worth $25 (their wage) \u2192 WTP \u2248 $25/hour<br><br>
                    <strong>There is no single "correct" WTP.</strong> That's why the CEAC shows results across a range.
                    Your leadership can look at the curve and say: "At our budget reality, is this likely worth it?"
                </div>
            </div>
            """, unsafe_allow_html=True)

        elif "12." in lesson:
            st.markdown("""
            <div class="lesson-card">
                <div class="lesson-title">\U0001f3af Putting It All Together</div>
                <div class="lesson-text">
                    Here's the full workflow for evaluating a digital health tool:\n\n
                    <strong>1. Gather data:</strong> Costs (vendor + internal), benefits (time savings + recovered visits)<br>
                    <strong>2. Deterministic check:</strong> Quick ROI and break-even (Pillar 1 in DECIDE)<br>
                    <strong>3. Set ranges:</strong> Low/base/high for each uncertain input<br>
                    <strong>4. Run PSA:</strong> 1,000 iterations with triangular distributions<br>
                    <strong>5. Calculate:</strong> NMB, NHB, ICER for each iteration<br>
                    <strong>6. Visualize:</strong> CE Plane, NMB histogram, CEAC<br>
                    <strong>7. Interpret EVPI:</strong> Is a pilot worth it?<br>
                    <strong>8. Decide:</strong> Adopt / Pilot / Reject<br><br>
                    DECIDE's Advanced Analysis module does steps 3-7 automatically.
                    You just provide the inputs!
                </div>
            </div>
            """, unsafe_allow_html=True)

    # ======================== QUIZ TAB ========================
    with tab_quiz:

        st.markdown('<div class="lesson-title" style="text-align:center; font-size:24px;">\U0001f9e0 Quiz Challenge</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="score-display">Score: {st.session_state["game_score"]} / {st.session_state["game_total"]}</div>', unsafe_allow_html=True)

        questions = [
            {
                "q": "What does NMB stand for?",
                "options": ["Net Monetary Benefit", "National Medical Board", "New Market Baseline", "Net Marginal Budget"],
                "answer": "Net Monetary Benefit",
                "explain": "NMB = (\u03bb \u00d7 \u0394E) \u2212 \u0394C. It converts all outcomes into dollars."
            },
            {
                "q": "If NMB is positive, what should you do?",
                "options": ["Reject the tool", "Adopt or pilot the tool", "Run more simulations", "Increase the budget"],
                "answer": "Adopt or pilot the tool",
                "explain": "Positive NMB means the tool's benefits exceed its costs at your WTP."
            },
            {
                "q": "What does PSA stand for?",
                "options": ["Patient Safety Assessment", "Probabilistic Sensitivity Analysis", "Primary Service Audit", "Public Spending Account"],
                "answer": "Probabilistic Sensitivity Analysis",
                "explain": "PSA runs 1,000+ simulations to account for uncertainty in your estimates."
            },
            {
                "q": "The CEAC shows:",
                "options": ["Total cost over time", "Probability of cost-effectiveness at different WTP values", "Staff satisfaction scores", "Revenue projections"],
                "answer": "Probability of cost-effectiveness at different WTP values",
                "explain": "CEAC = Cost-Effectiveness Acceptability Curve. At each WTP, it shows what % of simulations were cost-effective."
            },
            {
                "q": "EVPI tells you:",
                "options": ["The total cost of the tool", "How many staff you need", "The value of running a pilot before deciding", "The vendor's profit margin"],
                "answer": "The value of running a pilot before deciding",
                "explain": "EVPI = Expected Value of Perfect Information. If EVPI > pilot cost, run the pilot."
            },
            {
                "q": "A tool costs $20,000/year and saves $35,000/year. What is the deterministic net value?",
                "options": ["$55,000", "$15,000", "-$15,000", "$20,000"],
                "answer": "$15,000",
                "explain": "Net value = Benefits \u2212 Costs = $35,000 \u2212 $20,000 = $15,000"
            },
            {
                "q": "What does the SE quadrant of the CE Plane mean?",
                "options": ["More effective and cheaper (dominant)", "More effective but costlier", "Less effective and costlier (dominated)", "Less effective but cheaper"],
                "answer": "More effective and cheaper (dominant)",
                "explain": "SE = South-East = lower cost (south) + higher effectiveness (east). This is the best outcome!"
            },
            {
                "q": "In a triangular distribution, what do the three values represent?",
                "options": ["Mean, median, mode", "Low, base, high", "Cost, benefit, profit", "Min, max, average"],
                "answer": "Low, base, high",
                "explain": "Low = worst case, Base = most likely, High = best case. The distribution peaks at base."
            },
            {
                "q": "ICER = $4.73/visit. Your WTP = $85/visit. Is this tool cost-effective?",
                "options": ["Yes, ICER < WTP", "No, ICER > WTP", "Need more data", "Only with a pilot"],
                "answer": "Yes, ICER < WTP",
                "explain": "If ICER ($4.73) is below your WTP ($85), you're paying less per visit than you're willing to \u2192 cost-effective!"
            },
            {
                "q": "Which source would you use to find your CHC's patient volume?",
                "options": ["Vendor marketing brochure", "HRSA UDS Report", "Wikipedia", "Staff break room whiteboard"],
                "answer": "HRSA UDS Report",
                "explain": "The Uniform Data System (UDS) report is submitted annually to HRSA and contains official patient volume data."
            },
        ]

        if "quiz_indices" not in st.session_state:
            indices = list(range(len(questions)))
            random.shuffle(indices)
            st.session_state["quiz_indices"] = indices
        if "quiz_pos" not in st.session_state:
            st.session_state["quiz_pos"] = 0

        pos = st.session_state["quiz_pos"]

        if pos < len(questions):
            qi = st.session_state["quiz_indices"][pos]
            q = questions[qi]

            st.markdown(f"**Question {pos + 1} of {len(questions)}**")
            st.markdown(f"### {q['q']}")

            answer = st.radio("Select your answer:", q["options"], key=f"quiz_{pos}")

            if st.button("Submit Answer", key=f"submit_{pos}"):
                st.session_state["game_total"] += 1
                if answer == q["answer"]:
                    st.session_state["game_score"] += 1
                    st.success(f"\u2705 Correct! {q['explain']}")
                else:
                    st.error(f"\u274c Wrong. The answer is: **{q['answer']}**. {q['explain']}")
                st.session_state["quiz_pos"] += 1
                st.rerun()
        else:
            score = st.session_state["game_score"]
            total = st.session_state["game_total"]
            pct = (score / total * 100) if total > 0 else 0

            if pct >= 80:
                st.balloons()
                grade = "\U0001f3c6 Health Economics Expert!"
            elif pct >= 60:
                grade = "\U0001f4aa Getting There!"
            else:
                grade = "\U0001f4d6 Review the Lessons"

            st.markdown(f"""
            <div class="lesson-card" style="text-align:center;">
                <div style="font-size:48px; margin-bottom:10px;">\U0001f3af</div>
                <div class="score-display">Final Score: {score}/{total} ({pct:.0f}%)</div>
                <div style="font-family:'Times New Roman',serif; font-size:24px; color:#6D4C41;">{grade}</div>
            </div>
            """, unsafe_allow_html=True)

            if st.button("\U0001f504 Restart Quiz"):
                st.session_state["game_score"] = 0
                st.session_state["game_total"] = 0
                st.session_state["quiz_pos"] = 0
                indices = list(range(len(questions)))
                random.shuffle(indices)
                st.session_state["quiz_indices"] = indices
                st.rerun()

    # ======================== PRACTICE TAB ========================
    with tab_practice:

        st.markdown('<div class="lesson-title" style="text-align:center; font-size:24px;">\U0001f527 Practice Calculator</div>', unsafe_allow_html=True)
        st.markdown("""
        <div class="example-box" style="text-align:center;">
            Enter any values below and see NMB, NHB, and ICER calculated in real time.
            Use this to build intuition before running the real Advanced Analysis.
        </div>
        """, unsafe_allow_html=True)

        st.markdown("")
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("**Costs**")
            pr_cost = st.number_input("Annual tool cost ($)", min_value=0, value=15000, step=500, key="pr_cost")
            pr_impl = st.number_input("Implementation ($, amortized 3yr)", min_value=0, value=5000, step=500, key="pr_impl")
            pr_train = st.number_input("Training cost ($)", min_value=0, value=500, step=100, key="pr_train")
            pr_hours_saved = st.number_input("Staff hours saved/week", min_value=0.0, value=8.0, step=0.5, key="pr_hrs")
            pr_wage = st.number_input("Staff wage ($/hr)", min_value=0.0, value=25.0, step=1.0, key="pr_wage")

        with col2:
            st.markdown("**Benefits**")
            pr_ns = st.number_input("No-show reduction (pp)", min_value=0.0, value=5.0, step=0.5, key="pr_ns")
            pr_patients = st.number_input("Patients/year", min_value=0, value=10000, step=500, key="pr_pat")
            pr_vppy = st.number_input("Visits/patient/year", min_value=1, value=3, step=1, key="pr_vppy")
            pr_vpv = st.number_input("Value per visit ($)", min_value=0.0, value=85.0, step=5.0, key="pr_vpv")
            pr_wtp = st.number_input("Your WTP ($/visit)", min_value=0.0, value=85.0, step=5.0, key="pr_wtp")

        # Calculations
        total_cost = pr_cost + (pr_impl / 3) + pr_train
        time_savings = pr_hours_saved * pr_wage * 52
        visits_gained = (pr_ns / 100) * pr_patients * pr_vppy
        delta_c = total_cost - time_savings
        delta_e = visits_gained
        nmb_val = (pr_wtp * delta_e) - delta_c
        nhb_val = delta_e - (delta_c / pr_wtp) if pr_wtp > 0 else 0
        icer_val = delta_c / delta_e if delta_e > 0 else float('inf')
        net_simple = (time_savings + visits_gained * pr_vpv) - total_cost

        st.markdown("---")

        r1, r2, r3, r4 = st.columns(4)
        with r1:
            clr = "#2A9D8F" if nmb_val >= 0 else "#E76F51"
            st.markdown(f'<div class="stat-card"><div class="stat-label">NMB</div><div class="stat-number" style="color:{clr};">${nmb_val:,.0f}</div></div>', unsafe_allow_html=True)
        with r2:
            st.markdown(f'<div class="stat-card"><div class="stat-label">NHB (visits)</div><div class="stat-number">{nhb_val:,.1f}</div></div>', unsafe_allow_html=True)
        with r3:
            icer_text = f"${icer_val:,.2f}" if icer_val < 999999 else "N/A"
            st.markdown(f'<div class="stat-card"><div class="stat-label">ICER ($/visit)</div><div class="stat-number">{icer_text}</div></div>', unsafe_allow_html=True)
        with r4:
            clr2 = "#2A9D8F" if net_simple >= 0 else "#E76F51"
            st.markdown(f'<div class="stat-card"><div class="stat-label">Simple Net Value</div><div class="stat-number" style="color:{clr2};">${net_simple:,.0f}</div></div>', unsafe_allow_html=True)

        st.markdown("")
        ce_status = "\u2705 Cost-effective" if icer_val < pr_wtp else "\u274c Not cost-effective"
        st.markdown(f"""
        <div class="example-box" style="text-align:center;">
            <strong>ICER = ${icer_val:,.2f}/visit</strong> vs <strong>WTP = ${pr_wtp:,.2f}/visit</strong> \u2192 <strong>{ce_status}</strong>
        </div>
        """, unsafe_allow_html=True)