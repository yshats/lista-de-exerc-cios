from datetime import datetime

print ('----------------------------------------------------------------------------------------------')
print ('------------------------------Verificador de Número Par ou Ímpar------------------------------')
print ('----------------------------------------------------------------------------------------------')

usuario = input('Quem deseja verificar? ')

hora_atual = datetime.now().hour

if 5 <= hora_atual < 12:
    saudacao = 'Bom dia'
elif 12 <= hora_atual < 18:
    saudacao = 'Boa tarde'
else:
    saudacao = 'Boa noite'

print(f'{saudacao}, {usuario}!')

def verificador_produto():
    n1 = int(input('Qual o numero que deseja verificar? '))

    if n1 % 2 == 0:
        print('O numero e par!!!')
    
    elif n1:
        print('O numero e impar!!!')
        
    else:
        print('Voce nao escolheu um valor valido, tente novamente!!!')

continuar = 'sim'
while continuar.lower() == 'sim':
    verificador_produto()
    continuar = input('Você deseja continuar verificando? (sim/nao): ')

print('Obrigado por usar o sistema!')