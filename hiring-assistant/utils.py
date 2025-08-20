import os
from openai import OpenAI
import json
from prompts import question_prompt

# Initialize OpenAI
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_response(messages):
    response = client.chat.completions.create(
        model="gpt-4o-mini",  # or "gpt-3.5-turbo"
        messages=messages,
        max_tokens=300,
        temperature=0.6
    )
    return response.choices[0].message.content.strip()

def save_candidate_data(data, filename="candidates.json"):
    with open(filename, "a") as f:
        f.write(json.dumps(data) + "\n")

def generate_questions(tech_stack):
    prompt = question_prompt.format(tech_stack=tech_stack)
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "system", "content": prompt}],
        max_tokens=400,
        temperature=0.5
    )
    return response.choices[0].message.content.strip()
