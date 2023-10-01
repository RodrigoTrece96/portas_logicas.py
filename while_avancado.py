#Criando um cronometro no Python 

#adicionar a noção de tempo no código

import time

#usar o while True para o cronometro continuar até o desejado 
segundo = 0
minuto = 0 

while True:
    segundo = segundo + 1 
    if segundo == 60:
        segundo = 0
        minuto = minuto + 1 
    time.sleep(1) 

    if minuto < 10 and segundo < 10:        #formatando o cronometro
        print(f'0{minuto}:0{segundo}')
    elif minuto < 10 and segundo >=10:
        print(f'0{minuto}:{segundo}')
    elif minuto >= 10 and segundo < 10:
        print(f'{minuto}:0{segundo}')
    else:
        print(f'{minuto}:{segundo}')

