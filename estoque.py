import os
import mysql.connector
from produto import Produto

import mysql.connector

class Estoque:
    def __init__(self):
        senha = 'fh1120hdf2005'  # ou use a variável de ambiente
        self.conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password=senha,
            database='EstoqueDB'
        )
        if self.conn.is_connected():
            print("Conectado ao banco EstoqueDB com sucesso!")
        else:
            print("Falha na conexão com o banco de dados.")
        self.cursor = self.conn.cursor()

# Teste rápido para ver se conecta:
if __name__ == "__main__":
    estoque = Estoque()


    def adicionar_produto(self, produto):
        try:
            sql = "INSERT INTO Produtos (Codigo, Nome, Quantidade, Preco, Setor, Prateleira) VALUES (%s, %s, %s, %s, %s, %s)"
            valores = (produto.codigo, produto.nome, produto.quantidade, produto.preco, produto.setor, produto.prateleira)
            self.cursor.execute(sql, valores)
            self.conn.commit()
            print(f"Produto '{produto.nome}' adicionado com sucesso!\n")
        except mysql.connector.IntegrityError:
            print("Erro: Produto com esse código já existe.\n")
        except mysql.connector.Error as err:
            print(f"Erro ao adicionar produto: {err}\n")

    def remover_produto(self, codigo):
        sql = "DELETE FROM Produtos WHERE Codigo = %s"
        self.cursor.execute(sql, (codigo,))
        self.conn.commit()
        if self.cursor.rowcount > 0:
            print("Produto removido com sucesso!\n")
        else:
            print("Produto não encontrado.\n")

    def atualizar_quantidade(self, codigo, nova_quantidade):
        sql = "UPDATE Produtos SET Quantidade = %s WHERE Codigo = %s"
        self.cursor.execute(sql, (nova_quantidade, codigo))
        self.conn.commit()
        if self.cursor.rowcount > 0:
            print("Quantidade atualizada com sucesso!\n")
        else:
            print("Produto não encontrado.\n")

    def buscar_por_nome(self, nome_busca):
        sql = "SELECT Codigo, Nome, Quantidade, Preco, Setor, Prateleira FROM Produtos WHERE LOWER(Nome) LIKE %s"
        like_pattern = f"%{nome_busca.lower()}%"
        self.cursor.execute(sql, (like_pattern,))
        resultados = self.cursor.fetchall()

        if resultados:
            print("\nProdutos encontrados:")
            for linha in resultados:
                p = Produto(*linha)
                print(p)
        else:
            print("Nenhum produto encontrado com esse nome.\n")

    def listar_todos(self):
        sql = "SELECT Codigo, Nome, Quantidade, Preco, Setor, Prateleira FROM Produtos"
        self.cursor.execute(sql)
        resultados = self.cursor.fetchall()

        if resultados:
            print("\n--- Estoque Atual ---")
            for linha in resultados:
                p = Produto(*linha)
                print(p)
            print()
        else:
            print("Estoque vazio.\n")

    def fechar_conexao(self):
        self.cursor.close()
        self.conn.close()
