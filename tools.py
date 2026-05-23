from langchain.tools import tool
import requests
from bs4 import BeautifulSoup
from tavily import TavilyClient
import os
from dotenv import load_dotenv
from rich import print
load_dotenv()

tavily = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))
@tool
def web_search(query:str) -> str:
    """Search The web for recent and relaible imformation on a topic. Returns Titles, URL """
    results = tavily.search(query=query,max_result=3)

    out = []

    for r in results["results"]:
        out.append(
            f"title':{r['title']}\nURL: {r['url']}\nSnippet: {r['content'][:300]}\n"
        )

        return "\n----\n".join(out)

print(web_search.invoke("what is the recent news of war"))