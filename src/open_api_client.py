import os
from openai import OpenAI
from dotenv import load_dotenv
#os - allows to manipulate files
#load_dotenv - allows to load environment from the files; can run as if you have the environment
#



# Load the .env file only once
dotenv_path = os.path.join(os.path.dirname(__file__), '..', '.env') #os.path... = allows you to join two paths 1)directory location of current file, then will do /env; passing in env; joining the name of the file
load_dotenv(dotenv_path=dotenv_path)#loads the dotenv makes the environment variables defined in .evn; makes available to current python process

# Initialize the client only once
_client_instance = None

def get_openai_client(): #check if this exists
    global _client_instance
    if _client_instance is None:
        api_key = os.getenv("OPENAI_API_KEY")
        org_id = os.getenv("OPENAI_ORG_ID").strip()
        _client_instance = OpenAI(api_key=api_key, organization=org_id)#will call openai to fetch instance of a client
    return _client_instance