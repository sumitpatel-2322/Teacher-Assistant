---
title: Teacher Assistant
emoji: 📚
colorFrom: blue
colorTo: green
sdk: docker
pinned: false
app_port: 7860
license: apache-2.0
short_description: AI-Powered Teacher Assistant
---
# 🎓 Just-in-Time Classroom Assistant

A **deterministic, real-time classroom decision-support system** built for teachers operating under real classroom constraints.

> **Design guarantee:** Given the same input and constraints, the system will always return the same output.

---

## 📌 What This System Is — and Is Not

### This system **IS**
- A just-in-time **classroom panic button**
- A **deterministic decision engine**, not a chatbot
- A bridge between **teacher micro-moments** and **academic leadership insight**
- Designed for **government and low-infrastructure classrooms**

### This system **IS NOT**
- A generative AI chatbot
- A counselling or therapy tool
- A lesson planner or curriculum designer
- A black-box ML personalization engine

Clear boundaries ensure safety, predictability, and trust.

---

## 📖 Overview

Teachers face breakdowns **during** teaching, not after workshops.

The Just-in-Time Classroom Assistant supports teachers in live classroom moments by converting messy, emotional input into **safe, executable actions within seconds**.

Instead of post-facto feedback, the system provides **micro-interventions** that respect:
- Time pressure
- Large class sizes
- Limited digital infrastructure
- Zero tolerance for experimentation risk

---

## ⚠️ Problem Statement

### Context
Classroom breakdowns are immediate:
- Noise escalation
- Conceptual confusion
- Student disengagement
- Time overruns

### Why Existing Systems Fail
- **Delayed**: Feedback arrives days or weeks later  
- **Generic**: Abstract advice, not executable steps  
- **Disconnected**: No feedback loop to academic leadership  

### Result
Teachers develop **Implementation Anxiety**, revert to rote methods, and avoid innovation.

---

## 🧠 Ground Research & Validation

Before development, we studied the field:

- Teacher surveys (Google Forms) identifying real breakdown moments
- Classroom observations in government schools
- Interviews revealing why existing EdTech tools fail:
  - Too complex
  - Internet dependent
  - High cognitive load

**Key insight:**  
Teachers don’t need intelligence. They need **reliability under pressure**.

---

## 💡 The Solution

### For Teachers
- Voice or text input (messy input allowed)
- Instant output: **Top 3 low-effort classroom actions**
- No follow-up questions
- No explanations
- Classroom-ready language

### For Academic Leadership (CRP / BRP / ARP)
- Live dashboards of classroom issues
- Cluster-wise heat maps
- Data-backed visit planning
- Visibility into digital vs physical intervention gaps

---

## 📚 Knowledge Base & Data Sources

All solutions are **pre-validated**, not generated.

Sources include:
- CBSE Handbooks (official pedagogy)
- FLN & NEP resources
- Large-scale scraping of teacher forums (practical edge cases)

This forms a **Solution Library** blending:
- Pedagogical correctness
- Field-tested practicality

---

## ⚙️ How the Deterministic Decision Engine Works

### End-to-End Example

**Input**
> “Students are noisy and don’t understand fractions”

**Detected Signals**
- NOISE_SPIKE
- CONCEPT_CONFUSION

**Constraints**
- No projector
- Time remaining < 10 minutes

**Output**
1. Board-based Think–Pair–Explain (fractions)
2. Fraction voting cards
3. Silent solve + peer check

---

### Core Pipeline

1. **Input Normalization**
   - Handles spelling errors, emotion, grammar noise

2. **Signal Extraction**
   - Rule-based detection (e.g., NOISE_SPIKE, TIME_LOW)

3. **Constraint Filtering**
   - Infrastructure, time, safety constraints applied

4. **Deterministic Scoring**
   - Low effort + high safety ranked highest

5. **Solution Selection**
   - Top 3 distinct solutions retrieved
   - No hallucination, no free-text generation

---

## 🛡 Failure Modes & Safeguards

- No solution match → fallback to safest generic intervention
- Overlapping solutions → enforced diversity
- Vague input → defaults to classroom-safe actions
- Empty output → impossible by design

---

## 🔄 Administrative Feedback Loop

Teacher → CRP → BRP → ARP

- Teachers report breakdowns
- CRPs see real-time cluster issues
- BRPs monitor intervention coverage
- ARPs identify systemic academic gaps

All logging is silent and non-intrusive.

---

## 🛠 Tech Stack

### Current
- Backend: FastAPI (Python 3.11)
- Frontend: Jinja2 + Vanilla JS
- Database: SQLite (zero-ops, offline-friendly)
- AI: Whisper/Vosk, HuggingFace (signal detection)
- Visualization: Chart.js

### Why SQLite First?
- Zero operational overhead
- Predictable performance
- Ideal for school pilots and offline-first deployment

---

## 🔮 Roadmap (Non-Negotiables Included)

- Offline Lite App (text-only, local DB)
- Vernacular language expansion
- SLMs for **empathetic acknowledgement only**
  - Deterministic decision core remains untouched

---

## 🚀 Installation
First edit the requirements.txt uncomment these three lines then follow the steps below it.(remove #)
```
# torch
# torchvision
# torchaudio #(for deployment purpose)
```
```bash
git clone <repo_url>
pip install -r requirements.txt
uvicorn app:app --reload
```

- Teacher Dashboard: http://localhost:8000/dashboard
- Admin Login: http://localhost:8000/login
- This changes is for the a feature of using microphone this is demo for the project the online site does not contain this feature yet because the microphone and speech to text need heavy models power processiing since that feature is not included yet,But you can access it via this above installation.
---

## 🧭 Design Principle

> Convert real-time classroom chaos into safe, ranked actions — instantly, predictably, and explainably.

