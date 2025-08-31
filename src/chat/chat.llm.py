from typing import Dict, Generator
import streamlit as st

import ollama

# ------------------------------------------------------------------------------
st.title("ChatGPT-like clone")

def ollama_generator(model_name: str, messages: Dict) -> Generator:
    stream = ollama.chat(
        model=model_name, messages=messages, stream=True)
    
    for chunk in stream:
        yield chunk['message']['content']


def get_response(
    prompt=None, messages=None, model="phi4-mini", stream=False
) -> ollama.ChatResponse:
    if messages is None:
        messages = (
            [
                {
                    "role": "user",
                    "content": prompt,
                },
            ],
        )

    response = ollama.chat(
        model=model,
        messages=messages,
        stream=stream,
    )

    # No Streaming:
    # print(response.message.content)

    # Streaming:
    # for chunk in stream:
    #     print(chunk["message"]["content"], end="", flush=True)
    #     return response

    return response


# ------------------------------------------------------------------------------
if "selected_model" not in st.session_state:
    st.session_state.selected_model = ""
    

if "messages" not in st.session_state:
    st.session_state.messages = []

st.session_state.selected_model = st.selectbox(
    "Please select the model:", [model["model"] for model in ollama.list()["models"]])

# ------------------------------------------------------------------------------
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("How could I help you?"):
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        response = st.write_stream(ollama_generator(
            st.session_state.selected_model, st.session_state.messages))
        
    st.session_state.messages.append(
        {"role": "assistant", "content": response})
    