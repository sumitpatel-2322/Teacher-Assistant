# Just in Time Classroom Assistant  
## Design and Approach Document

## 1. Context and Problem Background

Teachers frequently face high pressure and unpredictable classroom situations where immediate support is needed.  
Current support structures rely on periodic visits by resource persons, which results in delayed and generic feedback.  
This gap leaves teachers without actionable guidance during the most critical moments of instruction.  
Over time, this leads to implementation anxiety, abandonment of innovative practices, and burnout.

---

## 2. Core Positioning of the Application

This application is a **Just in Time Classroom Helper**.

It does not replace teacher training programs, resource persons, or pedagogical frameworks.  
Instead, it acts as a real time support bridge that extends the intent of teacher training and mentoring into the exact moment when a classroom situation is failing.

---

## 3. Core Design Philosophy

**The teacher is not asking a question. She is reporting a situation.**

Teachers are treated as skilled professionals who require situational support, not evaluation or correction.  
The assistant responds to classroom breakdowns rather than abstract theoretical doubts.

---

## 4. System Thinking Pipeline

Every interaction strictly follows this sequence:

- Situation  
- Constraints  
- Immediate Options  
- Optional Activity

---

## 5. Nature of Teacher Input

Teacher input may include:

• Messy and unstructured text or voice input  
• Grammatically incorrect or mixed language usage  
• Emotionally loaded or vague descriptions  
• Explicit mention of failure or urgency  

The system is designed to work reliably even when the input is imperfect.

---

## 6. Classroom Situation Categories

The system identifies one dominant classroom situation per interaction:

• Attention and discipline breakdown  
• Time pressure situations  
• Conceptual confusion  
• Activity failure  
• Technical breakdown  
• Student behavior edge cases  

Multiple issues are intentionally not handled together to reduce cognitive load.

---

## 7. Constraint Awareness

Before generating any response, the system evaluates real world classroom constraints such as:

• Time remaining in the period  
• Class size and student mix  
• Grade level  
• Subject type  
• Available tools  

Board only conditions are assumed by default.  
The system never assumes ideal classroom environments.

---

## 8. Output Design Rules

All responses strictly follow these rules:

• No fluff or motivational language  
• No explanation of why a suggestion works  
• Exactly three to four options per response  
• Options sorted by efficiency and safety  
• Every response includes a graceful fallback  

---

## 9. Activities Purpose and Inclusion Logic

**Purpose of Activities**

The purpose of an activity is not to teach the concept, but to unstuck the classroom and reset student thinking.

**Activity Rules**

• Activities are never auto suggested  
• Activities appear only when explicitly requested by the teacher  
• Only one activity is provided per interaction  
• Activities are non generic, low risk, and time boxed for three to five minutes  

---

## 10. Reference Scenario

**Teacher Input Example**

I have tried explaining Algebra concepts but students are not understanding.

**System Behavior**

The assistant provides immediate, executable options.  
If the teacher requests an activity, one curiosity driven activity is added to break the stuck pattern rather than repeat explanation.

---

## 11. Expected Outcomes

This system reduces implementation anxiety and eliminates coaching lag time.  
It helps teachers retain innovative practices without reverting to rote instruction.  
It complements existing training and mentoring structures by providing real time, context aware classroom support.

---

## Final Positioning Statement

This application is not a trainer, evaluator, or replacement for mentors.  
It is a reliable, just in time classroom companion that supports teachers at the exact moment they need help.
