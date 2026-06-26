Edge AI Telemetry & Performance Dashboard
A professional-grade, containerized dashboard built to monitor and analyze real-time telemetry from Edge AI model deployments. This project demonstrates expertise in Python data pipelines, containerization with Docker, and interactive data visualization.

Overview
This application serves as a Project Governance Console, simulating the monitoring of a live AI model. It features a 4-zone UI layout that allows users to track performance metrics, identify anomalies, and perform root-cause analysis in a highly efficient, production-ready environment.

Technical Stack
Core: Python 3.10+

Frontend/UI: Streamlit

Data Visualization: Plotly Express

Data Processing: Pandas (with high-performance caching)

DevOps/Deployment: Docker & Docker Compose

Key Features
Optimized Data Engine: Implements @st.cache_data decorators to ensure seamless data ingestion and normalization from structured telemetry logs.

Interactive Interaction Loops: Dynamic UI thresholds that trigger real-time alerts based on user-defined confidence levels.

Explainable AI (XAI) Feed: Automated root-cause analysis blocks triggered by system failures or performance drops.

Single-Command Deployment: Fully containerized environment ensuring "run-anywhere" reproducibility on macOS, Linux, or Windows.

Architecture
The dashboard is split into four distinct zones for clear governance:

Metrics Display: Real-time KPIs (Inference Latency, FPS, Confidence Score).

Analytics Charts: Responsive historical performance tracking using Plotly.

Control Sliders: Real-time threshold adjustment for system triggers.

Alert Feed: Dynamic status sidebar with automated diagnostic logs.

Getting Started
To run the dashboard locally, ensure you have Docker Desktop installed.

1. Clone the repository:
git clone https://github.com/Kosritok/ai-telemetry-dashboard.git
cd ai-telemetry-dashboard
2. Build and run the container:
docker compose up --build
3. Access the dashboard:
Open your browser and navigate to http://localhost:8501

Built as a professional-grade solution for Edge AI governance.
