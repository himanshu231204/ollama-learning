import ollama


response = ollama.generate(
    model="mistral",
    prompt='what is the capital of France?'
)

print(response)