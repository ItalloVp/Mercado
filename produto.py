import comando

while True:
    menu= (str(input("""
    Bem vindo! 
    1 - Cadastrar produto
    2 - Ver produtos
    3 - Edite um produto
    4 - Excluir um produto
    5 - Abrir venda
    6 - Finalizar o dia
    
""")))
    
    match menu:
        case "1":
            comando.cadastrar_produto()
        case "2":
            comando.ver_produtos()
        case "3":
            comando.editar_produtos()
        case "4": 
            comando.excluir_produto()
        case "5":
            comando.vendas_loja()

        case "6":
            comando.finalizacao
