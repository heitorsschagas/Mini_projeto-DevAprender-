'''
Criar programa que o usuário chute e acerte o valor aleatório de 1 a 10
'''
import random

valor_aleatorio = random.randint(1,10)

acertou= False
while acertou == False:
  chute = int(input('Chute um valor de 1 a 10: '))
  if chute > valor_aleatorio:
    print('O número gerado é maior')
  elif chute < valor_aleatorio:
    print('O número gerado é menor')
  elif chute == valor_aleatorio:
    print('Acertou o número gerado')
    acertou = True