# Cardápio Dinâmico — Containerizado com Docker

Aplicação web full-stack (Flask + PostgreSQL) totalmente containerizada com Docker e Docker Compose, publicada como imagem pública no Docker Hub, desenvolvida como projeto de estudo.

🔗 **Imagem pública:** `docker pull gabrielpe7/cardapio-flask`
🔗 **Versão ao vivo (Render):** https://cardapio-flask.onrender.com

## Funcionalidades

- Exibição de cardápio organizado por categoria, gerado dinamicamente via templates
- Formulário para adicionar novos itens diretamente pelo navegador
- Aplicação e banco de dados rodando em containers separados, orquestrados com Docker Compose
- Persistência de dados garantida por volume Docker, mesmo com containers recriados
- Imagem publicada publicamente no Docker Hub, pronta para ser baixada e executada em qualquer máquina

## Tecnologias utilizadas

- **Python 3 / Flask** (back-end e templates Jinja2)
- **PostgreSQL** (banco de dados relacional, via `psycopg2`)
- **Docker e Docker Compose** (containerização e orquestração)
- **HTML5 / CSS3**

## Estrutura do projeto

```
cardapio-flask/
├── main.py                # rotas e lógica da aplicação
├── banco.py                # persistência em PostgreSQL
├── requirements.txt
├── Dockerfile              # imagem da aplicação
├── docker-compose.yml      # orquestração da aplicação + banco de dados
├── templates/
│   └── index.html
└── static/
    └── style.css
```

## Sobre o projeto

Este projeto evoluiu em etapas até chegar à containerização completa:

1. **Aplicação web full-stack** — Flask, templates dinâmicos e banco de dados
2. **Deploy em nuvem** — publicação em produção via Render
3. **Containerização** — empacotamento da aplicação com Docker, garantindo execução idêntica em qualquer ambiente
4. **Orquestração multi-container** — uso de Docker Compose para rodar aplicação e banco de dados PostgreSQL como serviços conectados, com verificação de saúde (healthcheck) entre eles
5. **Publicação da imagem** — imagem disponibilizada publicamente no Docker Hub

## Como executar com Docker Compose

Pré-requisito: ter o [Docker Desktop](https://www.docker.com/products/docker-desktop/) instalado e em execução.

```bash
# Clone o repositório
git clone https://github.com/gabrielpe7/cardapio-flask.git
cd cardapio-flask

# Suba a aplicação e o banco de dados juntos
docker compose up --build
```

Acesse `http://localhost:5000`.

## Como executar apenas a imagem publicada

```bash
docker pull gabrielpe7/cardapio-flask
```

## Possíveis melhorias futuras

- Adicionar um serviço de cache (Redis) ao Compose
- Pipeline de CI/CD para build e push automáticos da imagem a cada atualização
- Orquestração em escala maior com Kubernetes

## Autor

Desenvolvido por Gabriel Pereira de Oliveira — estudante de Análise e Desenvolvimento de Sistemas.

[LinkedIn](#) · [GitHub](https://github.com/gabrielpe7)
