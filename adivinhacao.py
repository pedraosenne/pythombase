import random
print("*************************")
print("****Jogo Adivinhação*****")
print("*************************")

numero_secreto = random.randrange(1,101)
total_tentativas = 5
rodada = 1


for rodada in range(1,total_tentativas + 1):

    print(f"Tentativa {rodada} de {total_tentativas}")

    chute_str = input("Digite o seu número: ")
    chute = int(chute_str)

    if(chute < 1 or chute > 67):
      print("Voce deve digitart um numero entre 1 e 67")
      continue
   

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if (acertou):
        print("Parabéns! Você acertou!")
        break 
    else:
        if (maior):
            print("O seu chute foi MAIOR que o número secreto.")
        elif (menor):
            print(" O seu chute foi MENOR que o número secreto.")

print("Fim de jogo!")