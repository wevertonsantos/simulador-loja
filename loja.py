class Produtos:
    def __init__(self,nomes,precos):
        self.nomes = nomes
        self.precos = precos
    
    def produtos_disponiveis(self):
        for i in range(len(self.nomes)):
            print(f"Produto: {self.nomes[i]}, Preço: {self.precos[i]}")

class Carrinho:
    lista_produtos = []
    lista_precos = []
    def __init__(self):
        pass
    
    def adicionar_produto(self,produto,preco):
        if len(produto) > 0:
            self.lista_produtos.append(produto)
        if preco > 0:
            self.lista_precos.append(preco)

    def mostra_total(self):
        total = 0
        print(self.lista_produtos)
        if len(self.lista_precos) > 0:
            for preco in self.lista_precos:
                total += preco
        return total
    
    def finalizar_compra(self):
        print("Compra finalizada")

produtos = Produtos(["Lápis","Escova","Microfone"],[2.50,10,45])
print(produtos.produtos_disponiveis())
carrinho = Carrinho()
carrinho.adicionar_produto("Lápis",2.50)
carrinho.adicionar_produto("Escova",10)
print(f"Total no carrinho: {carrinho.mostra_total()}")
print(carrinho.finalizar_compra())

def main():
    while True:
        print("1. Ver produtos\n2. Adicionar produto\n3. Ver total do carrinho\n4. Finalizar compra\n5. Sair")
        try:
            escolha = int(input("Digite uma opção: "))
            if escolha == 1:
                ...
        except ValueError:
            print("Você digitou algo errado")


main()