USE EstoqueDB;

CREATE TABLE IF NOT EXISTS Produtos (
    Codigo VARCHAR(20) PRIMARY KEY,
    Nome VARCHAR(100) NOT NULL,
    Quantidade INT NOT NULL DEFAULT 0,
    Preco DECIMAL(10, 2) NOT NULL,
    Setor VARCHAR(50),
    Prateleira VARCHAR(50)
);

INSERT INTO Produtos (Codigo, Nome, Quantidade, Preco, Setor, Prateleira) VALUES
('P001', 'Pastilha de Freio', 100, 100.00, 'Pastilhas', 'A1'),
('P002', 'Sapata de Freio', 50, 120.00, 'Sapatas', 'B2');
