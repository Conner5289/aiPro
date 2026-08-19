import argparse
import os

from dotenv import load_dotenv
from openai import OpenAI

_ = load_dotenv()
api_key = os.environ.get("OPENROUTER_API_KEY")

parser = argparse.ArgumentParser(description="Chatbot")
_ = parser.add_argument("user_prompt", type=str, help="User prompt")
_ = parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
args = parser.parse_args()
# Now we can access `args.user_prompt`

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key,
)

messages = [
    {"role": "user", "content": args.user_prompt},
]

response = client.chat.completions.create(
    model="openrouter/free",
    messages=messages,
)

print(response.choices[0].message.content)
if args.verbose:
    print("User prompt:", args.user_prompt)
    print("Prompt tokens: ", response.usage.prompt_tokens)  # pyright: ignore[reportOptionalMemberAccess]
    print("Response tokens: ", response.usage.completion_tokens)  # pyright: ignore[reportOptionalMemberAccess]
