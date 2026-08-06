# Cardápio Dinâmico com Flask

Sistema web para gerenciamento de cardápio, com back-end em Flask, banco de dados SQLite e páginas geradas dinamicamente via templates, desenvolvido como projeto de estudo.

## Funcionalidades

- Exibição do cardápio organizado por categoria, gerado automaticamente a partir do banco de dados
- Formulário para adicionar novos itens diretamente pelo navegador, sem editar código
- Interface estilizada com CSS, reaproveitando um design responsivo

## Tecnologias utilizadas

- **Python 3**
- **Flask** (framework web)
- **Jinja2** (templates dinâmicos, incluso no Flask)
- **SQLite** (via módulo `sqlite3`, nativo do Python)
- **HTML5 / CSS3**

## Estrutura do projeto

```
cardapio-flask/
├── main.py           # rotas e lógica da aplicação
├── banco.py          # funções de persistência em SQLite
├── templates/
│   └── index.html    # template da página, processado pelo Flask
└── static/
    └── style.css      # estilos da aplicação
```

## Sobre o projeto

Este projeto foi construído em etapas, unindo três áreas trabalhadas em projetos anteriores — back-end, banco de dados e front-end:

1. **Templates dinâmicos** — geração de HTML a partir de dados do Python, usando a sintaxe do Jinja2 (`{{ }}` para valores, `{% %}` para lógica)
2. **Persistência de dados** — itens do cardápio armazenados e consultados em banco de dados relacional
3. **Formulários web** — recebimento de dados enviados pelo usuário via HTML, sem uso de JSON/API
4. **Organização de arquivos estáticos** — separação entre templates e arquivos CSS, seguindo a convenção do Flask

## Como executar

Pré-requisito: ter o [Python 3](https://www.python.org/) instalado.

```bash
# Clone o repositório
git clone https://github.com/gabrielpe7/cardapio-flask.git

# Entre na pasta do projeto
cd cardapio-flask

# Instale as dependências
python -m pip install -r requirements.txt

# Execute o programa
python main.py
```

Acesse `http://127.0.0.1:5000` no navegador.

## Possíveis melhorias futuras

- Edição e exclusão de itens já cadastrados
- Upload de imagens dos pratos
- Painel administrativo com login (reaproveitando o sistema de autenticação de outro projeto)
- Deploy em um servidor real

## Autor

Desenvolvido por Gabriel Pereira de Oliveira — estudante de Análise e Desenvolvimento de Sistemas.

[LinkedIn](#) · [GitHub](https://github.com/gabrielpe7)
