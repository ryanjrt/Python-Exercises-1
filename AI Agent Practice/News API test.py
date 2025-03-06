import json, os
import urllib.parse
import requests

from typing import List
from openai import OpenAI
from pydantic import BaseModel, Field

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def get_news_headlines(query, searchin, start_date, rank, page_size):
    
    # Encode parameters
    params = {
        'q' : query,
        'searchIn' : searchin,
        'date' : start_date,
        'sortBy' : rank,
        'pageSize' : page_size,
        'apiKey' : "efcac2e2900c4b1f81fea1705ec84b47"
        }

    encoded_params = urllib.parse.urlencode(params)
    
    # Construct GET request    
    base_url = "https://newsapi.org/v2/everything"
    full_url = f"{base_url}?{encoded_params}"
    
    # Submit GET request and extract response
    response = requests.get(full_url)
    print(params)
    if response.status_code == 200:
        
        print("Request successful")   
        data = response.json()
        return data
    else:
        print(f"Request failed, status code: {response.status_code}")
        

system_prompt = "You are a news summarizer that extracts news headlines and summarizes them in a matter-of-fact tone."

messages = [
    {"role": "system", "content": system_prompt},
    {"role": "user", "content": f"What are the headlines for US tariffs saying on 5 March 2025? Only retrieve the top 10 headlines."},
]

tools = [
    {
        "type": "function",
        "function": {
            "name": "get_news_headlines",
            "description": "Extract a list of news headlines for the user's query.",
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {"type": "string", "description": "The search query to filter news articles (e.g., crypto, technology)."},
                    "searchin": {"type": "string", "description": "Where to search for the query. Default is title."},
                    "start_date": {"type": "string", "description": "A date for the oldest article allowed."},
                    "rank": {"type": "string", "description": "The order to sort results by (e.g., relevancy, popularity)."},
                    "page_size": {"type": "integer", "description": "The maximum number of headlines to display per page. Default to 10."}
                },
                "required": ["query", "searchin", "start_date", "rank", "page_size"],
                "additionalProperties": False,
            },
            "strict": True,
        },
    }
]

completion = client.chat.completions.create(
    model="gpt-4o",
    messages=messages,
    tools=tools,
)

completion.model_dump()

def call_function(name, args):
    if name == "get_news_headlines":
        return get_news_headlines(**args)

    
for tool_call in completion.choices[0].message.tool_calls:
    name = tool_call.function.name
    args = json.loads(tool_call.function.arguments)
    messages.append(completion.choices[0].message)

    result = call_function(name, args)
    messages.append(
        {"role": "tool", "tool_call_id": tool_call.id, "content": json.dumps(result)}
    )
    
class NewsResponse(BaseModel):
    summary: str = Field(description="A short paragraph summarizing the news headlines.")
    sources: int = Field(description="The number of news headlines summarized.")
    
completion_2 = client.beta.chat.completions.parse(
    model="gpt-4o",
    messages=messages,
    tools=tools,
    response_format=NewsResponse,
)

final_response = completion_2.choices[0].message.parsed
final_response.summary
final_response.sources

print(final_response.summary)

total_tokens = completion.usage.total_tokens +completion_2.usage.total_tokens
print(f"Total tokens expended: {total_tokens}")