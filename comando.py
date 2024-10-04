import random

lista_de_produtos = []

def cadastrar_produto():
    produto = str(input("Digite o nome do produto: ")).lower()
    preco = float(input("Digite o preço: "))
    quantidade_estoque = int(input("Digite a quantidade em estoque: "))

    novo_produto = {
        "Produto": produto,
        "Preço": preco,
        "Quantidade em estoque": quantidade_estoque
    }
    lista_de_produtos.append(novo_produto)
    print(f"{produto} cadastrado com sucesso")

def ver_produtos():
    for produto_da_vez in lista_de_produtos:
        print(f"""
    O produto {produto_da_vez["Produto"]} está por R${produto_da_vez["Preço"]} e possui {produto_da_vez["Quantidade em estoque"]} em estoque.
""")
        
def editar_produtos():
      print("Os produtos disponíveis para alteração são:")
      for produto_da_vez in lista_de_produtos:
        print(f"{produto_da_vez["Produto"]}")
    
        produto_pra_alterar = str(input("Qual deseja alterar?")).lower()
        if produto_da_vez["Produto"] == produto_pra_alterar:
            produto_da_vez["Produto"] =  str(input("Digite o nome: ")).lower()
            produto_da_vez["Preço"] =  float(input("Digite o valor: "))
            produto_da_vez["Quantidade em estoque"] = int(input("Digite a quantidade: "))
            print(f"O {produto_da_vez["Produto"]} foi alterado.")


def excluir_produto():
    print("Os produtos disponíveis para exclusão são: ")
    for produto_da_vez in lista_de_produtos:
        print(f"{produto_da_vez["Produto"]}")


    produto_para_apagar = str(input("Qual deseja excluir?")).lower()
    produto_encontrado = False


    for produto_da_vez in lista_de_produtos:
        if produto_da_vez == produto_para_apagar:
            lista_de_produtos.remove(produto_para_apagar)
            produto_encontrado = True
            print("Produto removido com sucesso!")
    
    if produto_encontrado == False:
        print("Produto não encontrado")

compradores = []
vendas_da_loja = []

def vendas_loja():
    cliente = str(input("Digite o nome do cliente: "))
    itens_vendidos = str(input("Digite os itens do carrinho:"))
    valor_venda = float(input("Digite o valor total da compra."))

    nova_venda = {
        "Cliente": cliente,
        "Itens": itens_vendidos,
        "Venda": valor_venda
    }
    compradores.append(nova_venda)
    
    vendas_da_loja.append(nova_venda["Venda"])

maior_venda= [0]
menor_venda= [0] 

if vendas_da_loja > maior_venda:
    maior_venda = vendas_da_loja

if vendas_da_loja < menor_venda:
    menor_venda = vendas_da_loja


def finalizacao():
    vencedor = random.choice(compradores["Cliente"])
    print(f"O vencedor do dia que receberá 10% de cashback foi {vencedor}")
    total= sum(vendas_da_loja)
    print(f"Venda total do dia foi R${total}")
