# Algoritmo que solicita o valor do produto e de desconto e calcula o valor final

vproduto = float(input('Qual o valor do produto? '))
vdesconto = int(input('Qual o valor do desconto? [0-100%] '))
vtotal = vproduto - (vproduto * vdesconto/100)

print('Produto = R${}\n'
      'Desconto = {}%\n'
      'Valor Final = R${:.2f}'.format(vproduto, vdesconto, vtotal))