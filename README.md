# NagarikAI – Smart Bharat AI-Powered Civic Companion 🏛️

An intelligent, GenAI-powered web platform designed to bridge the gap between citizens and complex government machinery, promoting transparency, accessibility, and digital inclusion.

## 🔗 Submission Links
- **Working Deployed Web App:** (https://nagarikai-6fuxpwwkz9lvpquyrrx43n.streamlit.app/)
- **Public GitHub Repository:** (https://github.com/riasingh1234/NagarikAI)]

---

## ✨ Core Features

1. **💬 AI Civic Companion (Tab 1)**
   - Delivers accurate, conversational answers regarding central, state, and municipal procedures.
   - Instantly extracts structured document checklists and lists the relevant departments for a citizen's query.

2. **📄 Government Scheme Simplifier (Tab 2)**
   - Accepts complex, wordy government circulars or policy updates.
   - Parses the text and reconstructs it into high-readability blocks: *Overview, Eligibility, Benefits, and Application Steps*.

3. **🚨 Smart Grievance Redressal (Tab 3)**
   - Allows users to describe civic infrastructure problems (e.g., broken streetlights, water logging) in casual language.
   - Automatically re-writes the complaint into a formal municipal grievance letter.
   - Uses AI logic to categorize the issue into an appropriate civil department and generates a secure tracking ID.

---

## 🧠 GenAI Prompt Workflow & Strategy

To satisfy the hackathon requirements for a robust prompt design, NagarikAI implements a deterministic prompting strategy inside the Google Gemini framework:

* **Role-Based System Anchoring:** Every prompt initializes the LLM context by binding its persona to an *"Expert AI Civic Companion deeply knowledgeable about Indian government services."* This enforces professional decorum and stops the AI from hallucinating irrelevant or unsafe responses.
* **Strict Constraint Formatting:** Prompts utilize explicit structures (e.g., forcing a distinct `DEPARTMENT:` prefix block). This permits deterministic string parsing on the frontend while cleanly handling layout transitions.
* **Dynamic Multilingual Injection:** The application captures the user's UI language selection dynamically from the sidebar. The constraint `You must respond ENTIRELY in the {language} language... including headings and labels` is embedded into the core context matrix, delivering authentic localized output without needing slow secondary translation wrappers.

---

## 🛠️ Tech Stack & Deployment

- **Application Framework:** Streamlit (Python)
- **Generative AI Core:** Google Gemini API (`gemini-2.5-flash`)
- **Hosting Platform:** Streamlit Community Cloud
