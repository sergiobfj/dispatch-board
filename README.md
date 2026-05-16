# Dispatch Board

Painel de carregamento em tempo real para o almoxarifado da Virtron Energia Solar. Exibe os pedidos em andamento, próximos da fila e últimos concluídos em uma TV, substituindo o controle manual por papel.

---

## Funcionalidades

- Painel fullscreen para TV com atualização automática a cada 5s
- Painel administrativo para gerenciamento de pedidos
- Importação de pedidos via planilha Excel (.xlsx)
- Atualização de status (aguardando → em carregamento → concluído)

---

## Stack

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)

### Bibliotecas

![SQLModel](https://img.shields.io/badge/SQLModel-005571?style=for-the-badge&logo=fastapi&logoColor=white)
![openpyxl](https://img.shields.io/badge/openpyxl-217346?style=for-the-badge&logo=microsoftexcel&logoColor=white)
![Uvicorn](https://img.shields.io/badge/Uvicorn-499848?style=for-the-badge&logo=gunicorn&logoColor=white)

---

## Como rodar

1. Clone o repositório
```bash
   git clone https://github.com/sergiobfj/dispatch-board.git
   cd dispatch-board
```
2. Crie e ative o ambiente virtual
```bash
   python -m venv venv
   venv\Scripts\activate
```
3. Instale as dependências
```bash
   pip install -r requirements.txt
```
4. Inicie o servidor
```bash
   uvicorn main:app --reload
```

---

## Acesso

| Página | URL |
|---|---|
| Painel TV | http://localhost:8000/static/display.html |
| Painel Admin | http://localhost:8000/static/admin.html |
| API Docs | http://localhost:8000/docs |

---

## Estrutura do projeto

```
dispatch-board/
├── main.py
├── models.py
├── database.py
├── requirements.txt
├── routers/
│   └── orders.py
└── static/
    ├── display.html
    └── admin.html
```
