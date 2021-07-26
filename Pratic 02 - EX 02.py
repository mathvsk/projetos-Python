# Algoritmo para calcular o preco a pagar pelo o aluguel do carro.

km = int(input('Qual a quantidade de KM rodado?: '))
dias = int(input('Por quantos dias o carro foi alugado?: '))

valor = (km * 0.15) + (dias * 60)

print('KM = {}KM\n'
      'Dias = {} \n'
      'Valor final = R${:.2f}'.format(km, dias, valor))
