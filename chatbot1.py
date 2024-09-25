#basic chatbot on terminal

import google.generativeai as genai
from decouple import config

# Configure the API key for Gemini 1.5 Flash
GOOGLE_API_KEY = config('GOOGLE_API_KEY')
genai.configure(api_key=GOOGLE_API_KEY)

# Function to generate response using Gemini 1.5 Flash
def generate_response(prompt):
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content(prompt)
    return response.text

prompt=input("Enter your question:")
print(generate_response(prompt))
