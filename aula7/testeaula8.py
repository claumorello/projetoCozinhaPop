#laço condicional, indeterminado.
    #contador
contador = 0
    #acumulador
soma = 0
    #inicialização da variável de controle
resp = 'S'

while resp == 's' or resp == 'S':
        n = int(input('Digite um número: '))
        contador = contador = 1
        soma = soma + n #acumula
        #atualiza a variável de controle (resp)
        resp = input('Deseja digitar outro número? (S/N)')

        media = soma/contador
        print('A média é: ', media)
