
idade = int(input("Digite sua idade: "))

if idade < 16:
    print("Não Eleitor")
elif idade >= 18 and idade <= 65:
    print("Eleitor Obrigatório")
elif idade >=16 and idade <18:
    print("Eleitor Facultativo")
else:
    idade > 65, print("Eleitor Facultativo")
    
