vl1 = float(input("Digite o primeiro valor: "))
vl2 = float(input('Digiter o segundo valor: '))
op = input("Digite a operação pretendida sendo (soma, subtracao, multiplicacao ou divisao): ")

if op == 'soma':
    print (vl1 + vl2)
elif op == 'subtracao':
    print(vl1 - vl2)
elif op == 'multiplicacao':
    print(vl1 * vl2)
else:
    op == 'divisao', print(vl1 // vl2)