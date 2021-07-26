# Algoritmo que solicita o seu ano de nascimento e o ano atual. Calcule a sua idade e apresente na tela.

nasc = int(input('Informe o ano do seu nascimento: '))
ano = int(input('Informe o ano atual: '))
idade = ano - nasc

if idade < 18:
    print('Voce possui {} anos, portanto não esta nos requisitos minimos para tirar a carteira de habilitação'.format(idade))
else:
    print('Voce possui {} anos,portando atendeu os requistos para tirar a carteira de habilitação'.format(idade))