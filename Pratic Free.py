soma = 0
qnt = 0
for i in range(1, 101):
    if i % 2 == 0:
        soma += i
        qnt += 1
media = soma/qnt
print(media)
