import streamlit as st
from prompts import system_prompt, question_prompt
from utils import generate_response, save_candidate_data
import re

st.set_page_config(page_title="TalentScout Hiring Assistant", page_icon="🤖")

st.title("🤖 TalentScout Hiring Assistant")
st.write("Welcome! I am here to collect your details and ask some technical questions.")

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "system", "content": system_prompt}]
if "candidate_data" not in st.session_state:
    st.session_state.candidate_data = {}

# Chat input
user_input = st.chat_input("Type your message...")

if user_input:
    if user_input.lower() in ["bye", "exit", "quit"]:
        st.write("✅ Thank you for your time. We’ll get back to you with next steps.")
        save_candidate_data(st.session_state.candidate_data)
        st.stop()

    # Append user input
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Generate assistant response
    response = generate_response(st.session_state.messages)
    st.session_state.messages.append({"role": "assistant", "content": response})

# Display messages
for msg in st.session_state.messages[1:]:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])
