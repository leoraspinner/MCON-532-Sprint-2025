from src.open_api_client import get_openai_client
from pprint import pprint

client = get_openai_client()
pprint(vars(client))

# Make a request to OpenAI API
completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "Why did WW2 start?"
         },
        {"role": "user", "content": "respond to a young child"}
    ]
)
# Output the response
pprint(completion)
pprint(completion.choices[0].message.content)