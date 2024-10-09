from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from langserve import add_routes
import uvicorn
import os
from langchain_community.llms import Ollama
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(
    title="LangChain Server",
    version="1.0",
    description="A simple API server"
)

add_routes(
    app,
    ChatGroq(),
    path="/groq"
)

model = ChatGroq()
llm = Ollama(model="gemma:2b")

prompt1 = ChatPromptTemplate.from_template(
    "Write me an essay about {topic} under 100 words"
)

prompt2 = ChatPromptTemplate.from_template(
    "Write me an poem about {topic} under 100 words"
)

add_routes(
    app,
    prompt1 | model,
    path="/essay"
)

add_routes(
    app,
    prompt1 | llm,
    path="/poem"
)


if __name__=="__main__":
    uvicorn.run(app, host="localhost", port=8000)