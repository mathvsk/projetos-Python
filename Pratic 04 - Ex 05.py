# algoritmo que calcule a média dos números pares de 1 até 100. Utilizando o FOR
par = 0
total = 0

for i in range(1, 101):
    if i % 2 == 0:
        par += i
        total += 1

media = par / total

print(media)