import time

#entendendo a função do break e do pass

c = 0

while True: #legal para mesclar while e if 
    if c <= 60:
        pass
    else:
        break
    print(c) #coloca-se o print aqui para começar a contar do zero
    time.sleep(1) #da um tempo de 1s entre cada laço
    c = c + 1 
    # se o print estivesse aqui, começaria a contar do 1 e terminaria no 11, 
    # pois primeiro seria somado 1 ao 0
print('passou-se 1min')