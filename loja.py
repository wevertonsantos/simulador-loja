class Pessoa:
    def __init__(self,nome):
        self.nome = nome

class Produtos:
    def __init__(self,nomes,precos):
        self.nomes = nomes
        self.precos = precos
    
    def produtos_disponiveis(self):
        for i in range(len(self.nomes)):
            print(f"Produto: {self.nomes[i]}, Preço: {self.precos[i]}")

class Carrinho:
    lista_produtos = {}
    def __init__(self):
        pass
    
    def adicionar_produto(self,produto,preco):
        self.lista_produtos['produtos'] = produto
        self.lista_produtos['precos'] = preco

    def mostra_total(self):
        total = 0
        if len(self.lista_produtos['produtos']) > 0 and len(self.lista_produtos['precos']) > 0:
            for preco in self.lista_produtos['precos']:
                total += preco
        return total

pessoa1 = Pessoa("Rodrigo")
produtos = Produtos(["Lápis","Escova","Microfone"],[2.50,10,45])
print(produtos.produtos_disponiveis())
carrinho = Carrinho()
carrinho.adicionar_produto(["Lápis"],[2.50])
print(carrinho.mostra_total())