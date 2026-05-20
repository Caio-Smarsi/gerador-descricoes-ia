from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

URL_BANCO_DADOS = "sqlite:///./historico.db"

engine = create_engine(URL_BANCO_DADOS, connect_args={"check_same_thread": False})

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

class DescricaoProduto(Base):
    __tablename__ = "descricoes"

    id = Column(Integer, primary_key=True, index=True) 
    nome_produto = Column(String, index=True)          
    texto_gerado = Column(String)