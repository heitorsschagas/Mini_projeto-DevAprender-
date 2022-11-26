'''
# Medidor de velocidade
1. Quais são os dados de entrada necessário?
2. O que devo fazer com estes dados?
3. Quais são as restrições deste problema?
4. Qual é o resultado esperado?
5. Quais são as sequências de passos a serem feitos para chegar ao resultado esperado?
'''

velocidade = int(input('Qual foi a sua velocidade: '))
velocidade_maxima = 80

if velocidade <= velocidade_maxima:
  print('Não levou multa')
elif velocidade > velocidade_maxima and velocidade <= velocidade_maxima +10:
  print('Levou multa leve')
elif velocidade >= velocidade_maxima +11 and velocidade <= velocidade_maxima +20:
  print('Levou multa grave')
elif velocidade >= velocidade_maxima +21:
  print('Levou multa gravíssima')