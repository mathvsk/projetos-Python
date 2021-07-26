
while True:
    idade = int(input('Qual sua idade? '))

    if not idade:
        break
    sexo = str(input('Qual é seu sexo [M/F]? '))
    if sexo == 'M' or sexo == 'm':
        print('Boa noite Senhor, sua idade é {} anos'.format(idade))
    elif sexo == 'F' or sexo == 'f':
        print('Boa noite Senhora, sua idade é {} anos'.format(idade))

print('Encerrando...')