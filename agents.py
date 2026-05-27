from langchain import hub
from langchain.agents import create_react_agent, AgentExecutor
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from tools import web_search, scrape_url
import os
from dotenv import load_dotenv

load_dotenv()
llm = ChatOpenAI(model = "gpt-40-mini", temperature=0)


#1st agent
def build_search_agent():
    return create_agent(
        model = llm
        tools= [web_search]
    )