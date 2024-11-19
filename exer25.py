from datetime import datetime

print ('------------------------------------------------------------------------------------------------')
print ('------------------------------Filtro de Números Pares em uma Lista------------------------------')
print ('------------------------------------------------------------------------------------------------')

usuario = input('Quem deseja filtrar? ')

hora_atual = datetime.now().hour

if 5 <= hora_atual < 12:
    saudacao = 'Bom dia'
elif 12 <= hora_atual < 18:
    saudacao = 'Boa tarde'
else:
    saudacao = 'Boa noite'
    
print(f' {saudacao}, {usuario}!')

def filtro():
    numeros = [int(num) for num in input('Digite os números separados por espaço: ').split()]
    pares = [num for num in numeros if num % 2 == 0]
    print(f'Os números pares da lista são: {pares}')

continuar = 'sim'
while continuar.lower() == 'sim':
    filtro()
    continuar = input('Deseja filtrar mais alguma coisa (sim/nao): ')

print('Obrigado por usar o sistema!')