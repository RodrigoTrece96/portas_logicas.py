import random 

possibilidades = ('pedra', 'papel', 'tesoura')
rodadas = 0
score_usuario = 0
score_computador = 0

while True:

# Mostrando o placar a cada jogada
    print(f"Pontuação: {score_usuario}:{score_computador}") #formatando com f-strings
    print('Rodada: ', rodadas)

# Definindo o número de rodadas
    if score_usuario == 3 or score_computador == 3:
        print('A partida acabou!')
        break 

# Defindindo as jogadas
    jogada_do_computador = random.choice(possibilidades)
    jogada_usuario = input('Escolha pedra, papel ou tesoura: ')

# Casos inválidos
    if jogada_usuario not in possibilidades:
        print('Jogada inválida')
        continue

# Caso em que o jogo empata
    if jogada_usuario == jogada_do_computador:
        print('Empate')
        rodadas += 1 
        continue 

#Caso em que o computador vence
    if (jogada_do_computador == 'pedra' and jogada_usuario == 'tesoura') or \
        (jogada_do_computador == 'papel' and jogada_usuario == 'pedra') or \
        (jogada_do_computador == 'tesoura' and jogada_usuario == 'papel'):
        print('O computador venceu!')
        rodadas += 1 
        score_computador += 1 
    
#Caso em que o usuário vence
    if jogada_usuario == ('pedra' and jogada_do_computador == 'tesoura') or \
        (jogada_usuario == 'papel' and jogada_do_computador == 'pedra') or \
        (jogada_usuario == 'tesoura' and jogada_do_computador == 'papel'):
        print('Você venceu!')
        rodadas += 1 
        score_usuario += 1 
        continue 

