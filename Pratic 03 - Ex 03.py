# Algoritmo que leia o salário do funcionário e seu tempo de empresa, e apresente a bonificação de cada funcionário na tela. (20% + de 5 anos, 10% restante)

sal = float(input('Qual seu salario atual?: '))
empresa = float(input('Qual é seu tempo de empresa?: '))

if empresa > 5:
    bonificacao = sal * 20/100
else:
    bonificacao = sal * 10/100

print('Sua bonificação será de RS${:.2f} Referente ao seu salario de R${:.2f}.\nTotalizando: {:.2f}'.format(bonificacao, sal, bonificacao + sal))