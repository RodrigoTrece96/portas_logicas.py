#Resolvendo a questao de calculo IV do guilherme! 

#Transcrever a funcao que está dentro do somatorio para o python usando a biblioteca "math"

import math

#usar o while True para somar infinitamente 
n = 1
while True:
    n = n + 1 
    termo = 1/n*(math.log(n,math.e))**2 #1/n*ln^2(n)
    termo_arredondado = round(termo,7) #diminuindo o numero de casas decimais para meu pc não explodir
    print(termo_arredondado)

#Conlusão: a série é divergente