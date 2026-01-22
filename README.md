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

try it here: https://muxperts-veda.hf.space

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
- Note: The microphone and speech-to-text feature is currently a demo available only via local installation. It is not yet deployed to the live website due to the high processing power required to run the heavy AI models. You can test this feature by following the installation instructions above.
---

## 🧭 Design Principle

> Convert real-time classroom chaos into safe, ranked actions — instantly, predictably, and explainably.
---
## 📱/🖥️ Here's a preview of our website!
---
<img width="1919" height="932" alt="Screenshot 2026-01-21 173548" src="https://github.com/user-attachments/assets/8ce54f86-83db-44da-8e22-6965fad21910" />

---
<img width="1461" height="386" alt="Screenshot 2026-01-21 173614" src="https://github.com/user-attachments/assets/56eeb562-7a01-449b-9387-e56cd10bbca4" />

---
<img width="1530" height="784" alt="Screenshot 2026-01-21 173633" src="https://github.com/user-attachments/assets/0c5e3896-e2d0-430a-bff1-29b715719126" />

---
<img width="1509" height="613" alt="Screenshot 2026-01-21 173707" src="https://github.com/user-attachments/assets/f567208c-7a55-4f17-bb1a-87f2cd0317f3" />

---
<img width="1533" height="603" alt="Screenshot 2026-01-21 173720" src="https://github.com/user-attachments/assets/304fd7b1-2e04-47c5-ab47-43c9715d6ed6" />

---
<img width="1453" height="635" alt="Screenshot 2026-01-21 173737" src="https://github.com/user-attachments/assets/21d25bf6-6be8-43a6-88cb-747405d5c364" />

---
## Preview of Teacher's dashboard
---

<img width="1919" height="931" alt="Screenshot 2026-01-21 180258" src="https://github.com/user-attachments/assets/4f928faa-ab24-4a85-a147-e77114cfdd9b" />

---

## Preview of Admin's dashboard
---

<img width="1919" height="929" alt="Screenshot 2026-01-21 175915" src="https://github.com/user-attachments/assets/f44c1a1d-aff8-4d59-a546-0d648efa1762" />

---
