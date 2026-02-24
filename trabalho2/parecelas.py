while True:
   try:
       parcelas = int(input("Digite a quantidade de parcelas (1 a 12): "))
       if 1 <= parcelas <= 12:
           break 
       else:
           print("Erro: Por favor, escolha um número entre 1 e 12.")
   except ValueError:

       print("Entrada inválida! Digite apenas números inteiros (ex: 1, 6, 12).")
print("-" * 30)
print(f"Plano de pagamento confirmado: {parcelas}x parcelas.")


