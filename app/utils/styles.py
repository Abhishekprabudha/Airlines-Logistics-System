import streamlit as st


def inject_styles():
    st.markdown(
        """
        <style>
        .main { background: #f8fafc; }
        .block-container { padding-top: 1.2rem; padding-bottom: 2rem; }
        .hero-card {
            background: linear-gradient(135deg, #0f172a 0%, #1e3a8a 55%, #0369a1 100%);
            color: white; padding: 24px; border-radius: 22px; margin-bottom: 18px;
            box-shadow: 0 18px 45px rgba(15, 23, 42, 0.20);
        }
        .hero-title {font-size: 2.0rem; font-weight: 800; margin-bottom: 6px;}
        .hero-sub {font-size: 1.0rem; color: #dbeafe; max-width: 920px;}
        .kpi-card {
            background: white; padding: 16px; border-radius: 18px; border: 1px solid #e2e8f0;
            min-height: 116px; box-shadow: 0 8px 28px rgba(15, 23, 42, 0.07);
        }
        .kpi-title {font-size: 0.82rem; color: #64748b; font-weight: 700; letter-spacing: .02em; text-transform: uppercase;}
        .kpi-value {font-size: 1.85rem; font-weight: 800; color: #0f172a; margin-top: 4px;}
        .kpi-sub {font-size: 0.86rem; color: #2563eb; margin-top: 4px;}
        .alert-high {background:#fef2f2; border-left: 5px solid #dc2626; padding: 12px; border-radius: 12px; margin: 8px 0;}
        .alert-med {background:#fffbeb; border-left: 5px solid #f59e0b; padding: 12px; border-radius: 12px; margin: 8px 0;}
        .alert-low {background:#f0fdf4; border-left: 5px solid #16a34a; padding: 12px; border-radius: 12px; margin: 8px 0;}
        .module-card {background:white; padding:18px; border:1px solid #e2e8f0; border-radius:18px; margin-bottom:12px;}
        .small-label {font-size:0.78rem; color:#64748b; text-transform:uppercase; font-weight:700; letter-spacing:.04em;}
        .ai-badge {display:inline-block; padding:6px 10px; border-radius:999px; background:#e0f2fe; color:#075985; font-weight:700; margin: 3px;}
        .risk-badge {display:inline-block; padding:6px 10px; border-radius:999px; background:#fee2e2; color:#991b1b; font-weight:700; margin: 3px;}
        .ok-badge {display:inline-block; padding:6px 10px; border-radius:999px; background:#dcfce7; color:#166534; font-weight:700; margin: 3px;}
        </style>
        """,
        unsafe_allow_html=True,
    )
