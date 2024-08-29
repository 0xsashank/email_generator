import ollama

client = ollama.Client()

def chat(message, history):
    prompt = f"User: {message}\nAI:"
    response = client.generate(model='llama3', prompt=prompt)
    history.append((message, response['response']))
    return "", history
