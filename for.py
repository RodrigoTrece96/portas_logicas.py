#Quando usar o for?
#(1) Quando se tem um iterável [1,2,3,4,5,6,7,8]

lista = [1,2,3,4,5,6,7,8,9,10]
for n in lista: #a cada iteracao, pega-se um elemento da lista e printa
    print(n)    #isso quer dizer que o n assume cada posição da lista até o fim do laço

str = 'rodrigotrece'

for m in str: #também pode ser usado para strings, mas nesse caso a cada iteração passa-se por uma letra da string
    print(m)

#(2) Quando se tem um generator range(10)
for i in range(10): #aqui se tem um generator, que começa no zero e vai até o 9, pois o número que aparece
    print(i)        #é excludente 

#pode ser escrito como while, mas é menos intuitivo:
c = 0
while c < len(lista):
    print('usando o while: ', [c])
    c = c + 1 #note que uma vantagem do for é não precisar ficar usando o c = 0

#Quando usar um ou outro?
#Se usa muito o while quando o laço não tem tamanho definido, ou seja, não tem um momento exato para terminar
#Pensando em um jogo, o laço vai continuar rodando até clicar para parar de jogar, que pode ser executado com o break do while


