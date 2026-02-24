while True:
   try:
       altura = float(input("Digite sua altura em metros: "))
       if altura <= 0:
           print("Altura deve ser maior que 0")
       else:
           break
   except ValueError:
       print("Ocorreu um erro inesperado. Por favor, tente novamente.")


print("Altura cadastrada:", altura)


