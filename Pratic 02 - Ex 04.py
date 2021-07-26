#Algoritmo para calcular o total de segundos em um dia

dia = int(input('Quantos dias? '))
hora = int(input('Quantas horas? '))
minuto = int(input('Quantos minutos? '))
segundo = int(input('Quantos segundos? '))

totseg = (dia * 86400) + (hora * 3600) + (minuto * 60) + segundo

print('O total de segundos referente aos dados e de: {}s '.format(totseg))