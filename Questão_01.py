import random 

possibilidades = ('pedra', 'papel', 'tesoura')
rodadas = 0
score_usuario = 0
score_computador = 0

while True:
#
# Definindo o número de rodadas
    if score_usuario == 3 or score_computador == 3:
        print('A partida acabou!')
        break 
# Defindindo as jogadas
    jogada_do_computador = random.choice(possibilidades)
    jogada_usuário = input('Escolha pedra, papel ou tesoura: ')


# Casos inválidos
    if jogada_usuário != 'pedra' or 'papel' or 'tesoura':
        print('Jogada inválida')
        continue

# Caso em que o jogo empata
    if jogada_usuário == jogada_do_computador:
        print('Empate')
        continue 

#Caso em que o computador vence
    if (jogada_do_computador == 'pedra' and jogada_usuário == 'tesoura') or \
        (jogada_do_computador == 'papel' and jogada_usuário == 'pedra') or \
        (jogada_do_computador == 'tesoura' and jogada_usuário == 'papel'):
        print('O computador venceu!')
        rodadas += 1 
        score_computador += 1 
    
#Caso em que o usuário vence
    if (jogada_usuário)


    