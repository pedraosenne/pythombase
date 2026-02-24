while True:
   try:
       quantidade = int(imput("Digite a quantidade de itens: "))
       if quantidade <= 0:
           print("Quantidade deve ser maior que 0")
       else:
           break
   except ValueError:
       print("Ocorreu um erro inesperado. por favor, tente novamente.")


print("Quantidade cadastrada:" , quantidade)

