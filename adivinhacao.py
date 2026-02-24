import random


print('=====================================')
print('🎯 BEM-VINDO(A) AO JOGO DA ADIVINHAÇÃO 🎯')
print('=====================================')
print('Vou pensar em um número entre 1 e 100...')
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


tentativas = definir_dificuldade()
print(f'Você tem {tentativas} tentativas para adivinhar o número secreto. Boa sorte! 🍀\n')




numero_secreto = random.randrange(1, 101)


for tentativa in range(1, tentativas + 1):
   chute_str = input('Qual é o seu palpite? → ')
   print(f'Você chutou: {chute_str}')


   try:
       chute = int(chute_str)
   except:
       print('❌ Isso não é um número válido! Tenta de novo...\n')
       continue


   if chute < 1 or chute > 100:
       print('🚫 Calma! Só vale números entre 1 e 100!\n')
       continue


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

