import os
import mysql.connector

class Produto:
    def __init__(self, codigo, nome, quantidade, preco, setor, prateleira):
        self.codigo = codigo
        self.nome = nome
        self.quantidade = quantidade
        self.preco = preco
        self.setor = setor
        self.prateleira = prateleira

    def __str__(self):
        return (f"Código: {self.codigo} | Nome: {self.nome} | "
                f"Quantidade: {self.quantidade} | Preço: R${self.preco:.2f} | "
                f"Setor: {self.setor} | Prateleira: {self.prateleira}")

class Estoque:
    def __init__(self):
        print("Inicializando conexão com o banco de dados...")
        senha = os.getenv('DB_SENHA')
        if not senha:
            print("Erro: variável de ambiente DB_SENHA não definida.")
            exit(1)
        try:
            self.conn = mysql.connector.connect(
                host='localhost',
                user='root',
                password=senha,
                database='EstoqueDB'
            )
            self.cursor = self.conn.cursor()
            if self.conn.is_connected():
                print("Conectado ao banco EstoqueDB com sucesso!\n")
            else:
                print("Falha na conexão com o banco de dados.")
                exit(1)
        except mysql.connector.Error as err:
            print(f"Erro na conexão com o banco: {err}")
            exit(1)

    def adicionar_produto(self, produto):
        try:
            sql = ("INSERT INTO Produtos (Codigo, Nome, Quantidade, Preco, Setor, Prateleira) "
                   "VALUES (%s, %s, %s, %s, %s, %s)")
            valores = (produto.codigo, produto.nome, produto.quantidade, produto.preco,
                       produto.setor, produto.prateleira)
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
        print("Conexão com banco encerrada.")

class SistemaEstoque:
    def __init__(self):
        print("Iniciando sistema...")
        self.estoque = Estoque()

    def menu(self):
        while True:
            print("""
=== Sistema de Controle de Estoque ===
1. Adicionar produto
2. Remover produto
3. Atualizar quantidade
4. Listar produtos
5. Buscar produto
6. Sair
""")
            opcao = input("Escolha uma opção: ")

            if opcao == '1':
                self.adicionar()
            elif opcao == '2':
                self.remover()
            elif opcao == '3':
                self.atualizar()
            elif opcao == '4':
                self.estoque.listar_todos()
            elif opcao == '5':
                self.buscar()
            elif opcao == '6':
                print("Encerrando o sistema.")
                self.estoque.fechar_conexao()
                break
            else:
                print("Opção inválida. Tente novamente.\n")

    def adicionar(self):
        codigo = input("Informe o código do produto: ")
        nome = input("Informe o nome do produto: ")
        quantidade = int(input("Informe a quantidade inicial: "))
        preco = float(input("Informe o preço unitário: "))
        setor = input("Informe o setor onde o produto está localizado: ")
        prateleira = input("Informe a prateleira onde o produto está localizado: ")

        produto = Produto(codigo, nome, quantidade, preco, setor, prateleira)
        self.estoque.adicionar_produto(produto)

    def remover(self):
        codigo = input("Informe o código do produto a remover: ")
        self.estoque.remover_produto(codigo)

    def atualizar(self):
        codigo = input("Informe o código do produto: ")
        nova_quantidade = int(input("Informe a nova quantidade: "))
        self.estoque.atualizar_quantidade(codigo, nova_quantidade)

    def buscar(self):
        nome = input("Informe o nome do produto para buscar: ")
        self.estoque.buscar_por_nome(nome)

if __name__ == "__main__":
    sistema = SistemaEstoque()
    sistema.menu()
