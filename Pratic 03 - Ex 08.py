# Algoritmo para calcular o valor do produto final [Pagamento à vista – conceder desconto de 5%; Pagamento em 3x – o valor não sofre alterações; Pagamento em 5x – acréscimo de 2%; Pagamento em 10x – acréscimo 8%.]

valor_compra = float(input('Valor da compra: R$'))
pagamento = int(input('Qual a forma de pagamento?\n [1] À vista (5% de desconto)\n '
                      '[2] Parcelado em 3x (sem alterações)\n '
                      '[3] Parcelado em 5x (acréscimo de 2%)\n '
                      '[4] Parcelado em 10x (acréscimo de 10%)\n '))

if pagamento == 1:
    desc = valor_compra * 5/100
    tot = valor_compra - desc
    print('Valor do produto = R${:.2f}\n'
        'Desconto = R${:.2f}\n'
        'Total = R${:.2f}'.format(valor_compra, desc, tot))

elif pagamento == 2:
    tot = valor_compra / 3
    print('Parcelado em 3x = R${:.2f}\n'
          'Valor total = R${:.2f}'.format(tot, valor_compra))

elif pagamento == 3:
    acrescimo = valor_compra * 2/100
    tot = valor_compra + acrescimo
    print('Parcelado em 5x = R${:.2f}\n'
          'Acréscimo de 2% = R${:.2f}\n'
          'valor total = R${:.2f}'.format((tot/5), acrescimo, tot))

elif pagamento == 4:
    acrescimo = valor_compra * 8/100
    tot = valor_compra + acrescimo
    print('Parcelado em 10x = R${:.2f}\n'
          'Acréscimo de 8% = R${:.2f}\n'
          'valor total = R${:.2f}'.format((tot/10), acrescimo, tot))

else:
    print('Opção invalida!')