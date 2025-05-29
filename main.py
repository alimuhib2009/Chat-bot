from agents import Agent, AsyncOpenAI, OpenAIChatCompletionsModel, Runner, set_tracing_disabled
from agents.run import RunConfig
import os
from dotenv import load_dotenv
import streamlit as st
# import pandas as pd
import asyncio



st.header("welcome to wrok")

set_tracing_disabled(disabled = True)

load_dotenv()

API_KEY = os.environ.get("GEMINI_API_KEY")


external_client = AsyncOpenAI(
    api_key=API_KEY,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client = external_client,
)

config = RunConfig(
    model = model,
    model_provider = external_client,
    tracing_disabled = True,
)

agent = Agent(name = "Assistant", instructions = "You are a helpful assistant")

message = st.text_input(label="Enter your Question", placeholder="Write your Message here...")

result = asyncio.run(Runner.run(agent, message , run_config=config))

print(result.final_output)

st.success(result.final_output)

st.warning("Developed by Ali Muhib")