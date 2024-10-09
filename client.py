import streamlit as st
import requests as re


def get_groq_response(input_text):
    response = re.post (
                "http://localhost:8000/essay/invoke",
                json={"input": {"topic":input_text}}
            )

    return response.json()["output"]["content"]


def get_ollama_response(input_text):
    response = re.post (
                "http://localhost:8000/poem/invoke",
                json={"input": {"topic":input_text}}
            )

    return response.json()["output"]


# streamlit framework
st.title("LangChain Demo with Groq API and Ollama")
input_text1 = st.text_input('Write an essay on')
input_text2 = st.text_input('Write a poem on')


if input_text1:
    st.write(get_groq_response(input_text1))

if input_text2:
    st.write(get_ollama_response(input_text2))