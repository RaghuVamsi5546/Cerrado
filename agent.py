import sqlite3
import json
import time
from datetime import datetime, timedelta
from rich import print

WINDOW_SECONDS = 30

def get_recent_events():

    conn = sqlite3.connect("events.db")
    cursor = conn.cursor()

    cutoff = datetime.now() - timedelta(seconds=WINDOW_SECONDS)


    cursor.execute(
"""
SELECT timestamp,message,severity
FROM events
WHERE timestamp >= datetime('now','-30 seconds')
"""
)

    rows = cursor.fetchall()

    return rows


def analyze_events(events):

    cpu_spike = False
    memory_spike = False

    evidence = []

    for e in events:

        message = e[1]

        parts = message.split()

        cpu = float(parts[0].split("=")[1])
        mem = float(parts[1].split("=")[1])

        if cpu > 80:
            cpu_spike = True
            evidence.append(message)

        if mem > 80:
            memory_spike = True
            evidence.append(message)

        if mem > 95:
            severity = "CRITICAL"

    root_cause = "System operating normally"
    severity = "LOW"
    summary = "No anomaly detected"
    recommended = "No action needed"
    confidence = 0.7

    if memory_spike:
        root_cause = "High memory usage detected"
        severity = "HIGH"
        summary = "Memory spike causing potential slowdown"
        recommended = "Check running processes consuming memory"
        confidence = 0.85

    if cpu_spike:
        root_cause = "CPU overload detected"
        severity = "HIGH"
        summary = "CPU spike detected"
        recommended = "Inspect high CPU processes"
        confidence = 0.8

    diagnosis = {

        "incident_summary": summary,
        "root_cause": root_cause,
        "causal_chain": evidence,
        "evidence": evidence,
        "data_source": "own-machine",
        "severity": severity,
        "recommended_action": recommended,
        "confidence": confidence,
        "needs_more_data": False
    }

    return diagnosis


def save_output(data):

    with open("output.json","w") as f:
        json.dump(data,f,indent=4)


print("[green]Agent started[/green]")

while True:

    events = get_recent_events()

    diagnosis = analyze_events(events)

    print("\n[bold cyan]Agent Diagnosis[/bold cyan]")
    print(diagnosis)

    save_output(diagnosis)

    time.sleep(10)