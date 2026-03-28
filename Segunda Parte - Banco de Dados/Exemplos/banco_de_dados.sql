CREATE TABLE Cliente (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Nome TEXT NOT NULL,
    Email TEXT
);

CREATE TABLE Produto (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Nome TEXT NOT NULL, /* Força o texto não ser nulo*/
    Preco DECIMAL(10,2)
);
CREATE TABLE Pedido (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    ClienteID INTEGER,
    ProdutoID INTEGER,
    Quantidade INTEGER,
    Data DATE,
    FOREIGN KEY (ClienteID) REFERENCES Cliente(ID),
    FOREIGN KEY (ProdutoID) REFERENCES Produto(ID)
);


/* 1. Crie uma tabela chamada Fornecedor com os seguintes campos:
    ● ID (inteiro, chave primária)
    ● Nome (texto, obrigatório)
    ● CNPJ (texto de 14 caracteres) */

CREATE TABLE Fornecedor (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Nome TEXT NOT NULL,
    Cnpj TEXT (14) /* Isto trava que a variavel tenha 14 digitos no máximo*/
);

/*2. Adicione uma coluna Telefone na tabela Cliente.*/
ALTER TABLE Cliente ADD Telefone INTEGER(11)

/*3. Exclua a tabela Fornecedor que você criou.*/
DROP TABLE Fornecedor;

/*4. Insira um cliente chamado "Joana", com e-mail "joana@email.com" e ID 1.*/
INSERT INTO Cliente(ID,Nome,Email) VALUES (1,"Joana", "joana@email.com");

/* 5. Insira um produto chamado "Café", com preço de R$ 8,50 e ID 10. */
INSERT INTO Produto(ID,Nome,Preco) VALUES (10,"Café", 8.50);

/*6. Faça um pedido para Joana (ID 1) do produto Café (ID 10), com quantidade 3 e data de hoje.*/
INSERT INTO Pedido(ClienteID, ProdutoID, Quantidade, Data) VALUES (1,10, 3, "25/03/2026");

/*7. Atualize o e-mail de Joana para "joana.silva@email.com".*/
UPDATE Cliente SET Email = "joana.silva@email.com" WHERE ID = 1;  /*Sempre incluir o Where para não inserir o email em todos os usuários*/

/*8. Exclua o pedido feito por Joana.*/
DELETE FROM Pedido WHERE ID = 1;  /*Sempre incluir o Where para não deletar todos os pedidos*/

/*9. Liste todos os clientes da tabela Cliente.*/
SELECT * FROM Cliente LIMIT 10 /* Caso a Tabela seja grande use o LIMIT, select ALL FROM Clientes*/

/*10. Mostre o nome dos produtos com preço maior que R$ 10,00, ordenados pelo nome.*/
SELECT Nome FROM Produtos WHERE preco > 10 ORDER BY Nome;

/*11. Liste o nome dos clientes e a data de seus pedidos (utilize JOIN entre Cliente e Pedido).*/
SELECT Cliente.Nome, pedido.data
From Clientes
INNER JOIN Pedidos On Clientes.ID == Pedido.ClienteID

/*12. Para cada produto, mostre a quantidade total vendida (SUM), usando GROUP BY.*/
SELECT Produto.nome, SUM(pedido.quantidade)
FROM Produtos
INNER JOIN pedidos on Produto.ID == Pedido.ProdutoID
GROUP BY Nome

/*13. Liste os nomes dos produtos que nunca foram vendidos.*/
SELECT Produto.nome, Pedido.Quantidade
FROM Pedidos
WHERE Pedido.Quantidade == 0
INNER JOIN Produtos on Produto.ID == Pedido.ProdutoID
GROUP BY Nome
