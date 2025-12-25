
# 📘 Smart Resume Scanner (End-to-End DevOps Project)

## 🚀 Project Overview

**Smart Resume Scanner** is a Python-based Flask application that analyzes resumes and recommends jobs using NLP techniques.
This project demonstrates a **complete end-to-end DevOps lifecycle** — from local development to **CI/CD, containerization, Kubernetes deployment, and monitoring**.

The goal of this project was not only to build an application, but to **design, automate, deploy, and monitor it like a real production system**.

---

## 🧠 What I Learned From This Project

* How real CI/CD pipelines work end-to-end
* Docker image lifecycle (build → tag → push → deploy)
* Jenkins automation with GitHub webhooks
* Kubernetes deployments & services
* Handling real-world issues (ports, permissions, image pulls, auth)
* Monitoring workloads using Prometheus & Grafana

---

## 🏗️ Architecture

```
Developer → GitHub → Jenkins (CI/CD)
                     |
                     v
                Docker Image
                     |
                     v
                Docker Hub
                     |
                     v
             Kubernetes (Minikube)
                     |
                     v
           Monitoring (Prometheus + Grafana)
```

---

## 🧩 Tech Stack

### Application

* Python 3
* Flask
* spaCy (NLP)
* scikit-learn
* pdfminer

### DevOps & Cloud-Native

* Git & GitHub
* Jenkins (CI/CD)
* Docker & Docker Hub
* Kubernetes (Minikube)
* kubectl
* Prometheus
* Grafana
* Linux (Ubuntu)

---

## 📂 Repository Structure

```
SmartResumeScanner/
│
├── app/                    # Flask application code
├── k8s/
│   ├── deployment.yaml     # Kubernetes Deployment
│   └── service.yaml        # Kubernetes Service (NodePort)
├── Dockerfile              # Docker image definition
├── Jenkinsfile             # Jenkins CI/CD pipeline
├── requirements.txt        # Python dependencies
├── run.py                  # App entry point
└── README.md
```

---

## 🔄 CI/CD Pipeline (Jenkins)

### Pipeline Stages

1. **Checkout Code**

   * Pulls latest code from GitHub on every push

2. **Build Docker Image**

   * Builds image using Dockerfile
   * Tags image with Git commit hash

3. **Push Image to Docker Hub**

   * Pushes versioned image to Docker Hub

4. **Deploy to Kubernetes**

   * Updates running deployment using:

     ```bash
     kubectl set image
     ```
   * Ensures zero downtime rollout

---

## 🐳 Docker Highlights

* Lightweight base image (`python:3.11-slim`)
* Optimized layers using Docker cache
* Application exposed on port `5000`
* Production-ready image pushed to Docker Hub

---

## ☸️ Kubernetes Deployment

* **Deployment**

  * Manages application pods
  * Handles restarts & scaling

* **Service (NodePort)**

  * Exposes application outside cluster

* **Rolling Updates**

  * Achieved using `kubectl set image`

---

## 📊 Monitoring with Prometheus & Grafana

### Prometheus

* Collects cluster & node metrics
* Monitors pod health and resource usage

### Grafana

* Visual dashboards for:

  * CPU usage
  * Memory usage
  * Pod status
  * Node health

### Access Grafana

```bash
kubectl port-forward svc/monitoring-grafana 3000:80
```

---

## 🛠️ Common Issues Solved (Real-World Learning)

* Docker port conflicts (`address already in use`)
* Jenkins permission issues with Docker & Kubernetes
* `ImagePullBackOff` in Kubernetes
* Jenkins authentication to Minikube
* Secure handling of kubeconfig
* Grafana login & secret management

---

## 🎯 Why Jenkins Instead of GitHub Actions?

| Jenkins                     | GitHub Actions  |
| --------------------------- | --------------- |
| Self-hosted                 | SaaS            |
| Full control                | Limited runners |
| Enterprise-friendly         | Repo-centric    |
| Works well with on-prem K8s | Cloud-first     |

➡️ **This project intentionally uses Jenkins** to simulate **real enterprise environments**.

---

## 📌 Key Interview Questions From This Project

* How does Jenkins trigger builds from GitHub?
* Difference between Docker image & container?
* What is `kubectl set image`?
* Why NodePort vs LoadBalancer?
* How does Kubernetes handle rolling updates?
* Difference between CI and CD?
* How does Prometheus scrape metrics?
* What problems does Docker solve?

---

## ✅ Project Status

✔ Application running on Kubernetes
✔ CI/CD automated via Jenkins
✔ Monitoring enabled with Grafana & Prometheus

---

## 📈 Future Enhancements

* Helm charts
* Horizontal Pod Autoscaler (HPA)
* Ingress controller
* GitHub Actions comparison pipeline
* AWS / EKS deployment

---

