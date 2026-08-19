# 🤖 Copywriter IA - Gerador de Descrições Comerciais

Uma aplicação web (SaaS) completa que utiliza Inteligência Artificial para gerar descrições de produtos otimizadas para SEO, projetada com uma arquitetura moderna e desacoplada.

## 🌐 Demonstração (Live)

Aceda à aplicação a funcionar aqui: [Gerador de Descrições IA](https://caio-smarsi.github.io/gerador-descricoes-ia/)

> **Nota:** Como o backend está alojado num serviço gratuito (Render), o primeiro pedido pode demorar até 50 segundos para "acordar" o servidor. Os pedidos subsequentes serão rápidos.

## 🏛️ Arquitetura do Sistema

O projeto adota uma arquitetura de API RESTful com o Front-end totalmente desacoplado do Back-end.

- **Front-end (Client):** Interface HTML estática interativa com TailwindCSS puro e JavaScript assíncrono (Vanilla JS). Consome diretamente a API na nuvem via `fetch`. Hospedado no GitHub Pages.
- **Back-end (API):** Desenvolvido em Python utilizando FastAPI. Responsável por receber os dados, processar a integração com o modelo de IA e formatar a resposta. Hospedado no Render.
- **Inteligência Artificial:** Integração via API com o modelo `gemini-1.5-flash` (Google Generative AI) para processamento de linguagem natural.
- **Persistência de Dados:** Banco de dados SQLite local mapeado via ORM (SQLAlchemy) para guardar o histórico de interações.

## 🛠️ Tecnologias Utilizadas

- **Python (>=3.11):** Linguagem base.
- **Poetry:** Gestão rigorosa de dependências e ambientes virtuais (`pyproject.toml`).
- **FastAPI:** Framework assíncrono de alta performance para a construção da API.
- **Pydantic:** Validação de dados rigorosa e tipagem.
- **SQLAlchemy:** Mapeamento Objeto-Relacional (ORM) para a base de dados.
- **Google Generative AI SDK:** Comunicação nativa com a LLM do Google.
- **HTML/TailwindCSS:** Interface de utilizador minimalista e responsiva.

## 🚀 Como Executar Localmente

### Pré-requisitos

1. Python (>= 3.11) instalado.
2. Poetry instalado (`pip install poetry`).
3. Uma chave de API válida do Google AI Studio.

### Instalação

1. Clone o repositório:

   ```bash
   git clone https://github.com/Caio-Smarsi/gerador-descricoes-ia.git
   cd gerador-descricoes-ia
   ```

2. Instale as dependências:

   ```bash
   poetry install
   ```

3. Configure o Ambiente: Copie o ficheiro de exemplo `.env.example` e crie um ficheiro `.env` na raiz do projeto com a sua chave de API:

   ```
   GEMINI_API_KEY=sua_chave_aqui
   ```

### Execução

Inicie o servidor de desenvolvimento (Uvicorn) através do Poetry:

```bash
poetry run uvicorn main:app --reload
```

A API estará disponível em `http://127.0.0.1:8000`. Pode aceder à documentação interativa (Swagger) em `http://127.0.0.1:8000/docs`.

Para testar a interface completa, abra o ficheiro `index.html` diretamente no seu navegador localmente, garantindo que o URL na função `fetch` do JavaScript aponta para o seu servidor local.

## 👤 Autoria

Desenvolvido e criado por **Caio Smarsi**.

> **Nota sobre uso de IA:** Este é um projeto acadêmico. O uso de Inteligência Artificial (Gemini Pro) neste projeto é exclusivamente educativo/funcional - como parte da funcionalidade da aplicação (geração de descrições) - não tendo sido utilizado para gerar nenhuma linha de código do projeto.