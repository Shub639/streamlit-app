import streamlit as st
from datetime import datetime
from fpdf import FPDF


def generate_report_pdf():
    tool_name = st.session_state.get("tool_name", "Unknown Tool")
    if not tool_name:
        tool_name = "Unknown Tool"

    p1 = st.session_state.get("p1_score", "N/A")
    p2 = st.session_state.get("p2_score", "N/A")
    p3 = st.session_state.get("p3_score", "N/A")
    p4 = st.session_state.get("p4_score", "N/A")
    p5 = st.session_state.get("p5_score", "N/A")
    screening = st.session_state.get("screening", ["N/A"] * 5)

    weights = {
        "Cost & Value": 0.25,
        "Staff Readiness": 0.20,
        "Patient Trust & Equity": 0.25,
        "Privacy & Security": 0.15,
        "Sustainability": 0.15,
    }

    try:
        scores = {
            "Cost & Value": float(p1),
            "Staff Readiness": float(p2),
            "Patient Trust & Equity": float(p3),
            "Privacy & Security": float(p4),
            "Sustainability": float(p5),
        }
        overall = sum(scores[k] * weights[k] for k in weights) / 5 * 100
    except (ValueError, TypeError):
        overall = 0
        scores = {k: 0 for k in weights}

    if overall >= 70:
        verdict = "ADOPT"
        verdict_detail = "The tool scores well across all five pillars. The evidence supports moving forward with adoption."
    elif overall >= 45:
        verdict = "PILOT WITH CONDITIONS"
        verdict_detail = "The tool shows promise but has gaps in one or more pillars. Run a 3-6 month pilot before full commitment."
    else:
        verdict = "DO NOT ADOPT"
        verdict_detail = "Significant weaknesses across multiple pillars. The risks outweigh potential benefits at this time."

    now = datetime.now().strftime("%B %d, %Y at %I:%M %p")

    # Build PDF
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=20)

    # ---- Cover Page ----
    pdf.add_page()
    pdf.set_fill_color(62, 39, 35)
    pdf.rect(0, 0, 210, 297, "F")
    pdf.set_text_color(196, 168, 130)
    pdf.set_font("Times", "B", 48)
    pdf.ln(80)
    pdf.cell(0, 20, "DECIDE", align="C", new_x="LMARGIN", new_y="NEXT")
    pdf.set_font("Times", "", 14)
    pdf.set_text_color(220, 200, 170)
    pdf.cell(0, 10, "Digital Evaluation for Community Implementation Decisions", align="C", new_x="LMARGIN", new_y="NEXT")
    pdf.ln(20)
    pdf.set_draw_color(196, 168, 130)
    pdf.set_line_width(0.5)
    pdf.line(60, pdf.get_y(), 150, pdf.get_y())
    pdf.ln(20)
    pdf.set_font("Times", "B", 18)
    pdf.set_text_color(255, 255, 255)
    pdf.cell(0, 10, "EVALUATION REPORT", align="C", new_x="LMARGIN", new_y="NEXT")
    pdf.ln(10)
    pdf.set_font("Times", "", 14)
    pdf.cell(0, 8, f"Tool: {tool_name}", align="C", new_x="LMARGIN", new_y="NEXT")
    pdf.cell(0, 8, f"Generated: {now}", align="C", new_x="LMARGIN", new_y="NEXT")
    pdf.ln(40)
    pdf.set_font("Times", "I", 12)
    pdf.set_text_color(196, 168, 130)
    pdf.cell(0, 8, '"Before you adopt, evaluate."', align="C", new_x="LMARGIN", new_y="NEXT")

    # ---- Helper functions ----
    def section_header(title):
        pdf.set_font("Times", "B", 16)
        pdf.set_text_color(62, 39, 35)
        pdf.ln(6)
        pdf.cell(0, 10, title, new_x="LMARGIN", new_y="NEXT")
        pdf.set_draw_color(196, 168, 130)
        pdf.set_line_width(0.4)
        pdf.line(pdf.l_margin, pdf.get_y(), 190, pdf.get_y())
        pdf.ln(4)

    def body_text(text):
        pdf.set_font("Times", "", 11)
        pdf.set_text_color(60, 60, 60)
        pdf.multi_cell(0, 6, text)
        pdf.ln(2)

    def bold_line(label, value):
        pdf.set_font("Times", "B", 11)
        pdf.set_text_color(62, 39, 35)
        pdf.cell(55, 7, label, new_x="END", new_y="TOP")
        pdf.set_font("Times", "", 11)
        pdf.set_text_color(60, 60, 60)
        pdf.cell(0, 7, str(value), new_x="LMARGIN", new_y="NEXT")

    # ---- Page 2: Executive Summary ----
    pdf.add_page()
    section_header("1. EXECUTIVE SUMMARY")
    bold_line("Tool Evaluated:", tool_name)
    bold_line("Overall Score:", f"{overall:.0f} / 100")
    bold_line("Recommendation:", verdict)
    pdf.ln(4)
    body_text(verdict_detail)

    # ---- Screening ----
    section_header("2. QUICK SCREENING RESULTS")
    screening_labels = [
        "HIPAA BAA provided",
        "Works on mobile / low-bandwidth",
        "Supports patient languages",
        "Free trial / pilot available",
        "No additional staff needed",
    ]
    for i, label in enumerate(screening_labels):
        answer = screening[i] if i < len(screening) else "N/A"
        icon = "[PASS]" if answer == "Yes" else "[FAIL]" if answer == "No" else "[????]"
        pdf.set_font("Times", "", 11)
        pdf.set_text_color(60, 60, 60)
        pdf.cell(0, 6, f"  {icon}  {label}: {answer}", new_x="LMARGIN", new_y="NEXT")

    no_count = screening.count("No") if isinstance(screening, list) else 0
    pdf.ln(3)
    if no_count >= 2:
        pdf.set_font("Times", "B", 11)
        pdf.set_text_color(200, 50, 50)
        pdf.cell(0, 7, "  ALERT: Multiple deal-breakers detected.", new_x="LMARGIN", new_y="NEXT")
    elif no_count == 1:
        pdf.set_font("Times", "B", 11)
        pdf.set_text_color(180, 130, 0)
        pdf.cell(0, 7, "  WARNING: One deal-breaker flagged.", new_x="LMARGIN", new_y="NEXT")
    else:
        pdf.set_font("Times", "B", 11)
        pdf.set_text_color(42, 157, 143)
        pdf.cell(0, 7, "  No deal-breakers found.", new_x="LMARGIN", new_y="NEXT")

    # ---- Pillar Scores Table ----
    section_header("3. FIVE-PILLAR EVALUATION")

    # Table header
    pdf.set_font("Times", "B", 11)
    pdf.set_fill_color(196, 168, 130)
    pdf.set_text_color(255, 255, 255)
    pdf.cell(70, 8, "Pillar", border=1, fill=True, new_x="END", new_y="TOP")
    pdf.cell(25, 8, "Score", border=1, fill=True, align="C", new_x="END", new_y="TOP")
    pdf.cell(25, 8, "Weight", border=1, fill=True, align="C", new_x="END", new_y="TOP")
    pdf.cell(50, 8, "Status", border=1, fill=True, align="C", new_x="LMARGIN", new_y="NEXT")

    pdf.set_font("Times", "", 11)
    for name, weight in weights.items():
        s = scores.get(name, 0)
        status = "Strong" if s >= 4 else "Moderate" if s >= 3 else "Weak"
        if s >= 4:
            pdf.set_text_color(42, 157, 143)
        elif s >= 3:
            pdf.set_text_color(180, 130, 0)
        else:
            pdf.set_text_color(231, 111, 81)
        pdf.cell(70, 7, f"  {name}", border=1, new_x="END", new_y="TOP")
        pdf.cell(25, 7, f"{s}/5", border=1, align="C", new_x="END", new_y="TOP")
        pdf.set_text_color(60, 60, 60)
        pdf.cell(25, 7, f"{int(weight*100)}%", border=1, align="C", new_x="END", new_y="TOP")
        if s >= 4:
            pdf.set_text_color(42, 157, 143)
        elif s >= 3:
            pdf.set_text_color(180, 130, 0)
        else:
            pdf.set_text_color(231, 111, 81)
        pdf.cell(50, 7, status, border=1, align="C", new_x="LMARGIN", new_y="NEXT")

    pdf.set_text_color(62, 39, 35)
    pdf.set_font("Times", "B", 12)
    pdf.ln(3)
    pdf.cell(0, 8, f"  Weighted Overall Score: {overall:.0f} / 100", new_x="LMARGIN", new_y="NEXT")

    # ---- Recommendations ----
    pdf.add_page()
    section_header("4. PILLAR DETAILS & RECOMMENDATIONS")

    recs = {
        "Cost & Value": {
            "weak": "The financial case is weak. Request itemized cost breakdowns from the vendor. Get independent ROI estimates. Re-run the evaluation with conservative numbers. Consider negotiating pricing or phased implementation.",
            "ok": "The financial model shows positive returns. Validate assumptions during a pilot period.",
        },
        "Staff Readiness": {
            "weak": "Your team may struggle to adopt this tool. Conduct staff surveys on current workload and burnout. Involve frontline staff in the evaluation. Ensure the vendor provides comprehensive onboarding and plan for a transition period.",
            "ok": "Staff capacity appears adequate. Monitor adoption rates and workflow impact during the first 90 days.",
        },
        "Patient Trust & Equity": {
            "weak": "Equity gaps may exclude vulnerable patients. Request bias/fairness audit data from the vendor. Verify language support. Test accessibility across digital literacy levels. Consult your patient advisory board. Reference: Obermeyer et al. (Science, 2019).",
            "ok": "The tool appears to serve patients equitably. Continue monitoring for disparate impact after implementation.",
        },
        "Privacy & Security": {
            "weak": "CRITICAL: Do NOT proceed until privacy concerns are resolved. Obtain a signed HIPAA BAA. Verify data storage and encryption. Confirm data deletion capabilities. Determine if vendor uses patient data for AI training. Reference: Privacy by Design (Cavoukian).",
            "ok": "Privacy posture is adequate. Ensure BAA is reviewed annually and conduct periodic security assessments.",
        },
        "Sustainability": {
            "weak": "High risk of abandonment. Develop a sustainability plan beyond initial funding. Negotiate contract flexibility. Ensure data portability. Evaluate vendor financial stability. Reference: NASSS Framework (Greenhalgh et al., 2017).",
            "ok": "The tool appears sustainable for long-term use. Review annually and maintain an exit strategy.",
        },
    }

    for name in weights:
        s = scores.get(name, 0)
        pdf.set_font("Times", "B", 12)
        pdf.set_text_color(62, 39, 35)
        status_label = "ACTION NEEDED" if s < 3 else "ACCEPTABLE"
        pdf.cell(0, 8, f"{name} - {status_label}", new_x="LMARGIN", new_y="NEXT")
        text = recs[name]["weak"] if s < 3 else recs[name]["ok"]
        body_text(text)
        pdf.ln(2)

    # ---- Methodology ----
    section_header("5. METHODOLOGY")
    body_text(
        "This evaluation was conducted using DECIDE (Digital Evaluation for Community "
        "Implementation Decisions), a structured framework grounded in:\n\n"
        "  - Health economic evaluation (Net Monetary Benefit)\n"
        "  - Implementation science (CFIR framework)\n"
        "  - Algorithmic fairness (HEAL framework, Aequitas)\n"
        "  - Privacy by Design (Cavoukian, 7 principles)\n"
        "  - Sustainability science (NASSS framework)\n\n"
        "Pillar weights reflect the priorities of Community Health Centers (CHCs/FQHCs) "
        "serving underserved populations.\n\n"
        "Scoring: Each pillar is scored 1-5 based on structured questions. "
        "Weights: Cost & Value (25%), Patient Trust & Equity (25%), Staff Readiness (20%), "
        "Privacy & Security (15%), Sustainability (15%). "
        "Overall score is a weighted composite (0-100).\n\n"
        "Decision Thresholds: >= 70 ADOPT | 45-69 PILOT WITH CONDITIONS | < 45 DO NOT ADOPT"
    )

    # ---- Disclaimer ----
    section_header("6. DISCLAIMER")
    body_text(
        "This report is generated by DECIDE, a decision-support tool developed for the "
        "Hack the Health Gap Hackathon 2026. It is intended to inform, not replace, "
        "organizational decision-making. All scores are based on user-provided estimates "
        "and should be validated with actual operational data."
    )

    # ---- Footer on cover ----
    pdf.ln(10)
    pdf.set_font("Times", "I", 10)
    pdf.set_text_color(150, 150, 150)
    pdf.cell(0, 6, 'Report generated by DECIDE  |  "Before you adopt, evaluate."', align="C", new_x="LMARGIN", new_y="NEXT")

    return bytes(pdf.output())