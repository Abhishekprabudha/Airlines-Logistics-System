# Airline Logistics AI System — Streamlit Demo Repo

A Streamlit demo showing an AI-powered airline logistics control system for cargo, baggage, workforce safety/productivity, incident prevention, simulation and a conversational Gen BI assistant.

## What this demo includes

- Executive control tower dashboard
- Cargo damage vision AI module
- Passenger baggage damage detection module
- Workforce productivity and safety compliance module
- SLA incident prevention and risk scoring module
- Simulation engine for corrective actions
- Conversational Gen BI agent mock-up
- Flight / ULD / baggage / workforce sample datasets

## Login

Username: `admin`  
Password: `demo123`

## Run locally

```bash
pip install -r requirements.txt
streamlit run streamlit_app.py
```

## Recommended demo narrative

Use the app in this order:

1. Overview Control Tower
2. Cargo Vision AI
3. Baggage Vision AI
4. Workforce Safety
5. Incident Prevention
6. Simulation Engine
7. Gen BI Agent
8. SLA Cockpit

## Notes

This repo uses synthetic data for demo purposes. Replace the sample data in `app/services/airline_repo.py` with real camera inference, baggage tracking, WMS, RMS, AODB, workforce and SLA feeds when integrating into a production prototype.
