"""
Main Streamlit application.
"""

import streamlit as st
from langchain_core.messages import HumanMessage, AIMessage
from graph.workflow import graph

st.set_page_config(
    page_title="EngagePro Chatbot",
    page_icon="🤖",
    layout="centered",
)

st.title("🤖 EngagePro Chatbot")

st.caption("An AI assistant for EngagePro.")

# -----------------------------
# Sidebar
# -----------------------------
with st.sidebar:
    st.header("⚙️ Settings")

    st.write("Provider")
    st.info("OpenAI")

    st.write("Model")
    st.info("GPT-4.1")

    st.write("Temperature")
    st.info("0.2")

# -----------------------------
# Session State
# -----------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# -----------------------------
# Display Chat History
# -----------------------------
for message in st.session_state.messages:

    if isinstance(message, HumanMessage):
        with st.chat_message("user"):
            st.write(message.content)

    elif isinstance(message, AIMessage):
        with st.chat_message("assistant"):
            st.write(message.content)

# -----------------------------
# Chat Input
# -----------------------------
if prompt := st.chat_input("Ask me anything..."):

    # Add the user's message
    st.session_state.messages.append(
        HumanMessage(content=prompt)
    )

    # Send the conversation to LangGraph
    response = graph.invoke(
        {
            "messages": st.session_state.messages
        }
    )

    # Get the assistant's reply
    assistant_message = response["messages"][-1]

    # Save it
    st.session_state.messages.append(
        assistant_message
    )

    # Refresh the page
    st.rerun()