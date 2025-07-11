class Produtos:
    def __init__(self,produtos):
        self.produtos = produtos

    def produtos_disponiveis(self):
        if len(self.produtos) > 0:
            for numero_produto in self.produtos:
                print(f"{numero_produto} - {self.produtos[numero_produto]['nome']}, preço: {self.produtos[numero_produto]['preco']}")

class Carrinho(Produtos):
    def __init__(self):
        pass
    
    def adicionar_produto(self,numero_produto):
        if numero_produto > 0:
            self.lista_produtos.append(numero_produto)

    def mostra_total(self):
        total = 0
        if len(self.lista_precos) > 0:
            for preco in self.lista_precos:
                total += preco
        return total
    
    def finalizar_compra(self):
        print("Compra finalizada")

produtos = Produtos({
    1:{'nome':'Lápis','preco':2.5},
    2:{'nome':'Escova','preco':10},
    3:{'nome':'Microfone','preco':45}
})
'''
carrinho = Carrinho()
carrinho.adicionar_produto(1)
print(f"Total no carrinho: {carrinho.mostra_total()}")
print(carrinho.finalizar_compra())
'''

def main():
    while True:
        print("1. Ver produtos\n2. Adicionar produto\n3. Ver total do carrinho\n4. Finalizar compra\n5. Sair")
        try:
            escolha = int(input("Digite uma opção: "))
            if escolha == 1:
                produtos.produtos_disponiveis()
            elif escolha == 2:
                numero_produto = int(input("Digite o número do produto? "))
                #carrinho.adicionar_produto(numero_produto)
        except ValueError:
            print("Você digitou algo errado")


main()