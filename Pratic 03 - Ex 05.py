# Escreva um algoritmo que lê um valor inteiro qualquer. Após, verifique se este valor está contido dentro dos seguintes intervalos: -100 <= x <= -1 e 1 <= x <= 100. Imprima na tela  uma mensagem caso ele esteja em um dos intervalos.

value = int(input('Digite qualquer valor [-100... 100]: '))

if -100 <= value <= -1 or 1 <= value <=100:
    print('Seu numero esta entre um dos intervalos')
else:
    print('Seu numero nao faz parte desse intervalo')