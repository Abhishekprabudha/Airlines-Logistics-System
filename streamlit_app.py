from datetime import datetime
import streamlit as st

from app.services.airline_repo import AirlineLogisticsRepository
from app.utils.auth import login_panel
from app.utils.kpi import kpi_card, badge
from app.utils.styles import inject_styles

st.set_page_config(page_title="Airline Logistics AI System", page_icon="✈️", layout="wide")
inject_styles()
repo = AirlineLogisticsRepository()

if "authenticated" not in st.session_state:
    st.session_state.authenticated = False
if "actions" not in st.session_state:
    st.session_state.actions = []

if not st.session_state.authenticated:
    login_panel()
    st.stop()

st.sidebar.title("✈️ Airline Logistics AI")
st.sidebar.caption("Cargo • Baggage • People • Gen BI • SLA")
page = st.sidebar.radio(
    "Navigate",
    [
        "Overview Control Tower",
        "Cargo Vision AI",
        "Baggage Vision AI",
        "Workforce Safety",
        "Incident Prevention",
        "Simulation Engine",
        "Gen BI Agent",
        "SLA Cockpit",
        "System Architecture",
    ],
)

summary = repo.get_overview_summary()


def record_action(label: str):
    if st.button(f"Record action: {label}"):
        st.session_state.actions.append({"Action": label, "Time": datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")})
        st.success(f"Recorded: {label}")


def hero(title: str, subtitle: str):
    st.markdown(f"""
    <div class='hero-card'>
      <div class='hero-title'>{title}</div>
      <div class='hero-sub'>{subtitle}</div>
    </div>
    """, unsafe_allow_html=True)


if page == "Overview Control Tower":
    hero("The Invisible Airline Nervous System", "A real-time command layer that sees cargo, baggage, people, safety and SLA risk before incidents become operational failure.")
    c1, c2, c3, c4, c5, c6 = st.columns(6)
    with c1: kpi_card("Active Flights", summary["active_flights"], "Live monitored")
    with c2: kpi_card("Critical Risks", summary["critical_risks"], "Immediate action")
    with c3: kpi_card("Cargo Events", summary["cargo_damages"], "Vision detections")
    with c4: kpi_card("Baggage Events", summary["baggage_events"], "Passenger bags")
    with c5: kpi_card("Avg PPE", summary["avg_ppe"], "Safety compliance")
    with c6: kpi_card("Predicted SLA", summary["sla_prediction"], "Next 2 hours")

    left, right = st.columns([1.1, 1])
    with left:
        st.subheader("Live Flight Risk Board")
        st.dataframe(repo.flights_table(), use_container_width=True, hide_index=True)
        st.plotly_chart(repo.flight_risk_figure(), use_container_width=True)
    with right:
        st.subheader("Live AI Alerts")
        for a in repo.get_alerts():
            cls = "alert-high" if a["level"] == "high" else "alert-med"
            st.markdown(f"<div class='{cls}'><b>{a['title']}</b><br>{a['message']}</div>", unsafe_allow_html=True)
        st.subheader("Recorded Operator Actions")
        if st.session_state.actions:
            st.dataframe(st.session_state.actions[-5:], use_container_width=True, hide_index=True)
        else:
            st.info("No operator actions recorded yet.")

elif page == "Cargo Vision AI":
    hero("Cargo Damage Intelligence", "Computer vision inspects cargo boxes, ULDs and pallets for dents, crushed corners, seal anomalies, tears and water marks.")
    c1, c2, c3 = st.columns(3)
    with c1: kpi_card("Detected Cargo Events", len(repo.cargo_table()), "Last 2 hours")
    with c2: kpi_card("High Severity", int((repo.cargo_table()["Severity"] == "High").sum()), "Auto-held")
    with c3: kpi_card("Top Confidence", f"{repo.cargo_table()['Confidence %'].max()}%", "Vision model")
    st.markdown(badge("Crushed corner") + badge("Seal anomaly") + badge("Surface tear") + badge("Water mark"), unsafe_allow_html=True)
    st.subheader("Camera AI Event Log")
    st.dataframe(repo.cargo_table(), use_container_width=True, hide_index=True)
    st.info("Demo video placeholder: insert broken/crushed box conveyor footage here and overlay red bounding boxes, severity score, timestamp and linked flight ID.")
    record_action("Route high-severity cargo to inspection lane")

elif page == "Baggage Vision AI":
    hero("Passenger Baggage Protection", "AI detects cracked shells, broken wheels, open zippers, torn handles and strap entanglement before loading or passenger claim escalation.")
    c1, c2, c3 = st.columns(3)
    with c1: kpi_card("Baggage Events", len(repo.baggage_table()), "Live detections")
    with c2: kpi_card("High Severity", int((repo.baggage_table()["Severity"] == "High").sum()), "Needs intervention")
    with c3: kpi_card("Best Confidence", f"{repo.baggage_table()['Confidence %'].max()}%", "Damage model")
    st.markdown(badge("Cracked shell") + badge("Open zipper") + badge("Broken wheel") + badge("Handle tear"), unsafe_allow_html=True)
    st.subheader("Baggage Damage Evidence Register")
    st.dataframe(repo.baggage_table(), use_container_width=True, hide_index=True)
    st.info("Demo video placeholder: insert baggage belt / carousel footage here and overlay cracked shell, broken handle, open zipper or broken wheel detection graphics.")
    record_action("Create proactive baggage service recovery note")

elif page == "Workforce Safety":
    hero("People Productivity & Safety Compliance", "Track team flow, people count, PPE compliance, zone congestion, productivity and unsafe proximity risk across ramp and warehouse zones.")
    c1, c2, c3 = st.columns(3)
    with c1: kpi_card("Monitored Zones", len(repo.workforce_table()), "Ramp + warehouse")
    with c2: kpi_card("Avg PPE", summary["avg_ppe"], "Live compliance")
    with c3: kpi_card("Critical Zones", int((repo.workforce_table()["State"] == "Critical").sum()), "Supervisor action")
    st.plotly_chart(repo.workforce_figure(), use_container_width=True)
    st.subheader("People Intelligence by Zone")
    st.dataframe(repo.workforce_table(), use_container_width=True, hide_index=True)
    st.warning("Position this as safety-first workforce intelligence, not surveillance. The system helps supervisors support teams before incidents occur.")
    record_action("Send supervisor alert to Ramp Zone 4")

elif page == "Incident Prevention":
    hero("Real-Time Incident Prevention", "The system correlates camera signals, cargo damage, baggage exceptions, workforce safety and SLA clocks into one operational risk score.")
    c1, c2 = st.columns([1, 1])
    with c1:
        st.subheader("Active Risk Correlation")
        st.dataframe(repo.incident_table(), use_container_width=True, hide_index=True)
    with c2:
        st.plotly_chart(repo.risk_funnel_figure(), use_container_width=True)
    st.markdown("""
    <div class='module-card'>
    <div class='small-label'>AI reasoning example</div>
    A damaged cargo box, Belt-06 congestion and a Ramp Zone 4 PPE exception are not isolated events. Combined, they raise the probability of SLA breach for AI-274 and AI-191. The system recommends workforce redeployment and inspection-lane routing before the SLA breach occurs.
    </div>
    """, unsafe_allow_html=True)
    record_action("Accept recommended corrective action")

elif page == "Simulation Engine":
    hero("Simulation Before Execution", "Test corrective actions before deployment and choose the action with the highest SLA recovery and lowest residual risk.")
    st.subheader("Corrective Action Scenarios")
    st.dataframe(repo.simulation_table(), use_container_width=True, hide_index=True)
    scenario = st.selectbox("Choose a scenario to simulate", repo.simulation_table()["Scenario"].tolist())
    row = repo.simulation_table()[repo.simulation_table()["Scenario"] == scenario].iloc[0]
    c1, c2, c3 = st.columns(3)
    with c1: kpi_card("Predicted Outcome", row["Ranking"], row["Predicted Outcome"])
    with c2: kpi_card("SLA Buffer", f"{row['SLA Buffer Min']} min", "After action")
    with c3: kpi_card("Residual Risk", f"{row['Residual Risk %']}%", "Post-simulation")
    if row["Ranking"] == "Best":
        st.success("Recommended: execute this action. It gives the highest SLA recovery impact for AI-274.")
    else:
        st.info("Useful scenario, but compare against the best-ranked option before execution.")
    record_action(f"Simulated: {scenario}")

elif page == "Gen BI Agent":
    hero("Conversational Gen BI Agent", "Ask natural-language questions across cargo, baggage, workforce, camera AI, incidents, simulations and SLA data.")
    default_q = "What is the current baggage delay risk for Flight AI-274?"
    question = st.text_input("Ask the Gen BI Agent", value=default_q)
    result = repo.gen_bi_answer(question)
    st.markdown(f"""
    <div class='module-card'>
    <div class='small-label'>Gen BI answer</div>
    {result['answer']}
    </div>
    """, unsafe_allow_html=True)
    cols = st.columns(len(result["cards"]))
    for col, (title, val) in zip(cols, result["cards"]):
        with col:
            kpi_card(title, val, "Live data response")
    st.subheader("Suggested demo questions")
    st.markdown("""
    - Which flights are at highest baggage SLA risk right now?
    - Show cargo damage incidents in the last 2 hours by severity and location.
    - Are there any safety compliance violations near active ramp zones?
    - Simulate the best corrective action to recover SLA for Flight AI-274.
    - Show evidence video for the damaged cargo box.
    """)
    record_action("Asked Gen BI for next-best action")

elif page == "SLA Cockpit":
    hero("Best-in-Industry SLA Cockpit", "Monitor predicted SLA, actual SLA and incident risk in one control surface.")
    st.plotly_chart(repo.sla_figure(), use_container_width=True)
    st.dataframe(repo.sla_table(), use_container_width=True, hide_index=True)
    c1, c2, c3 = st.columns(3)
    with c1: kpi_card("Prediction Window", "15–30 min", "Before operational impact")
    with c2: kpi_card("Decision Time", "Seconds", "Conversational BI")
    with c3: kpi_card("Operating Mode", "Preventive", "Not reactive")

elif page == "System Architecture":
    hero("System Architecture", "A modular demo architecture showing how physical airport operations become a real-time AI command layer.")
    st.markdown("""
    ### Reference architecture

    1. **Camera layer** — cargo belts, baggage belts, ramp zones, warehouse bays, loading areas.
    2. **Vision AI layer** — damage detection, object tracking, PPE detection, group recognition, unsafe proximity.
    3. **Operational data layer** — flight data, baggage IDs, ULD data, workforce roster, SLA timers, incident logs.
    4. **Risk correlation layer** — connects isolated signals into flight-level and zone-level risk scores.
    5. **Simulation layer** — tests workforce movement, lane rebalancing, baggage prioritization and inspection routing.
    6. **Gen BI layer** — natural language answers, root-cause explanation, evidence retrieval and next-best action.
    7. **Control tower layer** — executive dashboard, supervisor console, alerting and audit trail.
    """)
    st.code("""
Camera Feeds → Vision AI Models → Event Store → Risk Engine → Simulation Engine → Gen BI Agent → Control Tower
    """, language="text")
    st.subheader("Demo data modules")
    st.dataframe(repo.flights_table(), use_container_width=True, hide_index=True)
