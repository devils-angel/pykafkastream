# 🌀 PyKafkaStream  
### _Full Stack Real-Time Web Application with Kafka & Docker_    

---

## 🚀 Overview
**PyKafkaStream** is a containerized full-stack web application that demonstrates real-time data streaming using **Apache Kafka** integrated with a **Flask backend** and **React frontend**.  
The project showcases an end-to-end setup where stock data updates flow seamlessly through a **Kafka producer-consumer** architecture, with a **Dockerized microservice** deployment.

---

## 🧠 Key Features
- 🔐 **User Authentication** — Secure registration & login with password hashing.  
- ⚡ **Real-Time Stock Data Endpoint** — Kafka-driven data streaming.  
- 🧩 **Modular Microservice Setup** — Scalable and containerized with Docker.  
- 💾 **SQLite Database Integration** — Persistent user and stock information storage.  
- 🔄 **React–Flask Communication** — REST API integration via Axios.  
- 🛡️ **Secure Design** — OWASP-aligned implementation using encrypted passwords, secure API calls, and CORS handling.

---

## 🏗️ System Architecture
```
Frontend (React) → Backend (Flask) → Database (SQLite)
Kafka Producer → Kafka Topic → Kafka Consumer
Docker Compose → Manages Services (Zookeeper, Kafka, Flask, React)
```

### 🧩 Components:
- **React Frontend:** Interactive UI for registration, login, and stock dashboard.  
- **Flask Backend:** REST API handling authentication, data access, and Kafka integration.  
- **Kafka & Zookeeper:** Real-time message broker for data streaming.  
- **SQLite Database:** Lightweight storage using SQLAlchemy ORM.  
- **Docker Compose:** Orchestrates all services into a single deployable environment.

---

## 🔧 Technology Stack

| Layer | Technology |
|-------|-------------|
| Frontend | React + Axios + React Router |
| Backend | Flask + SQLAlchemy |
| Streaming | Apache Kafka + Zookeeper |
| Database | SQLite |
| Containerization | Docker + Docker Compose |

---

## 🔐 Security Highlights
- **Encrypted Authentication:** Passwords hashed.  
- **Secure Data Transmission:** Sensitive data hidden in POST requests and URLs.   
- **OWASP Top 10 Alignment:** Protection against common vulnerabilities like broken authentication, sensitive data exposure, and insecure design.

---

## 🧾 Flask API Endpoints

| Endpoint | Method | Description |
|-----------|---------|-------------|
| `/register` | POST | Secure user signup with password hashing |
| `/login` | POST | Authenticates user credentials |
| `/data` | GET | Fetches stock details from SQLite |

---

## 🧱 Database Models
- **User:** Stores username, email, and encrypted password.  
- **Stock:** Stores stock symbol, name, and real-time price data.

---

## 🧰 Kafka Configuration
- **Broker:** `KAFKA_BROKER=kafka:9092` (defined via environment variables)  
- **Flow:** Producers publish → Kafka topics → Consumers receive and update frontend.  

---

## 🐳 Docker Deployment

### Services & Ports

| Service | Port |
|----------|------|
| React App | 5173 |
| Flask API | 5000 |
| Kafka | 9092 |
| Zookeeper | 2181 |

### Run Instructions:
```bash
# Clone repository and ensure docker is installed by checking version : docker --version
git clone https://github.com/devils-angel/pykafkastream.git
cd pykafkastream

# Build and start all services
docker-compose up --build
# To run in detached mode
docker-compose up -d --build
```

Access the application via **http://localhost:5173**

---

## 📊 Impact
- Demonstrates full-stack, real-time system architecture.  
- Showcases practical knowledge of microservices and containerization.  
- Builds real-world experience with Kafka integration and Docker Compose orchestration.

---

## 🧭 Learning Outcomes
- Integrated multiple technologies across the full stack.  
- Gained DevOps and CI/CD exposure using Docker.  
- Debugged container networking and dependency issues.  

## 🙌 Acknowledgments
Built with ❤️ by **Yukta Piyush Shah** 
