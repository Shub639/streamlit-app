import streamlit as st
import numpy as np
import plotly.graph_objects as go

def render_advanced_analysis():

    st.markdown('<h1 style="text-align:center;">🧾 Advanced Health Economic Analysis</h1>', unsafe_allow_html=True)
    st.markdown('<p style="text-align:center;">PSA (1,000 iterations) • CE Plane • NMB • NHB • CEAC • EVPI</p>', unsafe_allow_html=True)
    st.markdown("---")

    # ========== COST INPUTS ==========
    st.markdown("### 💰 Cost Inputs (low / base / high)")
    c1, c2, c3 = st.columns(3)
    with c1:
        cost_low = st.number_input("Annual cost LOW ($)", min_value=0, value=10000, step=500)
        impl_low = st.number_input("Implementation LOW ($)", min_value=0, value=3000, step=500)
    with c2:
        cost_base = st.number_input("Annual cost BASE ($)", min_value=0, value=15000, step=500)
        impl_base = st.number_input("Implementation BASE ($)", min_value=0, value=5000, step=500)
    with c3:
        cost_high = st.number_input("Annual cost HIGH ($)", min_value=0, value=22000, step=500)
        impl_high = st.number_input("Implementation HIGH ($)", min_value=0, value=8000, step=500)
    with st.expander("ℹ️ Info on Cost Inputs"):
        st.markdown("""
        **Annual cost**: Total yearly operating costs of the intervention (staff, software, equipment).  
        **Implementation cost**: One-time setup costs (training, IT setup, onboarding).  

        **Source**: invoices, budgets, vendor quotes, IT/training dept.  
        **Calculation**: Sum relevant costs; amortize implementation over expected lifespan (e.g., 3 years).  
        **Use**: Used in PSA to calculate incremental cost versus time-savings or other benefits.
        """)

    # ========== BENEFIT INPUTS ==========
    st.markdown("### ⚡ Benefit Inputs (low / base / high)")
    b1, b2, b3 = st.columns(3)
    with b1:
        hours_low = st.number_input("Hours saved/wk LOW", min_value=0.0, value=3.0, step=0.5)
        ns_low = st.number_input("No-show reduction LOW (pp)", min_value=0.0, value=2.0, step=0.5)
    with b2:
        hours_base = st.number_input("Hours saved/wk BASE", min_value=0.0, value=8.0, step=0.5)
        ns_base = st.number_input("No-show reduction BASE (pp)", min_value=0.0, value=5.0, step=0.5)
    with b3:
        hours_high = st.number_input("Hours saved/wk HIGH", min_value=0.0, value=14.0, step=0.5)
        ns_high = st.number_input("No-show reduction HIGH (pp)", min_value=0.0, value=10.0, step=0.5)
    with st.expander("ℹ️ Info on Benefit Inputs"):
        st.markdown("""
        **Hours saved/wk**: Estimated reduction in staff time per week.  
        **No-show reduction**: Expected percentage reduction in patient no-shows.  

        **Source**: Observational data, pilot studies, literature review.  
        **Calculation**: Use historical data or estimate improvements from similar interventions.  
        **Use**: Determines incremental effectiveness (delta E) in the PSA.
        """)

    # ========== FIXED PARAMETERS ==========
    st.markdown("### 🛠 Fixed Parameters")
    f1, f2, f3, f4 = st.columns(4)
    with f1:
        wage = st.number_input("Staff wage ($/hr)", min_value=0.0, value=25.0, step=1.0)
    with f2:
        patients = st.number_input("Patients/year", min_value=0, value=10000, step=500)
    with f3:
        vppy = st.number_input("Visits/patient/yr", min_value=1, value=3, step=1)
    with f4:
        vpv = st.number_input("Value per visit ($)", min_value=0.0, value=85.0, step=5.0)
    with st.expander("ℹ️ Info on Fixed Parameters"):
        st.markdown("""
        **Staff wage**: Cost per hour of staff performing the intervention.  
        **Patients/year**: Total number of patients expected per year.  
        **Visits/patient/yr**: Average annual visits per patient.  
        **Value per visit**: Monetary value assigned to each visit.  

        **Source**: HR/payroll data, hospital records, literature benchmarks.  
        **Use**: Needed to calculate cost offsets from time saved and incremental effectiveness.
        """)

    # ========== WTP RANGE ==========
    st.markdown("### 💵 Willingness-to-Pay Range ($ per visit gained)")
    w1, w2, w3 = st.columns(3)
    with w1:
        wtp_min = st.number_input("Min WTP ($)", min_value=0.0, value=0.0, step=50.0)
    with w2:
        wtp_max = st.number_input("Max WTP ($)", min_value=1.0, value=500.0, step=50.0)
    with w3:
        wtp_point = st.number_input("Point WTP for NMB/EVPI ($)", min_value=0.0, value=85.0, step=5.0)
    with st.expander("ℹ️ Info on Willingness-to-Pay"):
        st.markdown("""
        **Definition**: Maximum amount society is willing to pay per additional visit gained.  

        **Source**: Health economic literature or decision-maker guidance.  
        **Use**: Determines NMB, NHB, CEAC, and EVPI in the analysis.  
        Adjust WTP range to explore cost-effectiveness under different thresholds.
        """)

    # ========== CONFIDENCE ==========
    st.markdown("### 🎯 Confidence in Benefit Estimates (%)")
    confidence = st.slider("Confidence in your expected benefits", 0, 100, 100, step=5)
    with st.expander("ℹ️ Info on Confidence Input"):
        st.markdown("""
        **Definition**: How confident you are in the estimated benefits.  
        **Use**: Scales the incremental effectiveness (delta E) to account for uncertainty.  
        **0%** = no confidence, **100%** = fully confident.
        """)

    st.markdown("---")

    # ========== RUN PSA ==========
    if st.button("🚀 Run PSA (1,000 iterations)"):
        n_iter = 1000
        np.random.seed(42)

        # Triangular distributions
        sim_cost = np.random.triangular(cost_low, cost_base, cost_high, n_iter)
        sim_impl = np.random.triangular(impl_low, impl_base, impl_high, n_iter)
        sim_hours = np.random.triangular(hours_low, hours_base, hours_high, n_iter)
        sim_ns = np.random.triangular(ns_low, ns_base, ns_high, n_iter)

        # Total cost
        total_cost = sim_cost + (sim_impl / 3.0)

        # Incremental effectiveness
        delta_e = (sim_ns / 100.0) * patients * vppy
        delta_e *= confidence / 100.0

        # Time savings
        time_offset = sim_hours * wage * 52
        delta_c = total_cost - time_offset

        # NMB & NHB
        nmb = (wtp_point * delta_e) - delta_c
        mean_nmb = float(np.mean(nmb))
        nhb = delta_e - (delta_c / wtp_point if wtp_point > 0 else delta_c)
        mean_nhb = float(np.mean(nhb))
        p_ce = float(np.mean(nmb > 0))

        # CEAC
        wtp_range = np.linspace(wtp_min, wtp_max, 200)
        ceac = [float(np.mean((w * delta_e - delta_c) > 0)) for w in wtp_range]

        # EVPI
        evpi = float(np.mean(np.maximum(nmb, 0.0)) - max(mean_nmb, 0.0))

        # ICER
        mask = delta_e > 0
        icer_arr = np.where(mask, delta_c / delta_e, np.nan)
        median_icer = float(np.nanmedian(icer_arr))

        # ===== DISPLAY METRICS =====
        st.markdown("---")
        m1, m2, m3, m4 = st.columns(4)
        with m1:
            clr = "#2A9D8F" if mean_nmb >= 0 else "#E76F51"
            st.markdown(f"**Mean NMB:** ${mean_nmb:,.0f}", unsafe_allow_html=True)
        with m2:
            st.markdown(f"**Prob Cost-Effective:** {p_ce*100:.0f}%", unsafe_allow_html=True)
        with m3:
            st.markdown(f"**Mean NHB (visits):** {mean_nhb:,.1f}", unsafe_allow_html=True)
        with m4:
            st.markdown(f"**EVPI:** ${evpi:,.0f}", unsafe_allow_html=True)

        # ===== CE Plane =====
        fig_plane = go.Figure()
        fig_plane.add_trace(go.Scatter(x=delta_e, y=delta_c, mode="markers",
                                       marker=dict(size=5, color="rgba(196,168,130,0.55)"), name="Simulated outcomes"))
        fig_plane.add_trace(go.Scatter(x=[float(np.mean(delta_e))], y=[float(np.mean(delta_c))],
                                       mode="markers", marker=dict(size=14, color="#E76F51", symbol="x",
                                                                   line=dict(width=2, color="#3E2723")), name="Mean"))
        fig_plane.update_layout(xaxis_title="Incremental effectiveness (visits gained)",
                                yaxis_title="Incremental cost ($, net of time savings)",
                                height=420, paper_bgcolor="rgba(0,0,0,0)",
                                plot_bgcolor="rgba(251,247,242,0.6)")
        st.plotly_chart(fig_plane, use_container_width=True)
        with st.expander("ℹ️ How to interpret CE Plane"):
            st.markdown("""
            **X-axis:** Incremental effectiveness (visits gained)  
            **Y-axis:** Incremental cost ($)  
            **Interpretation:** Points in the **bottom right quadrant** = cost-saving and more effective.  
            **Top right quadrant** = more effective but more costly (evaluate ICER).  
            **Mean point:** expected average outcome.
            """)

        # ===== NMB Histogram =====
        fig_nmb = go.Figure()
        fig_nmb.add_trace(go.Histogram(x=nmb, nbinsx=50, marker_color="rgba(196,168,130,0.7)",
                                       marker_line=dict(color="#6D4C41", width=1)))
        fig_nmb.add_vline(x=0, line_dash="dash", line_color="#E76F51",
                          annotation_text="Break-even", annotation_position="top")
        fig_nmb.update_layout(xaxis_title="Net Monetary Benefit ($)", yaxis_title="Frequency",
                              height=380, paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(251,247,242,0.6)")
        st.plotly_chart(fig_nmb, use_container_width=True)
        with st.expander("ℹ️ How to interpret NMB Histogram"):
            st.markdown("""
            **X-axis:** NMB values across PSA iterations  
            **Y-axis:** Frequency of simulations  
            **Interpretation:**  
            - Most values **>0** → likely cost-effective  
            - Values **<0** → not cost-effective  
            - Break-even line indicates where benefit equals cost.
            """)

        # ===== CEAC =====
        fig_ceac = go.Figure()
        fig_ceac.add_trace(go.Scatter(x=wtp_range, y=[p*100 for p in ceac], mode="lines",
                                      line=dict(color="#6D4C41", width=3),
                                      fill="tozeroy", fillcolor="rgba(196,168,130,0.2)"))
        fig_ceac.add_hline(y=50, line_dash="dot", line_color="#888",
                           annotation_text="50% threshold", annotation_position="bottom right")
        fig_ceac.update_layout(xaxis_title="Willingness-to-pay ($ per visit gained)",
                               yaxis_title="Probability cost-effective (%)",
                               yaxis=dict(range=[0, 105]),
                               height=380, paper_bgcolor="rgba(0,0,0,0)",
                               plot_bgcolor="rgba(251,247,242,0.6)")
        st.plotly_chart(fig_ceac, use_container_width=True)
        with st.expander("ℹ️ How to interpret CEAC"):
            st.markdown("""
            **X-axis:** WTP thresholds ($ per visit)  
            **Y-axis:** Probability intervention is cost-effective  
            **Interpretation:**  
            - At a given WTP, the curve shows the **chance intervention is cost-effective**.  
            - Steeper curves indicate more uncertainty.  
            - Use to justify decision-making thresholds.
            """)

        # ===== Summary Card =====
        st.markdown(f"""
        ### 📊 Analysis Summary
        - **Iterations:** {n_iter} Monte Carlo
        - **Distributions:** Triangular (low/base/high)
        - **Confidence applied:** {confidence}%
        - **Mean NMB:** ${mean_nmb:,.0f}
        - **Mean NHB:** {mean_nhb:,.1f} visits
        - **Prob cost-effective at WTP=${wtp_point:,.0f}:** {p_ce*100:.0f}%
        - **EVPI:** ${evpi:,.0f}
        - **Median ICER:** ${median_icer:,.0f}/visit
        """)