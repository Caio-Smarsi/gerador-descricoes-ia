import os
import google.generativeai as genai
from dotenv import load_dotenv

# Carrega a sua chave do .env
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

print("--- BUSCANDO MODELOS AUTORIZADOS ---")

# Pergunta ao Google quais modelos estão disponíveis para gerar texto
for modelo in genai.list_models():
    if 'generateContent' in modelo.supported_generation_methods:
        print(modelo.name)

print("------------------------------------")