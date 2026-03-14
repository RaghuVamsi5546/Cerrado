# AI Log Diagnosis Agent

A lightweight **AI-style system monitoring agent** that collects system metrics, detects anomalies, diagnoses root causes, and exposes results through an API.

The system monitors **CPU, Memory, and Disk usage**, stores logs in a database, analyzes recent events, and generates automated incident reports.

---

# Features

- Collects system metrics using `psutil`
- Stores logs in **SQLite**
- Detects **CPU and memory spikes**
- Generates **structured incident diagnosis**
- Exposes results through a **FastAPI API**
- Includes a **stress test script** for anomaly simulation

---

# Architecture

```
System Metrics
     ↓
Observer (Collector)
     ↓
SQLite Database
     ↓
Diagnosis Agent
     ↓
JSON Output
     ↓
FastAPI API
```

---

# Project Workflow

1. System metrics are collected from the machine.
2. The **Observer** records these metrics.
3. Logs are stored in an **SQLite database**.
4. The **Diagnosis Agent** analyzes recent events.
5. Root cause analysis is generated.
6. Results are exposed via a **FastAPI endpoint**.

---

# Run the Project

### 1️⃣ Start Log Collector

```bash
python observer.py
```

### 2️⃣ Start Diagnosis Agent

```bash
python agent.py
```

### 3️⃣ Start API Server

```bash
uvicorn api:app --reload
```

The API will run at:

```
http://127.0.0.1:8000/diagnosis
```

---

# Stress Test (Optional)

Run the stress test script to simulate anomalies.

```bash
python stress_test.py
```

This script simulates a **memory spike** to test the anomaly detection system.

---

# Example Output

```json
{
  "root_cause": "High memory usage detected",
  "severity": "HIGH",
  "recommended_action": "Check running processes consuming memory"
}
```

---

# Tech Stack

- **Python**
- **psutil**
- **SQLite**
- **FastAPI**
- **Uvicorn**

---

