print('=-='*9)
print('Bem Vindo ao Banco Mesquita')
print('=-='*9)
valor = int(input('Qual o valor: R$ '))
total = valor
ced = 50
totced = 0
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'Total de {totced} cédulas de {ced}.')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if total == 0:
            break
print('=-='*9)
print('Finalizando...')
print('Até Mais!')