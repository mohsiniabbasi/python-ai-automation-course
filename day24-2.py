import anthropic
from dotenv import load_dotenv

load_dotenv()
client = anthropic.Anthropic()

question = input("Hi! I am Claude, ask me a question: ")
response = client.messages.create(
    model="claude-haiku-4-5",
    max_tokens=1000,
    messages=[{"role": "user", "content": question}],
)
answer = response.content[0].text
print(answer)