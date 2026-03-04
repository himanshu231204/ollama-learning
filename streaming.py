from ollama import chat

stream = chat(
    model="mistral",
    messages=[{"role": "user", "content": "What is 17 × 23?"}],
    stream=True,
)

content = ""

for chunk in stream:
    if chunk.message.content:
        print(chunk.message.content, end="", flush=True)
        content += chunk.message.content

print("\n\nFinal Answer:", content)