# take the input from the user and make a simple calcutaor 
from ollama import chat
response = chat(
    model="mistral",
    messages=[{"role": "user", "content": "What is 17 × 23?"}],
    stream=True,
)

content = ""

for chunk in response:
    if chunk.message.content:
        print(chunk.message.content, end="", flush=True)
        content += chunk.message.content

print("\n\nFinal Answer:", content)
print("Done.")
print("Done.")
print("Done.")
print("Done.")
print("Done.")
print("Done.")
print("Done.")
print("Done.")
print("Done.")