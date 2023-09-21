print('Calculadora IMC\n')

altura = float(input("Digite sua Altura: "))
peso = float(input("Digite seu Peso: "))

imc = peso/(altura*altura)

print('Seu IMC é: ', imc)

if imc < 18.5:
    print('Baixo Peso')
elif imc >= 18.5 and imc <= 24.99:
    print('Peso Normal')
elif imc >= 25 and imc <= 29.99:
    print('Sobrepeso')
elif imc > 30:
    print('Obesidade')