from fastapi import APIRouter,FastAPI
import os
from langchain_core.prompts import PromptTemplate
from langchain_openai import OpenAI
from pydantic import BaseModel

template = """Question: {question}

Answer: Let's think step by step."""

prompt = PromptTemplate.from_template(template)

class Payload(BaseModel):
    query: str
    api_key: str

app = FastAPI()

@app.get("/ping")
def health_check():
    return "healthy"

@app.post("/query")
def run_query(payload: Payload):
    llm = OpenAI(openai_api_key=payload.api_key)
    llm_chain = prompt | llm
    return llm_chain.invoke(payload.query)

