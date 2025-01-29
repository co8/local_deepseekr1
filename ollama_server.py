from ollama import OllamaClient
import os
#from dotenv import load_dotenv
    
# Load environment variables from .env file
#load_dotenv()

# Initialize Ollama client
client = OllamaClient()
client.set_model('deepseek-r1:8b')

@app.route('/')

def home():
  return "Ollama Chatbot"

@app.route('/api/chat')

def chat():
  if request.method == 'POST':
    data = request.get_json()
  response = client.chat(**data)
