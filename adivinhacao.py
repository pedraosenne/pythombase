print("*************************")
print("****Jogo Adivinhação*****")
print("*************************")

numero_secreto = 69
total_tentativas = 5
rodada = 1


while (rodada <= total_tentativas):
    print(f"Tentativa {rodada} de {total_tentativas}")

    chute_str = input("Digite o seu número: ")
    chute = int(chute_str)

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

    rodada = rodada + 1

print("Fim de jogo!")