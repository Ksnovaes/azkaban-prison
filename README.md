# Projeto Final - Programação Web
Esse repositório contém uma aplicação fullstack voltada para um projeto de faculdade, é um projeto básico contendo um CRUD.

## Tecnologias utilizadas
- **PostgreSQL:** banco de dados relacional flexível e eficiente
- **FastAPI:** framework para aplicações web
- **SQLAlchemy:** ORM para aplicações em python

## Configuração local- **Siga os passos abaixo:**
**1.** Clone o repositório:
```bash
git clone https://github.com/Ksnovaes/azkaban-prison.git
```
**2.** Construir as imagens Docker e iniciar os contêineres:
```bash
docker-compose up --build -d
```
**3.** Parar os contêineres:
```bash
docker-compose down
```

Você pode acessar a aplicação em http://localhost:7777

## Endpoints
**Juiz**
- **GET /juiz** - com esse endpoint você consegue verificar a página de cadastro de juiz
- **POST /addjuiz** - com esse endpoint você consegue cadastrar um juiz

**Sentenciado**
- **GET /sentenciado** - com esse endpoint você consegue verificar a página de cadastro de sentenciados
- **POST /addsentenciado** - com esse endpoint você consegue cadastrar sentenciados
- **GET /sentencas** - com esse endpoint você consegue ver a lista dos sentenciados que você cadastrou
    - **PUT** /:id - com esse endpoint você pode fazer o update de algum sentenciado que você cadastrou
    - **DELETE** /:id - com esse endpoint você pode fazer o delete de algum sentenciado que você cadastrou