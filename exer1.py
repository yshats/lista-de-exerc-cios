from datetime import datetime

print ('---------------------------------------------------------------------------------------')
print ('------------------------------Calculadora de Soma Simples------------------------------')
print ('---------------------------------------------------------------------------------------')

usuario = input('Quem deseja caucular? ')

hora_atual = datetime.now().hour

if 5 <= hora_atual < 12:
    saudacao = 'Bom dia'
elif 12 <= hora_atual < 18:
    saudacao = 'Boa tarde'
else:
    saudacao = 'Boa noite'

print(f'{saudacao}, {usuario}!')

def soma_produto():
    n1 = int(input('Qual o primeiro numero? '))
    n2 = int(input('Qual o segundo numero? '))

    soma = n1 + n2

    print(f'A soma de {n1} mais {n2} e igual a {soma}')

continuar = 'continuar'
while continuar.lower() == 'continuar':
    soma_produto()
    continuar = input('Você deseja continuar calculando, ou deseja fechar o programa? (continuar/fechar): ')

print('Obrigado por usar o sistema!')