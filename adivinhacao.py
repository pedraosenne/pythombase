import random


VERMELHO = '\033[31m'
VERDE = '\033[32m'
AMARELO = '\033[33m'
AZUL = '\033[34m'
RESET = '\033[0m'






print('Escolha a dificuldade:')
print('1 - facil (10 tentativas)')
print('2 - medio (5 tentativas)')
print('3 - dificil (2 tentativas)')




def definir_dificuldade():
   dificuldade = input('digite a dificuldade: ')
   if dificuldade == '1':
       return 10
   elif dificuldade == '2':
       return 5
   elif dificuldade == '3':
       return 2
   else:
       print("Você escolheu uma opção inválida! faça outra escolha de dificuldade.")
       exit()


   while True:
       nivel_str = input('Digite a dificuldade (1, 2 ou 3): ')
       if nivel_str.isdigit():
           print(VERMELHO + "digite apenas numeros!" + RESET)
           continue
       nivel = int(nivel_str)
       if nivel in [1, 2, 3]:
           if nivel == 1:
               return 10
           elif nivel == 2:
               return 5
           elif nivel == 3:
               return 3
       else:
           print(AMARELO + "Opção inválida! Escolha' 1, 2 ou 3." + RESET)


def jogar():
   print(AZUL + '=====================================' + RESET)
   print(AZUL + '🎯 BEM-VINDO(A) AO JOGO DA ADIVINHAÇÃO 🎯' + RESET)
   print(AZUL + '=====================================' + RESET)
   print('Vou pensar em um número entre 1 e 100...')


   tentativas = definir_dificuldade()
   numero_secreto = random.randrange(1, 100)
   historico = []
  
  
for rodada in range(1, tentativas + 1):
       print("tentativa {} de {}".format(rodada, tentativas))
      
       if not chute_str.isdigit():
           print(VERMELHO + '❌ Isso não é um número válido! Tenta de novo...\n' + RESET)
           continue


           chute =int(chute_str)


       if (chute < 1 or chute > 100):
           print(AMARELO + '🚫 Calma! Só vale números entre 1 e 100!\n' + RESET)
           continue
       historico.append(chute)


       acertou = chute == numero_secreto
       maior   = chute > numero_secreto
       menor   = chute < numero_secreto


       if acertou:
           print('\n🎉 PARABÉNS! Você acertou o número secreto! 🎉')
           print(f'  O número era {numero_secreto} mesmo!')
           break
       else:
           if maior:
               print('📈 Você chutou ALTO demais!')
               print('Tenta um número MENOR na próxima...\n')
           elif menor:
               print('📉 Você chutou BAIXO demais!')
               print('Tenta um número MAIOR agora...\n')


print('=====================================')
print('        FIM DO JOGO         ')
print('=====================================')
print(f'O número secreto era: {numero_secreto} ⭐')
print('Joga de novo quando quiser! 😉')

