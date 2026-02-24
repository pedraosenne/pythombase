ano_atual = 2026
while True:
   try:
       ano_nascimento = int(input("Digite o seu ano de nascimento: "))
       if 1900 < ano_nascimento <= ano_atual:
           break
       else:
           print(f"Erro: O ano deve ser maior que 1900 e menor ou igual a {ano_atual}.")

   except ValueError:
       print("Entrada inválida Por favor digite apenas números inteiros.")

print("Ano registrado com sucesso:", ano_nascimento)
 

