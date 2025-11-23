import os
from dotenv import load_dotenv
import sys
from google import genai
from google.genai import types

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")


client = genai.Client(api_key=api_key)
verbose = ''
try:
	user_prompt = sys.argv[1]
except IndexError:
	print('Error: No command line argument provided')
	sys.exit(1)

try:
	verbose = sys.argv[2]
except IndexError:
	pass

messages = [
    types.Content(role="user", parts=[types.Part(text=user_prompt)]),
]

response = client.models.generate_content(model='gemini-2.0-flash-001', contents=messages,)
print(response.text)
if verbose == '--verbose':
	print('User prompt:', user_prompt)
	print('Prompt tokens:', response.usage_metadata.prompt_token_count)
	print('Response tokens:', response.usage_metadata.candidates_token_count)

def main():
    print("Hello from llms!")


if __name__ == "__main__":
    main()
