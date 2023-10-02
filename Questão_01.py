#criando um pedra papel tesoura no python 

import random

#criando uma tupla com as possibilidades 

possibilidades = ('pedra','papel','tesoura')
primeira_jogada = input('Digite sua jogada: ')
var1 = random.choice(possibilidades)

pontuacao_computador = 0
minha_pontuacao = 0 

if primeira_jogada == var1:
    print('empate')
elif primeira_jogada == 'tesoura' and var1 == 'pedra':
    
    print('o computador ganhou')
elif 



     