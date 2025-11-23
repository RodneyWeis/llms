import os
from dotenv import load_dotenv
import sys

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

from google import genai

client = genai.Client(api_key=api_key)
try:
	prompt = sys.argv[1]
except IndexError:
	print('Error: No command line argument provided')
	sys.exit(1)
		
print(prompt)

response = client.models.generate_content(model='gemini-2.0-flash-001', contents=prompt)
print(response.text)
print('Prompt tokens:', response.usage_metadata.prompt_token_count)
print('Response tokens:', response.usage_metadata.candidates_token_count)

def main():
    print("Hello from llms!")


if __name__ == "__main__":
    main()
