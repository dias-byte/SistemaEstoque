import mysql.connector

# Configuração da conexão com o banco MySQL
config = {
    'user': 'root',
    'password': 'fh1120hdf2005',
    'host': 'localhost',
    'database': 'EstoqueDB',
    'raise_on_warnings': True
}

def conectar():
    return mysql.connector.connect(**config)

def adicionar_item():
    cnx = conectar()
    cursor = cnx.cursor()
    
    codigo = input("Informe o código do produto: ")
    # Verificar se produto já existe
    cursor.execute("SELECT COUNT(*) FROM Produtos WHERE Codigo = %s", (codigo,))
    if cursor.fetchone()[0] > 0:
        print("Produto já cadastrado.")
        cursor.close()
        cnx.close()
        return
    
    nome = input("Informe o nome do produto: ")
    quantidade = int(input("Informe a quantidade inicial: "))
    preco = float(input("Informe o preço unitário: "))
    setor = input("Informe o setor onde o produto está localizado: ")
    prateleira = input("Informe a prateleira onde o produto está localizado: ")
    
    sql = "INSERT INTO Produtos (Codigo, Nome, Quantidade, Preco, Setor, Prateleira) VALUES (%s, %s, %s, %s, %s, %s)"
    valores = (codigo, nome, quantidade, preco, setor, prateleira)
    
    cursor.execute(sql, valores)
    cnx.commit()
    print(f"Produto '{nome}' adicionado com sucesso!\n")
    
    cursor.close()
    cnx.close()

def remover_item():
    cnx = conectar()
    cursor = cnx.cursor()
    
    codigo = input("Informe o código do produto a remover: ")
    cursor.execute("SELECT COUNT(*) FROM Produtos WHERE Codigo = %s", (codigo,))
    if cursor.fetchone()[0] == 0:
        print("Produto não encontrado.\n")
    else:
        cursor.execute("DELETE FROM Produtos WHERE Codigo = %s", (codigo,))
        cnx.commit()
        print("Produto removido com sucesso!\n")
    
    cursor.close()
    cnx.close()

def atualizar_quantidade():
    cnx = conectar()
    cursor = cnx.cursor()
    
    codigo = input("Informe o código do produto: ")
    cursor.execute("SELECT COUNT(*) FROM Produtos WHERE Codigo = %s", (codigo,))
    if cursor.fetchone()[0] == 0:
        print("Produto não encontrado.\n")
    else:
        nova_quantidade = int(input("Informe a nova quantidade: "))
        cursor.execute("UPDATE Produtos SET Quantidade = %s WHERE Codigo = %s", (nova_quantidade, codigo))
        cnx.commit()
        print("Quantidade atualizada com sucesso!\n")
    
    cursor.close()
    cnx.close()

def listar_estoque():
    cnx = conectar()
    cursor = cnx.cursor()
    cursor.execute("SELECT Codigo, Nome, Quantidade, Preco, Setor, Prateleira FROM Produtos")
    resultados = cursor.fetchall()
    
    if not resultados:
        print("Estoque vazio.\n")
    else:
        print("\n--- Estoque Atual ---")
        for (codigo, nome, quantidade, preco, setor, prateleira) in resultados:
            print(f"Código: {codigo} | Nome: {nome} | Quantidade: {quantidade} | Preço: R${preco:.2f} | Setor: {setor} | Prateleira: {prateleira}")
        print()
    
    cursor.close()
    cnx.close()

def buscar_item():
    cnx = conectar()
    cursor = cnx.cursor()
    
    nome_busca = input("Informe o nome do produto para buscar: ").lower()
    cursor.execute("SELECT Codigo, Nome, Quantidade, Preco, Setor, Prateleira FROM Produtos WHERE LOWER(Nome) LIKE %s", (f"%{nome_busca}%",))
    resultados = cursor.fetchall()
    
    if resultados:
        print("\nProdutos encontrados:")
        for (codigo, nome, quantidade, preco, setor, prateleira) in resultados:
            print(f"Código: {codigo} | Nome: {nome} | Quantidade: {quantidade} | Preço: R${preco:.2f} | Setor: {setor} | Prateleira: {prateleira}")
        print()
    else:
        print("Nenhum produto encontrado com esse nome.\n")
    
    cursor.close()
    cnx.close()

def menu():
    while True:
        print("""
=== Sistema de Controle de Estoque (MySQL) ===
1. Adicionar produto
2. Remover produto
3. Atualizar quantidade
4. Listar produtos
5. Buscar produto
6. Sair
""")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            adicionar_item()
        elif opcao == '2':
            remover_item()
        elif opcao == '3':
            atualizar_quantidade()
        elif opcao == '4':
            listar_estoque()
        elif opcao == '5':
            buscar_item()
        elif opcao == '6':
            print("Encerrando o sistema.")
            break
        else:
            print("Opção inválida. Tente novamente.\n")

if __name__ == "__main__":
    menu()
