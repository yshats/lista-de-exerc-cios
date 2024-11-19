from datetime import datetime

print ('--------------------------------------------------------------------------------------------')
print ('------------------------------Contagem de Números em uma Lista------------------------------')
print ('--------------------------------------------------------------------------------------------')

usuario = input('Quem gostaria de contar os numeros? ')

hora_atual = datetime.now().hour

if 5 <= hora_atual < 12:
    saudacao = 'Bom dia'
elif 12 <= hora_atual < 18:
    saudacao = 'Boa tarde'
else:
    saudacao = 'Boa noite'

print(f'{saudacao}, {usuario}!')

def contador():
    numeros = int(input('Digite a lista que deseja fazer a contagem? '))

    quantidade = len(numeros)

    print(f'A quantidade de numeros e {quantidade}')
    
continuar = 'sim'
while continuar.lower():
    contador()
    continuar = input('Deseja contar a quantidade de caracteres de outra palavra (sim/nao)? ')
    
print('Obrigado por usar o sistema!!!')