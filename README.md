
# Delicada e Feminina 💅✨

Bem-vindo ao repositório oficial do **Delicada e Feminina**, uma loja virtual de cosméticos desenvolvida com Django e Bootstrap. A plataforma permite que clientes explorem produtos de beleza e skincare, adicionem itens ao carrinho e finalizem pedidos de forma prática, rápida e elegante.

## 💡 Sobre o Projeto

O **Delicada e Feminina** foi criado com o objetivo de oferecer uma experiência de compra online pensada especialmente para quem ama se cuidar. Com uma interface amigável, moderna e responsiva, o site proporciona facilidade de navegação e uma jornada de compra agradável.

Este projeto é uma adaptação do sistema **Web Shop**, aplicado agora ao ramo de cosméticos e cuidados pessoais.

### 🔗 Integração com o Sales_Hub

Assim como o Web Shop, o **Delicada e Feminina** está **integrado ao sistema [Sales_Hub]**, responsável pela **gestão de estoque**. Isso permite manter os produtos atualizados automaticamente, controlar as vendas e evitar inconsistências nas quantidades disponíveis.

## 🛠 Tecnologias Utilizadas

- **Python 3.11**
- **Django 4.x**
- **Bootstrap 5**
- **HTML5 e CSS3**
- **SQLite** (desenvolvimento)
- **Docker** (desenvolvimento)

## 💎 Funcionalidades

- Página inicial com produtos em destaque
- Filtro de cosméticos por categoria
- Carrinho de compras com total dinâmico
- Envio de pedidos via WhatsApp
- Sistema de autenticação para administradores
- Painel administrativo para gerenciar produtos e pedidos
- Layout responsivo para celulares e computadores

## 📝 Arquivo `.env`

Para rodar o projeto localmente ou em produção, configure o arquivo `.env` com as seguintes variáveis:

```
SECRET_KEY=
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1,

POSTGRES_DB=
POSTGRES_USER=
POSTGRES_PASSWORD=
POSTGRES_HOST=
POSTGRES_PORT=5432
PORT=8000

WHATSAPP_NUMBER=
EXTERNAL_API_URL=
```

> **Nota:** Substitua os valores vazios pelas configurações correspondentes ao seu ambiente.

## 🚀 Como Executar Localmente

1. Clone o repositório:

   ```bash
   git clone https://github.com/KaioHerculano/delicada_e_feminina
   cd delicada_e_feminina
   ```

2. Crie e ative um ambiente virtual:

   ```bash
   python -m venv venv
   source venv/bin/activate  # ou venv\Scripts\activate no Windows
   ```

3. Instale as dependências:

   ```bash
   pip install -r requirements.txt
   ```

4. Realize as migrações e execute o servidor:

   ```bash
   python manage.py migrate
   python manage.py runserver
   ```

5. Acesse: `http://127.0.0.1:8000`

## 😋 Contribuindo

Contribuições são muito bem-vindas! Caso tenha sugestões de melhorias, abra uma *issue* ou envie um *pull request*.
