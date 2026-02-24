while True:
   print("Bem_vindo ao Caixa Eletrônico!")
   print("1 - Sacar")
   print("2 - Depositar")
   print("3 - Sair")
   escolha = input("Escolha uma opção: ")
   if escolha == "1":
       valor_saque = float(input("DIGITE O VALOR DO SAQUE: "))
       print(f"você sacou R${valor_saque:.2f}")
   elif escolha == "2":
       valor_deposito = float(input("DIGITE O VALOR DO DEPOSITO: "))
       print(f"você depositou R${valor_deposito:.2f}")
   elif escolha == "3":
       print("Obrigado por usar o Caixa Eletrônico. Até logo!")
       break
   else:
       print("Opção inválida. Por favor, escolha uma opção válida.")


