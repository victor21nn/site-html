peso = float(input('Informe o seu peso: '))
altura = float(input('Informe sua altura: '))

imc = peso / (altura * altura)

print(imc)

if (imc < 18.5):
    print('Abaixo do peso')
elif (imc < 25):
    print('Peso Normal')
elif  (imc < 30):
    print('Sobrepeso')
elif  (imc < 35):
    print('Obesidade Grau I')
elif   (imc < 40):
    print('Obesidade Grau II')
else:
    print('Obesidade Grau III ou Mórbida')
