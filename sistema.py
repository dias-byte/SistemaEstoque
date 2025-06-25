from estoque import Estoque
from produto import Produto

class SistemaEstoque:
    def __init__(self):
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
