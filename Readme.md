# SistemaEstoque

Sistema de controle de estoque desenvolvido em Python com conexão a banco de dados MySQL.  
Permite cadastrar, remover, atualizar e listar produtos do estoque de forma simples e orientada a objetos.

---

## Tecnologias usadas

- Python 3.x  
- MySQL  
- Biblioteca mysql-connector-python  

---

## Configuração do ambiente

1. Instale a biblioteca MySQL Connector para Python:

pip install mysql-connector-python

2. Configure o banco de dados MySQL com a estrutura de tabela:

USE EstoqueDB;

CREATE TABLE IF NOT EXISTS Produtos (
    Codigo VARCHAR(20) PRIMARY KEY,
    Nome VARCHAR(100) NOT NULL,
    Quantidade INT NOT NULL DEFAULT 0,
    Preco DECIMAL(10, 2) NOT NULL,
    Setor VARCHAR(50),
    Prateleira VARCHAR(50)
);

3. Configure a variável de ambiente com a senha do MySQL:

No Windows (Prompt de Comando):

set DB_SENHA=sua_senha_aqui



---

## Como rodar

1. Clone este repositório:

git clone https://github.com/dias-byte/SistemaEstoque.git

2. Acesse a pasta do projeto:

cd SistemaEstoque

3. Execute o programa:

python estoquePOO.py

---

## Funcionalidades

- Adicionar produto  
- Remover produto  
- Atualizar quantidade  
- Listar todos os produtos  
- Buscar produto por nome  

---

## Autor

Helbert Dias Filho  

https://github.com/dias-byte