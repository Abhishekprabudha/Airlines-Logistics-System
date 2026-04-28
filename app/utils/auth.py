import streamlit as st


def login_panel():
    st.markdown("""
    <div class='hero-card'>
      <div class='hero-title'>Airline Logistics AI System</div>
      <div class='hero-sub'>Demo login for the invisible airline nervous system — cargo, baggage, people, incident prevention, simulations and Gen BI.</div>
    </div>
    """, unsafe_allow_html=True)
    with st.form("login"):
        user = st.text_input("Username", value="admin")
        password = st.text_input("Password", type="password", value="demo123")
        submitted = st.form_submit_button("Login")
    if submitted:
        if user == "admin" and password == "demo123":
            st.session_state.authenticated = True
            st.rerun()
        else:
            st.error("Invalid credentials")
