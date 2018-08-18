# python 2.7.12

peso = float(input('Insira o peso: '))
print(peso)
altura = float(input('Insira a altura: '))
print(altura)
imc = (peso / (altura * altura))
ideal1 = ((altura * altura) * 18.52)
ideal2 = ((altura * altura) * 24.97)

perda1 = round(peso - ideal2)
perda2 = round(peso - ideal1)
pideal1 = round(ideal1)
pideal2 = round(ideal2)

print('Seu IMC e:', round(imc, 2))

if imc < 16.99:
    print('Muito abaixo do peso')
    print('Voce necessitaria ganhar aproximadamente entre', round(ideal1 - peso), 'e', round(ideal2 - peso), 'kg para atingir o peso ideal(', pideal1, 'e', pideal2, 'kg)')

elif 17.0 < imc < 18.49:
    print('Abaixo do peso')
    print('Voce necessitaria ganhar aproximadamente entre', round(ideal1 - peso), 'e', round(ideal2 - peso),
          'kg para atingir o peso ideal(', pideal1, 'e', pideal2, 'kg)')

elif 18.5 < imc < 24.99:
    print('Parabens, voce esta no peso ideal')

elif 25.0 < imc < 29.99:
    print('Voce esta acima do peso')
    print('Voce necessitaria perder aproximadamente entre', perda1, 'e', perda2,
          'kg para atingir o peso ideal(', pideal1, 'kg e', pideal2, 'kg)')

elif 30.0 < imc < 34.99:
    print('Voce esta com Obesidade Grau I')
    print('Voce necessitaria perder aproximadamente entre', perda1, 'e', perda2,
          'kg para atingir o peso ideal(', pideal1, 'kg e', pideal2, 'kg)')


elif 35.00 < imc < 39.99:
    print('Voce esta com Obesidade Grau II (Severa)')
    print('Voce necessitaria perder aproximadamente entre', perda1, 'e', perda2,
          'kg para atingir o peso ideal(', pideal1, 'kg e', pideal2, 'kg)')

elif imc > 40:
    print('Voce esta com Obesidade Grau III (Morbida)')
    print('Voce necessitaria perder aproximadamente entre', perda1, 'e', perda2,
          'kg para atingir o peso ideal(', pideal1, 'kg e', pideal2, 'kg)')
