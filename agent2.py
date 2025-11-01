from dotenv import load_dotenv
load_dotenv()
import os
azure_openai_api_key = os.getenv("AZURE_OPENAI_API_KEY")
azure_openai_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
azure_openai_model_deployment = os.getenv("AZURE_OPENAI_MODEL_DEPLOYMENT")
azure_api_version = os.getenv("AZURE_API_VERSION")

#create client
from openai import AsyncAzureOpenAI
client = AsyncAzureOpenAI(
    api_key=azure_openai_api_key,
    azure_endpoint=azure_openai_endpoint,
    api_version=azure_api_version,
)

#create agent
from agents import Agent,Runner,OpenAIChatCompletionsModel,set_tracing_disabled
set_tracing_disabled(True)
model = OpenAIChatCompletionsModel(
    openai_client=client,
    model=azure_openai_model_deployment
)

from tools import get_weather

from pydantic import BaseModel
class WeatherRequest(BaseModel):
    location: str
    temp_unit: str = "Celsius"
    temp_value: float = None

agent = Agent(
    name="Hello agent",
    instructions="You are a helpful assistant.",
    model=model,
    tools=[get_weather],
    output_type=WeatherRequest
)

#run agent
response=Runner.run_sync(agent, "what is the weather in Seattle?")
print(response.final_output)
