import os
from fastapi import FastAPI, Depends
from pydantic import BaseModel
import google.generativeai as genai
from dotenv import load_dotenv
from sqlalchemy.orm import Session
from database import SessionLocal, engine, Base, DescricaoProduto
from fastapi.middleware.cors import CORSMiddleware

load_dotenv()
CHAVE_API = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=CHAVE_API)
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Gerador de Descrições IA")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # O asterisco significa "liberado para todos"
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ProdutoRequest(BaseModel):
    nome: str
    caracteristicas: str = ""

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/gerar")
def gerar_descricao(produto: ProdutoRequest, db: Session = Depends(get_db)):
    
    modelo = genai.GenerativeModel("gemini-3-flash-preview")
    prompt = f"""
    Aja como um copywriter profissional de e-commerce.
    Crie uma descrição comercial muito atrativa para um produto chamado: '{produto.nome}'.
    Detalhes extras do produto: '{produto.caracteristicas}'.
    
    Retorne APENAS um formato JSON válido com as seguintes chaves:
    - descricao:
    - categoria:
    - tags:
    """
    
    resposta = modelo.generate_content(
        prompt,
        generation_config={"response_mime_type": "application/json"}
    )
    
    novo_registro = DescricaoProduto(
        nome_produto=produto.nome,
        texto_gerado=resposta.text
    )
    
    db.add(novo_registro)
    db.commit()
    db.refresh(novo_registro)

    return {
        "status": "sucesso",
        "id_salvo_no_banco": novo_registro.id,
        "produto_recebido": produto.nome,
        "resposta_da_ia": resposta.text
    }