from fastapi import FastAPI
import Summarization
import Generation

app = FastAPI()

@app.get("/")
def read_root():
    return {'Hello': 'World!'}

@app.get("/summarization/{text}")
def summary(text: str):
    return Summarization.query({"inputs": text})

@app.get("/generation/{text}/{answer}")
def generate(text: str, answer: str):
    return Generation.query({"inputs": text+'<unused0>'+answer})