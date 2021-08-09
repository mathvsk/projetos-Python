while True:
    nota = int(input('Digite uma nota entre 0 e 10'))
    if nota < 0 or nota > 10:
        print('Valor inválido')
    else:
        print('Tudo certo')
        break
