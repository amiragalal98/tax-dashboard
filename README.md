# 📊 Tax Dashboard - DevOps Project

A full-stack Dockerized application that collects tax data using a Flask web app, stores it in a MySQL database, monitors app metrics with Prometheus, and visualizes data using Grafana. CI/CD is managed via GitHub Actions (and optionally Jenkins).

---

## 📦 Technologies Used

- **Flask** — Web server
- **MySQL** — Database to store tax data
- **Docker + Docker Compose** — Containerization
- **Grafana** — Visualization of tax data
- **Prometheus** — Monitoring metrics from the Flask app.
- **GitHub Actions** — CI/CD automation
- **Jenkins** *(optional)* — Alternative CI/CD pipeline.

---

## 🗂️ Project Structure

project/

│
├── app/ # Flask app and Dockerfile

│ ├── app.py
│ └── templates/index.html
│

├── init.sql # MySQL schema

├── prometheus.yml # Prometheus config

├── docker-compose.yml # Multi-service setup

└── Jenkinsfile # jenkins pipeline
└── docker-build.yml


---

## 🛠️ How to Run Locally

1. Clone the repo:
```bash
git clone https://github.com/amiragalal98/tax-dashboard.git
cd tax-dashboard
2. Start the services:
docker compose up -d
3. Access the apps:
| Service    | URL                                            |
| ---------- | ---------------------------------------------- |
| Flask App  | [http://localhost:5001](http://localhost:5000) |
| Grafana    | [http://localhost:3000](http://localhost:3000) |
| Prometheus | [http://localhost:9090](http://localhost:9090) |
| Jenkins    | [http://localhost:8080](http://localhost:8080) |


🧪 Features
*Submit tax data via a form.

*Data is stored in MySQL.

*Visualized in Grafana using a MySQL data source.

*Monitored using Prometheus (http requests, status codes, etc.).

*CI/CD builds app image automatically using GitHub Actions OR Jenkins.




