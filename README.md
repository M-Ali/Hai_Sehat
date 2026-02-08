# SehatSathi — Safety-First Health Education Assistant for NGOs

SehatSathi is a safety-first, offline-capable health education assistant designed for NGOs and community health programs. It provides **general health education and awareness only** and does not offer diagnosis, treatment, medication advice, or emergency guidance.

This project was built as a submission for the **MedGemma Impact Challenge** and demonstrates responsible use of open-weight models from Google’s **Health AI Developer Foundations (HAI-DEF)**.

---

##  Purpose & Scope

Many NGOs operate in low-resource environments with limited internet access and strict privacy requirements. While AI can help scale health education, unsafe or overreaching systems pose serious risks.

SehatSathi is intentionally scoped to:
-  Support **health education and awareness**
-  Run **locally** after initial setup
-  Preserve **user privacy**
-  Avoid clinical decision-making
-  Avoid diagnosis, prescriptions, or emergency advice

---

##  Safety-First Design

A core design principle of SehatSathi is that **safety is enforced before any model interaction**.

All user inputs are first passed through deterministic intent and safety checks:
- Requests related to diagnosis, medication, or emergency symptoms are **blocked**
- Only general, educational queries are routed to the language model
- All responses include explicit educational disclaimers

This ensures predictable, auditable behavior suitable for NGO use.

---

##  Model Usage

The system is architected to be compatible with **MedGemma instruction models** from Google’s HAI-DEF collection.

- Local testing uses a smaller Gemma-family instruction model for CPU feasibility
- The architecture supports direct MedGemma deployment where appropriate compute is available
- The application runs fully **offline after the initial model download**

The focus is on **responsible application**, not benchmark performance.

---

##  Project Structure
