import streamlit as st
import ollama
st.set_page_config(page_title="lazy & study hub", page_icon="🫥")
page = st.sidebar.radio("Menu", ["Planner", "Chat"])

if page == "Planner":
    st.title("😑 Study Planner")
    h = st.slider("Hours/day", 1, 24, 3)
    d = st.number_input("Days", 1, 60, 7)
    topics = st.text_input("Study topics")

    if st.button("Generate"):
        try:
            r = ollama.chat(model="qwen2.5", messages=[{
                "role": "user",
                "content": f"Create a study plan for {topics} in {h*d} hours."
            }])
            st.write(r["message"]["content"])
        except Exception as e:
            st.error(str(e))
else:
    st.title("💬 Study Chat")
    chat_message= st.text_input("")
    if st.button("Send"):
        try:
            r = ollama.chat(model="qwen2.5", messages=[{
                "role": "user",
                "content": f"{chat_message}."
            }])
            st.write(r["message"]["content"])
        except Exception as e:
            st.error(str(e))
#by Codeplan Sheikh Raed, Tanush Saluja, and Akhilesh Kumar Kushwaha