# Algorotimo de calculadora

op = 0

while op != 5:
    op = int(input('\nDigite;\n'
                   '[1] Adição\n'
                   '[2] Subtração\n'
                   '[3] Multiplicação\n'
                   '[4] Divisão\n'
                   '[5] Sair\n'))

    if op == 1:
        v1 = float(input('Digite o primeiro valor: '))
        v2 = float(input('Digite o segundo valor: '))
        soma = v1 + v2
        print('A soma entre {} + {} = {}'.format(v1, v2, soma))

    elif op == 2:
        v1 = float(input('Digite o primeiro valor: '))
        v2 = float(input('Digite o segundo valor: '))
        subtracao = v1 - v2
        print('A subtração entre {} - {} = {}'.format(v1, v2, subtracao))

    elif op == 3:
        v1 = float(input('Digite o primeiro valor: '))
        v2 = float(input('Digite o segundo valor: '))
        multiplicacao = v1 * v2
        print('A multiplicação entre {} * {} = {}'.format(v1, v2, multiplicacao))

    elif op == 4:
        v1 = float(input('Digite o primeiro valor: '))
        v2 = float(input('Digite o segundo valor: '))
        divisao = v1 / v2
        print('A divisão entre {} / {} = {}'.format(v1, v2, divisao))

    elif op != 5:
        print('Digite uma opção válida!')

    else:
        print('Programa Encerrado!')