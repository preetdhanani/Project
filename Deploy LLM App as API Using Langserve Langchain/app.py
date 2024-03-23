from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langchain_community import chat_models
from langserve import add_routes
import uvicorn
from langchain_openai import ChatOpenAI
import os



os.environ['OPENAI_API_KEY'] = os.getenv("OPENAI_API_KEY")

app = FastAPI(
    title='Langchain Server',
    version='1.0',
    description='Simple API Server'
)

add_routes(
    app,
    ChatOpenAI(),
    path='/openai'
)

model = ChatOpenAI()
prompt = ChatPromptTemplate.from_template("provide an essay about {topic}")
prompt1 = ChatPromptTemplate.from_template("provide an poem about {topic}")

add_routes(
    app,
    prompt|model,
    path="/essay"
)

add_routes(
    app,
    prompt1|model,
    path="/poem"
)  


if __name__ == '__main__':
    uvicorn.run(app,host='localhost',port=8000)