import os
from fastapi import FastAPI
from pydantic import BaseModel
import google.generativeai as genai
from dotenv import load_dotenv
from sqlalchemy.orm import Session
from database import SessionLocal, engine, Base, DescricaoProduto

load_dotenv()
CHAVE_API = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=CHAVE_API)

Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def gerar_descricao(produto: ProdutoRequest, db: Session = Depends(get_db)):
    novo_registro = DescricaoProduto(
        nome_produto=produto.nome,
        texto_gerado=resposta.text
    )
    db.add(novo_registro)  
    db.commit()            
    db.refresh(novo_registro) 


app = FastAPI(title="Gerador de Descrição IA")

class ProdutoRequest(BaseModel):
    nome: str
    caracteristicas: str = ""

@app.post("/gerar")
def gerar_descricao(produto: ProdutoRequest):
    
    modelo = genai.GenerativeModel("gemini-3-flash-preview")

    prompt = f"""Aja como um copywriter profissional de e-commerce.
    Crie uma descrição comercial muito atrativa para um produto chamado: '{produto.nome}'.
    Detalhes extras do produto: '{produto.caracteristicas}'.

    Retorne apenas um formato JSON válido com as seguintes chaves:
    - descrição: (Texto comercial)
    - categoria: (A qual categoria a loja pertence)
    - tags: (Uma lista com 3 palavras chave)
    """

    resposta = modelo.generate_content(prompt)     

    return {
        "status": "sucesso",
        "produto_recebido": produto.nome,
        "resposta_da_ia": resposta.text
    }  