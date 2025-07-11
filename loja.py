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
    def __init__(self,produtos,precos):
        self.produtos = produtos
        self.precos = precos

    def mostra_total(self):
        total = 0
        if len(self.produtos) > 0 and len(self.precos) > 0:
            for i in range(len(self.produtos)):
                total += self.precos[i]
        return total

pessoa1 = Pessoa("Rodrigo")
produtos = Produtos(["Lápis","Escova","Microfone"],[2.50,10,45])
print(produtos.produtos_disponiveis())
carrinho = Carrinho(["Lápis","Escova"],[2.50,10])
print(carrinho.mostra_total())