import random

estoque = [
    {"id": 1, "nome": "Arroz 5kg", "preco": 20.00, "qtde_no_estoque": 50},
    {"id": 2, "nome": "Feijão 1kg", "preco": 8.50, "qtde_no_estoque": 30},
    {"id": 3, "nome": "Açúcar 1kg", "preco": 5.00, "qtde_no_estoque": 25},
    {"id": 4, "nome": "Café 500g", "preco": 12.00, "qtde_no_estoque": 15},
    {"id": 5, "nome": "Óleo de soja 900ml", "preco": 6.00, "qtde_no_estoque": 20},
    {"id": 6, "nome": "Sal 1kg", "preco": 2.00, "qtde_no_estoque": 40},
    {"id": 7, "nome": "Macarrão 500g", "preco": 3.50, "qtde_no_estoque": 35},
    {"id": 8, "nome": "Molho de tomate 340g", "preco": 4.00, "qtde_no_estoque": 10},
    {"id": 9, "nome": "Leite 1L", "preco": 4.50, "qtde_no_estoque": 45},
    {"id": 10, "nome": "Sabão em pó 1kg", "preco": 10.00, "qtde_no_estoque": 12}
]

lista_total_de_vendas = []

contador_de_ids = 11

while True:
  menu = input("""
  Escolha uma opção:
  1 - Produtos
  2 - Vendas
  0 - Encerrar
  """)
  match menu:
    case "1":
      while True:
        menu_de_produtos = input("""
        Escolha uma opção
        1 - Cadastrar novo produto
        2 - Ver todos os produtos
        3 - Editar produto cadastrado
        4 - Excluir produto cadastrado
        0 - Voltar para o Menu principal
        """)
        match menu_de_produtos:
          case "1":
            nome = str(input("Digite o nome do produto: "))
            while True:
              preco = float(input("Digite o preço do produto: "))
              if preco > 0:
                break
            while True:
              qtde = int(input("Digite a quantidade do produto: "))
              if qtde > 0:
                break

            novo_produto = {
              "id": contador_de_ids,
              "nome": nome,
              "preco": preco,
              "qtde_no_estoque": qtde
            }
            contador_de_ids += 1
            estoque.append(novo_produto)
            print("Produto cadastrado com sucesso")
          case "2":
            if len(estoque) == 0:
              print("Estoque vazio")
            else:
              for produto_da_vez in estoque:
                print(f"""
                ID: {produto_da_vez["id"]}
                Nome do Produto: {produto_da_vez["nome"]}
                Preço do Produto: R$ {produto_da_vez["preco"]}
                Quantidade no estoque: {produto_da_vez["qtde_no_estoque"]}
                """)
          case "3":
              for produto_da_vez in estoque:
                print(f"ID: {produto_da_vez["id"]} - Nome do Produto: {produto_da_vez["nome"]}")
              id_do_item_a_ser_editado = int(input("Digite o ID do item que você quer editar: "))
              produto_foi_encontrado = False
              for produto_em_questao in estoque:
                if produto_em_questao["id"] == id_do_item_a_ser_editado:
                  submenu_do_editar = input("""
                  Qual atributo você quer editar:
                  1 - Nome
                  2 - Preço
                  3 - Quantidade
                  0 - Sair
                  """)
                  match submenu_do_editar:
                    case "1":
                      novo_valor = str(input("Digite o novo nome do produto: "))
                      produto_em_questao["nome"] = novo_valor
                    case "2":
                      novo_valor = float(input("Digite o novo preço do produto: "))
                      produto_em_questao["preco"] = novo_valor
                    case "3":
                      novo_valor = int(input("Digite a nova quantidade no estoque do produto: "))
                      produto_em_questao["qtde_no_estoque"] = novo_valor
                    case "0":
                      break
                    case _:
                      print("Opção inválida")
                  print("Produto editado com sucesso")
                  produto_foi_encontrado = True
                  break
              if produto_foi_encontrado == False:
                print("Produto não encontrado")
          case "4":
              for produto_da_vez in estoque:
                print(f"ID: {produto_da_vez["id"]} - Nome do Produto: {produto_da_vez["nome"]}")
              id_do_item_a_ser_excluido = int(input("Digite o ID do item que você quer excluir: "))
              produto_foi_encontrado = False
              for produto_em_questao in estoque:
                if produto_em_questao["id"] == id_do_item_a_ser_excluido:
                  estoque.remove(produto_em_questao)
                  print("Produto removido com sucesso")
                  produto_foi_encontrado = True
                  break
              if produto_foi_encontrado == False:
                print("Produto não encontrado")
          case "0":
            break
          case _:
            print("Opção inválida")
    case "2":
      carrinho = []
      nome_do_cliente = str(input("Digite o nome do cliente: "))
      while True:
        menu_de_vendas = input("""
        1 - Vender produto
        2 - Encerrar Venda
        """)
        match menu_de_vendas:
          case "1":
            id_do_produto_vendido = int(input("Digite o id do produto que você está vendendo: "))
            produto_foi_encontrado = False
            for produto_da_vez in estoque:
              if produto_da_vez["id"] == id_do_produto_vendido:
                while True:
                  qtde_vendida = int(input("Digite a quantidade vendida do item: "))
                  if produto_da_vez["qtde_no_estoque"] >= qtde_vendida:
                    produto_da_vez["qtde_no_estoque"] -= qtde_vendida
                    break
                  else:
                    print(f"Quantidade inválida, estoque atual desse produto é: {produto_da_vez["qtde_no_estoque"]}")
                produto_foi_encontrado = True
                nova_venda = {
                  "produto": produto_da_vez["nome"],
                  "preco_unitario": produto_da_vez["preco"],
                  "quantidade_vendida": qtde_vendida,
                  "total_da_venda_do_produto": produto_da_vez["preco"] * qtde_vendida
                }
                carrinho.append(nova_venda)
                print("Item adicionado no carrinho")
            if produto_foi_encontrado == False:
              print("Item não encontrado")
          case "2":
            soma_total = 0
            for venda_da_vez in carrinho:
              soma_total += venda_da_vez["total_da_venda_do_produto"]

            nova_nota_fiscal = {
              "Nome do Cliente": nome_do_cliente,
              "Lista_de_itens_da_notas": carrinho,
              "Valor_total": soma_total
            }
            print(nova_nota_fiscal)
            lista_total_de_vendas.append(nova_nota_fiscal)
            break
    case "0":
      print("Programa encerrado")
      break
    case _:
      print("Opção inválida")


soma_final_do_dia = 0
maior_do_dia = lista_total_de_vendas[0]
menor_do_dia = lista_total_de_vendas[0]

for nota_fiscal_da_vez in lista_total_de_vendas:
  soma_final_do_dia += nota_fiscal_da_vez["Valor_total"]

  if nota_fiscal_da_vez["Valor_total"] > maior_do_dia["Valor_total"]:
    maior_do_dia = nota_fiscal_da_vez

  if nota_fiscal_da_vez["Valor_total"] < menor_do_dia["Valor_total"]:
    menor_do_dia = nota_fiscal_da_vez

print(f"A soma total do dia foi {soma_final_do_dia}")

print(f"A maior venda do dia foi do cliente {maior_do_dia["Nome do Cliente"]} e custou {maior_do_dia["Valor_total"]}")

print(f"A menor venda do dia foi do cliente {menor_do_dia["Nome do Cliente"]} e custou {menor_do_dia["Valor_total"]}")

nota_fiscal_sorteada = random.choice(lista_total_de_vendas)

print(f"O cliente sorteado foi {nota_fiscal_da_vez["Nome do Cliente"]}")