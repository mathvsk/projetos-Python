# Algoritmo para calcular as vendas de ingressos, media e arrecadaçao de um estabelecimento

tot_Pessoas = 0
gratuito = 0
tot_Dinheiro = 0
tot_Idade = 0
media = 0

while True:
    idade = int(input('Digite sua idade: '))
    if idade < 3:
        gratuito += 1
        valor = 0
        print('Seu ingresso é Gratuiito!')
    elif idade <= 12:
        valor = 15
        print('Seu ingresso sairá R${}!'.format(valor))
    else:
        valor = 30
        print('Seu ingresso sairá R${}'.format(valor))

    tot_Idade += idade
    tot_Pessoas += 1
    tot_Dinheiro += valor
    media = tot_Idade / tot_Pessoas

    perg = str(input('Deseja continuar [S/N]?: '))
    if perg == 'n' and 'N':
        print('Finalizando...')
        break

print('Total de pessoas que compraram o ingresso foi de: {} sendo {} gratuito(s).\n'
      'Total de dinheiro arrecado foi de: R${}\n'
      'Média de idade foi de: {:.2f}'.format(tot_Pessoas,gratuito, tot_Dinheiro, media))