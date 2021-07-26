# Escreva um algoritmo em Python em que o usuário escolhe se ele quer comprar maçãs, laranjas ou bananas. Deverá ser apresentado na tela um menu com a opção 1 para maçã, 2 para laranja e 3 para banana.
# Após escolhida a fruta, deve-se digitar quantas unidades se quer comprar. O algoritmo devecalcular o preço total a pagar do produto escolhido e mostrá-lo na tela. Considere que uma maçã custa R$ 2,30, uma laranja R$ 3,60 e uma banana 1,85

varejo = int(input('Digite;\n'
                   '[1] Maçã RS2.30 Uni.\n'
                   '[2] Laranja R$3.60 Uni.\n'
                   '[3] Banana R$1.85 Uni.\n'))

quantidade = int(input('Quantas unidades?:'))

if varejo == 1:
    preco = quantidade * 2.30
elif varejo == 2:
    preco = quantidade * 3.60
elif varejo == 3:
    preco = quantidade * 1.85
else:
    print('Produto inexiste')

print('Total = R${:.2f}'.format(preco))