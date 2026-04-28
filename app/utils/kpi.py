import streamlit as st


def kpi_card(title: str, value, subtitle: str = ""):
    st.markdown(
        f"""
        <div class='kpi-card'>
            <div class='kpi-title'>{title}</div>
            <div class='kpi-value'>{value}</div>
            <div class='kpi-sub'>{subtitle}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def badge(text: str, kind: str = "ai"):
    cls = {"ai": "ai-badge", "risk": "risk-badge", "ok": "ok-badge"}.get(kind, "ai-badge")
    return f"<span class='{cls}'>{text}</span>"
