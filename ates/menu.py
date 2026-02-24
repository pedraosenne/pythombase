while True:
    print("1- Cadatrar")
    print("2- Consultar")
    print("3- Sair")

    opcao = input("Escolha uma opção:")

    if opcao in [ "1","2", "3"]:
        break
    else:
        print("Função inválida! - escolha novamente")
    
print("Voce escolheu: ",opcao)