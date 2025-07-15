import ollama

client = ollama.Client()

model = "tinyllama"  
prompt = "What is Python?"

response = client.generate(model=model, prompt=prompt)

print("Response from Ollama:")
print(response.response)