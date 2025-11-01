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
from agents import Agent,Runner,OpenAIChatCompletionsModel
model = OpenAIChatCompletionsModel(
    openai_client=client,
    model=azure_openai_model_deployment
)
agent = Agent(
    name="Hello agent",
    instructions="You are a helpful assistant that greets the user.",
    model=model
)

#run agent
response=Runner.run_sync(agent, "hi there!")
print(response.final_output)
