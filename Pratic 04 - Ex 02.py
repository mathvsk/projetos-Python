# Algoritmo de contagem de cédulas (caixa eletronico)

v = int(input('Qual é o valor?: '))
while True:
    if v >= 100:
        c100 = v // 100
        v -= c100 * 100
        print('Cédulas de 100: {}'.format(c100))
        if not v:
            break

    if v >= 50:
        c50 = v // 50
        v -= c50 * 50
        print('Cédulas de 50: {}'.format(c50))
        if not v:
            break

    if v >= 10:
        c10 = v // 10
        v -= c10 * 10
        print('Cédulas de 10: {}'.format(c10))
        if not v:
            break

    if v >= 5:
        c5 = v // 5
        v -= c5 * 5
        print('Cédulas de 5: {}'.format(c5))
        if not v:
            break

    if v:
        c1 = v
        print('Cédulas de 1: {}'.format(v))
        break
