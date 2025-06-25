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
