# 📚 Flashcards App

Aplicativo web de estudos com **flashcards**, construído com **Django + DRF**, **Alpine.js**, e **Tailwind CSS**. Possui API REST autenticada via JWT e interface web moderna.

## 🐳 Rodando com Docker

### 1. Clone o repositório

```bash
git clone https://github.com/seuusuario/flashcards-app.git
cd flashcards-app
```

### 2. Construa os containers

```bash
docker-compose build
```

### 3. Suba os containers

```bash
docker-compose up
```

O app estará disponível em: [http://localhost:8000](http://localhost:8000)

---

## ⚙️ Comandos úteis (com Docker)

### Acessar o container

```bash
docker-compose exec web bash
```

### Criar superusuário

```bash
docker-compose exec web python manage.py createsuperuser
```

### Aplicar migrações

```bash
docker-compose exec web python manage.py migrate
```

### Coletar arquivos estáticos (produção)

```bash
docker-compose exec web python manage.py collectstatic
```

---

## 🧠 Funcionalidades

- CRUD de **decks** e **flashcards**
- Upload de imagens para flashcards
- Estudo interativo de flashcards
- Interface web com Tailwind + Alpine.js
- API RESTful protegida por JWT
- Documentação Swagger e ReDoc

---

## 🔐 Autenticação (JWT)

- Obter token:
  ```
  POST /api/token/
  ```
- Refresh token:
  ```
  POST /api/token/refresh/
  ```
- As requisições autenticadas usam:
  ```
  Authorization: Bearer <access_token>
  ```

---

## 📄 Documentação da API

- Swagger: [http://localhost:8000/swagger/](http://localhost:8000/swagger/)
- ReDoc: [http://localhost:8000/redoc/](http://localhost:8000/redoc/)

---

## 📁 Estrutura do Projeto

```bash
flashcards-app/
├── flashcards/             # App principal com os modelos e API
├── mainsite/               # Autenticação e páginas principais
├── media/                  # Uploads de imagens (flashcards)
├── static/                 # Arquivos estáticos (via collectstatic)
├── templates/              # HTML com Tailwind + Alpine.js
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
└── manage.py
```

---

## ✅ Testes

Execute os testes dentro do container:

```bash
docker-compose exec web python manage.py test
```

---

## 📱 Versão Mobile

A versão mobile está sendo construída com:

- Ionic + Angular
- Comunicação com a API Django via JWT

---

## 📌 Requisitos

- Docker
- Docker Compose

---

## 📄 Licença

MIT License
```
