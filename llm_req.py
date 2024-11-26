from openai import OpenAI
import os
from dotenv import load_dotenv
import streamlit as st

def get_questions(client, relevant_entries):
    completion = client.chat.completions.create(
        messages=[
                {
                    "role": "assistant",
                    "content": f"""
                        you are my therapist. Ask me a relevant question to help me reflect on my recent experiences.
                        Here are my relevant journal entries as context: {relevant_entries}
                    """,
                }
            ],
        model="gpt-4o",
    )

    return completion

def get_chat_bot(relevant_entries):
    load_dotenv()

    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    if "messages" not in st.session_state:
        st.session_state.messages = []
    if "set_context" not in st.session_state:
        st.session_state.set_context = False

    # Handle user input
    if not st.session_state.set_context:
        chat_completion = get_questions(client, relevant_entries)
        st.session_state.messages.append(
            {"role": "assistant", "content": chat_completion.choices[0].message.content}
        )
        st.session_state.set_context = True

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("What is up?"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # Send prompt to Groq API
        with st.chat_message("assistant"):
            response = client.chat.completions.create(
                model="gpt-4o",
                messages=[
                    {"role": m["role"], "content": m["content"]}
                    for m in st.session_state.messages
                ]
            )
            # Display response
            st.markdown(response.choices[0].message.content)
        st.session_state.messages.append(
            {"role": "assistant", "content": response.choices[0].message.content}
        )
