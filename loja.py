class Produtos:
    def __init__(self,produtos):
        self.produtos = produtos

    def produtos_disponiveis(self):
        if len(self.produtos) > 0:
            for numero_produto in self.produtos:
                print(f"{numero_produto} - {self.produtos[numero_produto]['nome']}, preço: {self.produtos[numero_produto]['preco']}")

class Carrinho:
    lista_precos = []
    def __init__(self,produtos):
        self.produtos_disponiveis = produtos.produtos

    def adicionar_produto(self,numero_produto_usuario):
        if numero_produto_usuario > 0:
            for numero_produto in self.produtos_disponiveis:
                if numero_produto == numero_produto_usuario:
                    self.lista_precos.append(self.produtos_disponiveis[numero_produto]['preco'])

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
#print(f"Total no carrinho: {carrinho.mostra_total()}")
#print(carrinho.finalizar_compra())

def main():
    while True:
        print("1. Ver produtos\n2. Adicionar produto\n3. Ver total do carrinho\n4. Finalizar compra\n5. Sair")
        try:
            escolha = int(input("Digite uma opção: "))
            if escolha == 1:
                produtos.produtos_disponiveis()
            elif escolha == 2:
                carrinho = Carrinho(produtos)
                adicionar_produto_carrinho(carrinho)
            elif escolha == 3:
                carrinho.mostra_total()
        except ValueError:
            print("Você digitou algo errado")

def adicionar_produto_carrinho(carrinho):
    while True:
        numero_produto_usuario = int(input("Digite o número do produto que deseja adicionar: "))
        if numero_produto_usuario < 0 or numero_produto_usuario > len(produtos.produtos):
            print("Você digitou uma opção incorreta!")
        else:
            carrinho.adicionar_produto(numero_produto_usuario)
            print("Produto adicionado no carrinho!")
            break

main()