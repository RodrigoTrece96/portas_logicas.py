#SIMULANDO O SISTEMA DE NOTAS DA UFRJ

#entrando com as notas da P1 e da P2

nota_p1 = float(input('Digite sua nota da P1: '))
nota_p2 = float(input('Digite sua nota de P2: '))

media = (nota_p1 + nota_p2)/2 

#caso a media seja menor que 7, entrar com a nota da P3

if media >= 7.0:
    aux = 'Aprovado' #usar coisas dentro do escopo é bom para poupar memória
    print(aux)
elif media >= 3.0:
    nota_p3 = float(input('Digite sua nota da P3: '))
    media = (nota_p1 + nota_p2 + nota_p3)/3
    if media >= 5.0:
        aux2 = 'Aprovado com PF'
        print(aux2)
    else:
        aux3 = 'Reprovado'
        print(aux3)
else:
    aux4 = 'Reprovado por nota'
    print(aux4)
