# Algoritmo que le números inteiros via teclado. Calculando sua media no final do laço [Digite 0 para encerrar o laço]
media = 0
c = 0
media_Final = 0

while True:
    x = int(input('Digite um valor [POSITIVO]: '))
    if not x:
        break
    if x < 0:
        print('Valor inaceitável!')
    media += x
    c += 1
    media_Final = media / c

print(media_Final)