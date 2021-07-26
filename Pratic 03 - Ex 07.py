# Escreva um algoritmo que leia dois valores numéricos e que pergunte ao usuário qual operação ele deseja realizar: adição (+), subtração (-), multiplicação (*) ou divisão (/). Exiba na tela o resultado da operação desejada.

v1 = float(input('Digite o primeiro valor: '))
v2 = float(input('Digite o segundo valor: '))

calc = int(input('Escolha a opção para a operação que deseja fazer;\n'
                 '[1] Para Somar [+]\n'
                 '[2] Para Diminuir [-]\n'
                 '[3] Para Multiplicar [*]\n'
                 '[4] Para Dividir [/]\n'))

if calc == 1:
    res = v1 + v2
    print('Resultado = {:.2f}'.format(res))
elif calc == 2:
    res = v1 - v2
    print('Resultado = {:.2f}'.format(res))
elif calc == 3:
    res = v1 * v2
    print('Resultado = {:.2f}'.format(res))
elif calc == 4:
    res = v1/ v2
    print('Resultado = {:.2f}'.format(res))
else:
    print('Operação Inexistente!')


