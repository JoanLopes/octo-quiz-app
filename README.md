
## 🐙 Octo Quiz App – Backend + Web (Django)

**Octo Quiz App** é uma plataforma de estudos com quizzes interativos e rankings de desempenho. Esta versão foca no desenvolvimento do **backend em Django** com API REST e interface **web responsiva via Django admin ou templates**, ideal para uso por administradores, professores e alunos.

---

### 📚 Funcionalidades

* Cadastro e autenticação de usuários
* Criação e gerenciamento de quizzes
* Execução de quizzes com correção automática
* Pontuação e histórico de resultados por usuário
* Ranking geral de desempenho
* Interface administrativa via Django admin

---

## 🚀 Tecnologias utilizadas

* **Linguagem**: Python 3.10+
* **Framework**: Django 5.x + Django REST Framework
* **Banco de dados**: PostgreSQL
* **Ambiente**: Docker + Docker Compose
* **Gerenciador de pacotes**: pip

---

## ⚙️ Como rodar o projeto

### 🧾 Pré-requisitos

* [Docker](https://www.docker.com/)
* [Docker Compose](https://docs.docker.com/compose/)

### 🛠️ Passos de instalação

```bash
# 1. Clone o repositório
git clone https://github.com/joanlopes/octo-quiz-app.git
cd octo-quiz-app

# 2. Construa os containers
docker-compose up --build
```

### 🗃️ Migrações iniciais

```bash
docker-compose exec web python manage.py migrate
```

### 👤 Criar superusuário

```bash
docker-compose exec web python manage.py createsuperuser
```

---

## 🌐 Acessos

| Recurso                             | URL                                                        |
| ----------------------------------- | ---------------------------------------------------------- |
| API REST                            | [http://localhost:8000/api/](http://localhost:8000/api/)   |
| Django Admin                        | [http://localhost:8000/admin](http://localhost:8000/admin) |
| Navegação geral (se usar templates) | [http://localhost:8000/](http://localhost:8000/)           |

---

---

<!-- ## ✅ Status do projeto

| Etapa                       | Status                           |
| --------------------------- | -------------------------------- |
| Backend com Django REST     | ✅ Pronto/inicializado            |
| API de quizzes e categorias | ✅ Em desenvolvimento             |
| Interface admin web         | ✅ Disponível                     |
| Suporte a rankings          | ✅ Em progresso                   |
| Frontend mobile (Ionic)     | 🔜 Separado em outro repositório |

--- -->

## 📄 Licença

Este projeto está licenciado sob a [MIT License](LICENSE).

---

Se quiser, posso salvar este conteúdo em um arquivo `README.md`, ou complementar com instruções para testes automatizados, separação de settings (`dev`/`prod`), ou documentação da API. Deseja algum desses?
