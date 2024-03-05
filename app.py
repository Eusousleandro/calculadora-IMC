titulo = str('Calculadora IMC')
print(titulo)

nome = str(input('Digite o seu nome completo: '))

altura = float(input('Digite a sua altura: '))
peso = float(input('Digite o seu Peso: '))
resultado = peso / (altura * altura)
print(f'{nome} seu Imc é: ',  resultado)

if resultado < 17:
    print("Muito abaixo do peso")
elif resultado >= 17 and resultado <= 19:
    print("Abaixo do peso")
elif resultado >= 18 and resultado <= 25:
    print("Peso normal")
elif resultado >= 25 and resultado <= 30:
    print("Acima do peso")
elif resultado >= 30 and resultado <= 35:
    print("Obesidade grau I")
elif resultado >= 35 and resultado <= 40:
    print("Obesidade grau II")
else: 
    print("Obesidade grau III")