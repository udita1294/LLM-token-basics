import os 
from pathlib import Path
from pyexpat.errors import messages
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

my_api_key = os.getenv("GROQ_API_KEY")
if not my_api_key:
    raise ValueError("API key not found")

client = Groq(api_key = my_api_key);

model = "llama-3.3-70b-versatile"
role = "user"
# 3 prompts
prompt1 = "Hi!"
prompt2 = "Explain time travel in detail."
prompt3 = "Write an essay on Machine learning in 100 words"

prompts = [prompt1, prompt2, prompt3]

for prompt in prompts:
    message = {
    "role" : role,
    "content" : prompt
    }
    messages = [message]

    response = client.chat.completions.create(model=model, messages=messages)
    answer = response.choices[0].message.content
    # print(answer)
    usage = response.usage
    print(f"Prompt : {prompt} --> tokens --> ,Prompt tokens: {usage.prompt_tokens}, Completion tokens: {usage.completion_tokens}, Total tokens: {usage.total_tokens}")
