import pandas as pd
import plotly.express as px
import plotly.graph_objects as go


class AirlineLogisticsRepository:
    """Synthetic repository for Streamlit demo. Replace with live feeds in production."""

    def __init__(self):
        self.flights = pd.DataFrame([
            ["AI-274", "DEL", "LHR", "Turnaround", 42, 72, "At Risk", "Belt-06 congestion + cargo recheck"],
            ["IG-819", "BLR", "DXB", "Loading", 31, 28, "Safe", "Normal"],
            ["6E-412", "BOM", "SIN", "Cargo Build", 55, 64, "Watch", "ULD inspection queue rising"],
            ["UK-105", "HYD", "FRA", "Boarding", 24, 18, "Safe", "Normal"],
            ["AI-191", "MAA", "JFK", "Baggage Closeout", 18, 81, "Critical", "Late baggage batch + PPE exception"],
        ], columns=["Flight", "Origin", "Destination", "Stage", "Mins to SLA", "Risk %", "SLA State", "Primary Driver"])

        self.cargo_events = pd.DataFrame([
            ["CGO-88391", "ULD-AKE-2201", "Bay C2", "Crushed corner", 91, "High", "AI-274", "Auto-hold + inspection lane"],
            ["CGO-88422", "ULD-PAG-1130", "Bay A1", "Seal anomaly", 94, "High", "6E-412", "Supervisor review"],
            ["CGO-88437", "Loose Carton", "Cargo Belt 3", "Surface tear", 87, "Medium", "IG-819", "Photograph + accept with note"],
            ["CGO-88451", "ULD-AKE-2298", "Bay D4", "Water mark", 78, "Medium", "AI-191", "Route to quarantine zone"],
            ["CGO-88470", "Pallet-PH-09", "Cold Chain Lane", "Temperature label missing", 82, "Medium", "UK-105", "Manual verification"],
        ], columns=["Asset ID", "Container", "Location", "Detection", "Confidence %", "Severity", "Linked Flight", "Action"])

        self.baggage_events = pd.DataFrame([
            ["BAG-48291", "Belt-06", "Cracked shell", 92, "Medium", "AI-274", "Before aircraft loading", "Service recovery note"],
            ["BAG-48302", "Belt-06", "Open zipper risk", 86, "Medium", "AI-274", "Sortation", "Secure + retag"],
            ["BAG-49818", "Carousel-02", "Broken wheel", 89, "Low", "IG-819", "Arrival claim prevention", "Photo evidence"],
            ["BAG-50112", "Ramp Dolly 4", "Handle tear", 90, "High", "AI-191", "Ramp transfer", "Hold and notify"],
            ["BAG-50777", "Belt-03", "Strap entanglement", 84, "High", "6E-412", "Transfer belt", "Stop belt + clear risk"],
        ], columns=["Bag ID", "Zone", "Detection", "Confidence %", "Severity", "Flight", "Detected At", "Action"])

        self.workforce = pd.DataFrame([
            ["Bay A", 16, 97, 92, 412, "Safe", "Normal flow"],
            ["Bay B", 22, 88, 80, 365, "Watch", "Congestion increasing"],
            ["Bay C", 14, 94, 91, 388, "Safe", "Normal flow"],
            ["Ramp Zone 4", 18, 82, 76, 301, "Critical", "Unsafe proximity + missing vest"],
            ["Belt-06", 11, 91, 84, 276, "Watch", "Staff shortage against loading demand"],
        ], columns=["Zone", "People Count", "PPE Compliance %", "Safety Score", "Packages/hr", "State", "Observation"])

        self.incidents = pd.DataFrame([
            ["INC-9001", "AI-191", "Critical", 81, "Late baggage batch + PPE exception", "Redeploy 3 staff to Belt-06 and hold damaged bag"],
            ["INC-9002", "AI-274", "High", 72, "Belt congestion + cargo recheck", "Move 2 staff from Bay A to Belt-06"],
            ["INC-9003", "6E-412", "Medium", 64, "ULD inspection queue", "Open parallel inspection lane"],
            ["INC-9004", "IG-819", "Low", 28, "Minor baggage evidence capture", "Continue operations"],
        ], columns=["Incident", "Flight", "Severity", "Risk %", "Root Cause", "Recommended Action"])

        self.simulations = pd.DataFrame([
            ["Do Nothing", "AI-274", "SLA breach in 18 min", -11, 72, "High"],
            ["Redeploy 3 staff to Belt-06", "AI-274", "SLA restored with 8 min buffer", 8, 34, "Best"],
            ["Open secondary cargo inspection lane", "6E-412", "ULD delay reduced by 22%", 5, 41, "Good"],
            ["Hold damaged bags + proactive passenger alert", "AI-191", "Claims risk reduced by 35%", 3, 52, "Good"],
            ["Prioritize transfer baggage batch B17", "AI-274", "Baggage closeout recovered", 6, 39, "Good"],
        ], columns=["Scenario", "Flight", "Predicted Outcome", "SLA Buffer Min", "Residual Risk %", "Ranking"])

        self.sla_history = pd.DataFrame({
            "Hour": ["08:00", "09:00", "10:00", "11:00", "12:00", "13:00", "14:00"],
            "Predicted SLA %": [93, 91, 89, 86, 88, 92, 96],
            "Actual SLA %": [92, 90, 88, 84, 87, 91, 95],
            "Incident Risk %": [22, 28, 44, 62, 51, 36, 21],
        })

    def get_overview_summary(self):
        return {
            "active_flights": len(self.flights),
            "critical_risks": int((self.flights["Risk %"] >= 75).sum()),
            "cargo_damages": len(self.cargo_events),
            "baggage_events": len(self.baggage_events),
            "avg_ppe": f"{round(self.workforce['PPE Compliance %'].mean(), 1)}%",
            "sla_prediction": "92.4%",
        }

    def get_alerts(self):
        return [
            {"level": "high", "title": "AI-191 critical SLA risk", "message": "Late baggage batch and safety exception may breach closeout window."},
            {"level": "high", "title": "Cargo damage detected", "message": "CGO-88391 crushed corner found at Bay C2 linked to AI-274."},
            {"level": "medium", "title": "Workforce congestion", "message": "Belt-06 is below required staffing for current baggage demand."},
        ]

    def flights_table(self):
        return self.flights

    def cargo_table(self):
        return self.cargo_events

    def baggage_table(self):
        return self.baggage_events

    def workforce_table(self):
        return self.workforce

    def incident_table(self):
        return self.incidents

    def simulation_table(self):
        return self.simulations

    def sla_table(self):
        return self.sla_history

    def risk_funnel_figure(self):
        df = pd.DataFrame({
            "Layer": ["Camera Signals", "AI Detections", "Correlated Risks", "Incidents Prevented"],
            "Count": [2840, 147, 19, 11]
        })
        return px.funnel(df, x="Count", y="Layer", title="Signal-to-Prevention Funnel")

    def flight_risk_figure(self):
        return px.bar(self.flights, x="Flight", y="Risk %", color="SLA State", title="Flight-level SLA Risk")

    def workforce_figure(self):
        return px.scatter(self.workforce, x="People Count", y="Packages/hr", size="Safety Score", color="State", hover_name="Zone", title="People Productivity vs Safety")

    def sla_figure(self):
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=self.sla_history["Hour"], y=self.sla_history["Predicted SLA %"], mode="lines+markers", name="Predicted SLA %"))
        fig.add_trace(go.Scatter(x=self.sla_history["Hour"], y=self.sla_history["Actual SLA %"], mode="lines+markers", name="Actual SLA %"))
        fig.add_trace(go.Scatter(x=self.sla_history["Hour"], y=self.sla_history["Incident Risk %"], mode="lines+markers", name="Incident Risk %"))
        fig.update_layout(title="SLA Prediction vs Incident Risk", yaxis_title="Percent")
        return fig

    def gen_bi_answer(self, question: str):
        q = question.lower()
        if "ai-274" in q or "baggage" in q or "belt" in q:
            return {
                "answer": "Flight AI-274 has a 72% SLA breach probability driven by Belt-06 congestion, two baggage damage events and one cargo recheck. Recommended action: redeploy 3 workers to Belt-06 and prioritize baggage batch B17. Simulation predicts SLA recovery with an 8-minute buffer.",
                "cards": [("Risk", "72%"), ("Impacted bags", "148"), ("Recovery action", "Redeploy 3 staff"), ("Predicted buffer", "+8 min")]
            }
        if "cargo" in q or "damage" in q:
            return {
                "answer": "There are 5 cargo vision events. Two are high severity: CGO-88391 crushed corner at Bay C2 and CGO-88422 seal anomaly at Bay A1. Both are linked to active flights and have been routed for inspection.",
                "cards": [("Cargo events", "5"), ("High severity", "2"), ("Top confidence", "94%"), ("Action", "Auto inspection")]
            }
        if "worker" in q or "safety" in q or "ppe" in q:
            return {
                "answer": "Ramp Zone 4 is the highest safety risk with 82% PPE compliance and a safety score of 76. The system recommends supervisor intervention and worker redeployment from Bay A after closeout.",
                "cards": [("Avg PPE", "90.4%"), ("Critical zone", "Ramp Zone 4"), ("People count", "18"), ("Action", "Supervisor alert")]
            }
        return {
            "answer": "The control tower is monitoring 5 active flights, 5 cargo events, 5 baggage events, 5 workforce zones and 4 active incident risks. One critical and two high-priority operational risks require immediate attention.",
            "cards": [("Active flights", "5"), ("Critical risks", "1"), ("Vision events", "10"), ("Predicted SLA", "92.4%")]
        }
