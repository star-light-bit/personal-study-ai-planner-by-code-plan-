# 🫥 Lazy & Study Hub — AI-Powered Student Study Planner

An interactive Python web application built with **Streamlit** and **Ollama (`qwen2.5`)** that helps students convert their available daily study hours, total days, and subject topics into a structured study plan, and ask follow-up questions in a built-in Study Chat.

* **Course:** Computational Thinking and Programming (`2026CSAE100`)
* **Institution:** Bennett University (School of Computer Science Engineering and Technology)
* **Academic Year:** 2026–27

---

## ✨ Features

* **Sidebar Navigation:** Switch cleanly between **Planner** and **Chat** modes using `st.sidebar.radio`.
* **Study Planner (`😑 Study Planner`):** Select daily study hours (`1–24` hours/day via `st.slider`), choose total study duration (`1–60` days via `st.number_input`), and enter study topics to automatically compute total available hours (`h * d`) and generate a tailored study schedule.
* **Study Chat (`💬 Study Chat`):** Interactive Q&A interface powered by `ollama.chat(model="qwen2.5", ...)` for clarifying concepts while studying.
* **Error Handling:** `try-except` blocks catch connection or model errors and display clear messages via `st.error(...)`.

---

## 📁 Project Structure

```text
student-study-planner-2026CSAE100/
├── codeplan_student_study_planner_ai_powered.py   # Main Streamlit application
├── README.md                                      # Project documentation
├── requirements.txt                               # Python dependencies (streamlit, ollama)
├── report/
│   └── Python_Project_Report_2026CSAE100.docx     # Prescribed project report
└── screenshots/                                   # App output screenshots
```

---

## ⚙️ Prerequisites

* **Python 3.9+** installed on your system
* **Ollama** installed locally from [ollama.com](https://ollama.com) with the `qwen2.5` model pulled

---

## 🚀 Installation & How to Run

1. **Install Python dependencies:**
   ```bash
   pip install streamlit ollama
   ```

2. **Pull the local LLM in Ollama:**
   ```bash
   ollama pull qwen2.5
   ```

3. **Run the Streamlit application:**
   ```bash
   streamlit run codeplan_student_study_planner_ai_powered.py
   ```

---

## 👥 Team Members (Team Codeplan)

| Name | Enrollment Number | Contribution |
| :--- | :--- | :--- |
| **Sheikh Raed Salah** | `S26CSEU2428` | Project idea, Planner & Chat workflow design, testing, and review |
| **Tanush Saluja** | `S26CSEU2319` | Streamlit UI implementation, input widgets, Ollama integration, and exception handling |
| **Akhilesh Kumar Kushwaha** | `S26CSEU2427` | General help, documentation, and overall project support |
