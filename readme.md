# env variables
AZURE_OPENAI_ENDPOINT="https://&lt;azure openai resourcename&gt;.openai.azure.com/"
go to ai.azure.com/for the azure ai foundry project/overview/libraries/azure openai/ paste azure openai endpoint (not azure ai foundry project endpoint)

AZURE_OPENAI_API_KEY= in the same path as above, copy the api key and paste here

AZURE_OPENAI_MODEL_DEPLOYMENT=in the same path as above, then click, models and endpoints, deploy a model, then copy  its deployment name and paste here eg."gpt-4o-mini" 

AZURE_API_VERSION=in the same path as above, under libraries, go to api documentation, search for api lifecycle and find the latest version of the api..Note this is api version not the model version.eg: "2025-04-01-preview"


# output
Hello! How can I assist you today?
OPENAI_API_KEY is not set, skipping trace export

# pip install 
python -m venv .venv
pip install python-dotenv openai openai-agents 