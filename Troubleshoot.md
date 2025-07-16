# 🛠️ Troubleshooting Guide for Tax Dashboard Project

This document lists all the major issues encountered during development,setup, and deployment of the project — along with the steps taken to solve them.

---

## 📦 Docker & Docker Compose Issues

### ❌ `environment must be a string or number`
**Problem:**  
Wrong format in `docker-compose.yml` under `environment`.

**Fix:**  
Ensure environment variables are in key-value form:-

```yaml
environment:
  MYSQL_ROOT_PASSWORD: rootpass


❌ build is not allowed under service.web
Problem:
Misuse of build property in docker-compose.yml.

Fix:
Make sure each service has a valid structure. Example:

services:
  web:
    build: ./app
    ports:
      - "5001:5000"
❌ 127.0.0.1 didn't send any data / browser not opening
Problem:
Service is not running or port is not mapped correctly.

Fix:

Check container status with docker ps

Verify port mapping in docker-compose.yml


❌ MySQL container exits (status Exited 1)
Problem:
Invalid init.sql or environment variables.

Fix:

Validate init.sql (syntax, schema)

Ensure correct environment vars
environment:
  MYSQL_DATABASE: taxdb
  MYSQL_ROOT_PASSWORD: rootpass


❌ Can't connect to local MySQL through socket
Problem:
MySQL not running or not exposed.

Fix:

Use localhost and port 3306

Confirm container is running

Use correct root password


📊 Grafana & Prometheus Issues
❌ Grafana: No connection / curl: connection refused
Problem:
Grafana container not running or wrong port.

Fix:

Ensure grafana service is mapped to 3000

Use docker ps and docker logs grafana



❌ Prometheus: No such host
Problem:
Wrong target in prometheus.yml.

Fix:
Use Docker service name instead of localhost
- targets: ['web:5001']


❌ Prometheus: No metrics / no data
Problem:
Flask app not exposing metrics or no requests made.

Fix:

Add PrometheusMetrics to app.py:
from prometheus_flask_exporter import PrometheusMetrics
metrics = PrometheusMetrics(app)


🔁 Jenkins CI/CD Issues
❌ could not find remote refs/heads/master
Problem:
GitHub repo uses main instead of master.

Fix:
Update Jenkins pipeline branch to main.



❌ permission denied when using Docker in Jenkins
Problem:
Jenkins user doesn't have access to Docker.

Fix:

Add Jenkins to Docker group:
RUN usermod -aG docker jenkins
Mount Docker socket in docker run:
-v /var/run/docker.sock:/var/run/docker.sock

❌ docker not found inside Jenkins container
Fix:
Install Docker inside Jenkins container:
RUN apt-get update && apt-get install -y docker.io


🧪 GitHub Actions Issues
❌ docker-compose not found
Fix:
Use docker/compose-action or install manually inside the runner


❌ GitHub Actions: No data in Grafana after build
Fix:
Make sure Flask app is generating traffic.
Wait for Prometheus to scrape data.


📌 Commands Used for Debugging

docker ps                     # List running containers
docker logs <container>      # View container logs
docker exec -it <id> bash    # Access running container
docker volume prune -f       # Clean up old volumes
docker-compose down -v       # Remove volumes and containers
curl http://localhost:<port> # Test service health

✅ General Advice
Always confirm containers are running with docker ps

Use docker logs when a container exits unexpectedly

Double-check port mappings in docker-compose.yml

Use volumes for persisting data like MySQL schema

Don't use localhost in Prometheus/Grafana — use Docker service name





