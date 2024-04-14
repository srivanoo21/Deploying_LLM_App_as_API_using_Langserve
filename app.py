from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
from langchain_community.chat_models import ChatOpenAI
from langserve import add_routes
import uvicorn
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")

# Check if the API key is set
if openai_api_key is None:
    raise ValueError("OpenAI API key is not set")

# Set the OpenAI API key in the environment
os.environ['OPENAI_API_KEY'] = openai_api_key


# Creating a FastAPI application instance named app
app=FastAPI(
    title="Langchain Server",
    version="1.0",
    description="A simple API Server"
)


# It creates an instance of the ChatOpenAI model, likely used to interact with ChatGPT for essay 
# and poem generation
model = ChatOpenAI()

# Defining a prompt for essay generation
prompt1 = ChatPromptTemplate.from_template("provide me an essay about {topic}")

# Defining a prompt for poem generation
prompt2 = ChatPromptTemplate.from_template("provide me a poem about {topic}")


# Adding Routes for ChatGPT Interaction
add_routes(
    app,
    model,
    path="/openai"
)

# Using add_routes to define routes under the path /essay
add_routes(
    app,
    prompt1|model,
    path="/essay"
)

# Using add_routes to define routes under the path /poem
add_routes(
    app,
    prompt2|model,
    path="/poem"
)



if __name__=="__main__":
    uvicorn.run(app, host="localhost", port=8000)