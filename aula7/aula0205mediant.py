#laço contado while
#inicialização da variável de controle (contador)

contador = 1

while contador <= 5:
    n1 = float(input('Digite a nota 1: '))
    n2 = float(input('Difite a nota 2 : '))
    media = ((n1+n2)/2)
    print('A média é: ', media)
    #atualização da variável de controle
    contador = contador + 1

    #laço condicional, indeterminado.
    #contador
    contador = 0
    #acumulador
    soma = 0 
    #inicialização da variável de controle
    resp = 's'

    while resp == 's' or resp == 'S':
        n = int(input('Digite um número: '))
        contador = contador = 1
        soma = soma + n #acumula
        #atualiza a variável de controle (resp)
        resp = input('Deseja digitar outro número? (S/N)')

        media = soma/contador
        print('A média é: ', media)


