class Produtos:
    def __init__(self,produtos):
        self.produtos = produtos

    def produtos_disponiveis(self):
        if len(self.produtos) > 0:
            for numero_produto in self.produtos:
                print(f"{numero_produto} - {self.produtos[numero_produto]['nome']}, preço: {self.produtos[numero_produto]['preco']}")

class Carrinho:
    def __init__(self,produtos):
        self.produtos_disponiveis = produtos.produtos
        self.lista_precos_carrinho = []
        self.lista_produtos_carrinho = []

    def adicionar_produto(self,numero_produto_usuario):
        if numero_produto_usuario > 0:
            for numero_produto in self.produtos_disponiveis:
                if numero_produto == numero_produto_usuario:
                    self.lista_precos_carrinho.append(self.produtos_disponiveis[numero_produto]['preco'])
                    self.lista_produtos_carrinho.append(self.produtos_disponiveis[numero_produto]['nome'])

    def remover_produto(self,numero_produto_usuario):
        if len(self.lista_produtos_carrinho) > 0 and len(self.lista_precos_carrinho) > 0:
            self.lista_precos_carrinho.pop(numero_produto_usuario)
            self.lista_produtos_carrinho.pop(numero_produto_usuario)

    def mostra_total(self):
        total = 0
        if len(self.lista_precos_carrinho) > 0:
            for preco in self.lista_precos_carrinho:
                total += preco
        return total
    
    def mostrar_produtos_carrinho(self):
        if len(self.lista_produtos_carrinho) > 0:
            print("Carrinho:")
            for i in range(len(self.lista_produtos_carrinho)):
                print(f"{i} - {self.lista_produtos_carrinho[i]} - R$ {self.lista_precos_carrinho[i]:.2f}")
    
    def finalizar_compra(self):
        print("Compra finalizada")

produtos = Produtos({
    1:{'nome':'Lápis','preco':2.5},
    2:{'nome':'Escova','preco':10},
    3:{'nome':'Microfone','preco':45}
})

def main():
    carrinho = Carrinho(produtos)
    while True:
        print("1. Ver produtos\n2. Adicionar produto no carrinho\n3. Remover produto do carrinho\n4. Ver total e produtos do carrinho\n5. Finalizar compra\n6. Sair")
        try:
            escolha = int(input("Digite uma opção: "))
            if escolha == 1:
                produtos.produtos_disponiveis()
            elif escolha == 2:
                adicionar_produto_carrinho(carrinho)
            elif escolha == 3:
                remover_produto_carrinho(carrinho)
            elif escolha == 4:
                total = carrinho.mostra_total()
                carrinho.mostrar_produtos_carrinho()
                print(f"Total no carrinho: R${total:.2f}")
            elif escolha == 5:
                total = carrinho.mostra_total()
                print(f"Total da compra: R${total:.2f}")
                carrinho.finalizar_compra()
                break
            elif escolha == 6:
                print("Você saiu do sistema.")
                break
            else:
                print("Opção inválida")
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

def remover_produto_carrinho(carrinho):
    while True:
        if len(carrinho.lista_produtos_carrinho) > 0:
            numero_produto_usuario = int(input("Digite o número do produto que deseja remover: "))
            if numero_produto_usuario < 0 or numero_produto_usuario > len(carrinho.lista_produtos_carrinho):
                print("Você digitou uma opção incorreta!")
            else:
                for i in range(len(carrinho.lista_produtos_carrinho)):
                    if i == numero_produto_usuario:
                        carrinho.remover_produto(numero_produto_usuario)
                        print("Produto removido no carrinho!")
                        return True
                    else:
                        print("Esse produto não existe")
                        return False
        else:
            print("Carrinho está vazio")
            break

main()