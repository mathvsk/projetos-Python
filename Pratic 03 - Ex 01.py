#Algoritmo  para verificar se os valores formam um triangulo

l1 = float(input('Digite o valor do Primeiro lado: '))
l2 = float(input('Digite o valor do Segundo lado: '))
l3 = float(input('Digite o valor do Terceiro lado: '))

if l1 > 0 and l2 > 0 and l3 > 0:
    if l1 + l2 > l3 and l2 + l3 > l1 and l1 + l3 > l2:
        if l1 == l2 and l2 == l3 and l3 == l1:
            print('Voce possui um triangulo Equilátero')
        elif l1 != l2 and l2 != l3 and l3 != l1:
            print('Voce possui um trinagulo Escaleno')
        else:
            print('Voce possui um triangulo Isóceles')