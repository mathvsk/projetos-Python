# Assuma que a média para aprovação é a partir de 7, e que o aluno cursa 3 matérias, somente. Escreva um algoritmo que leia a nota final do aluno em cada matéria, e informe na tela se ele passou de ano ou não.

m1 = float(input('Digite a nota da Primeira matéria: '))
m2 = float(input('Digite a nota da Segunda matéria: '))
m3 = float(input('Digite a nota da Terceira matéria: '))

if m1 >= 7 and m2 >= 7 and m3 >= 7:
    print('Parabéns, você passou!')
else:
    print('Que pena! Você reprovou')