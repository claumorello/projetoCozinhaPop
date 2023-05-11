#entrada de dados
numero = int(input('Digite um número para cálculo da tabuada: '))

for i in range(11):
    print(numero, '*', i, '=', numero*i)


#contador = contador = 1 (valor fixo) e no acumulador será acumulador + variável (valor inicial da variável sempre tem que ser igual a 0)
#0 = elemento neutro da soma

#acumulador
soma = 0

for i in range(10):
    n = float(input('Digite um número: '))
    #acumula o valor digitado = somatória
    soma = soma + n

    print('A soma dos valores digitados é: ', soma)


soma = 0

for i in range(10):
    n = float(input(str(i+('Digite um número: '))))
    #acumula o valor digitado = somatória
    soma = soma + n

    print('A soma dos valores digitados é: ', soma)

    
