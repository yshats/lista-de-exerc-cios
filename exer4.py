from datetime import datetime

print ('-------------------------------------------------------------------------------------------------')
print ('------------------------------Contador de Caracteres em uma Palavra------------------------------')
print ('-------------------------------------------------------------------------------------------------')

usuario = input('Quem gostaria de contar os caracteres? ')

hora_atual = datetime.now().hour

if 5 <= hora_atual < 12:
    saudacao = 'Bom dia'
elif 12 <= hora_atual < 18:
    saudacao = 'Boa tarde'
else:
    saudacao = 'Boa noite'

print(f'{saudacao}, {usuario}!')

def contador():
    palavra = input('Qual a palavra que deseja contar os caracteres? ')

    quantidade = len(palavra)

    print(f'A palavra "{palavra}" possui a quantidade de {quantidade} caracteres')
    
continuar = 'sim'
while continuar.lower():
    contador()
    continuar = input('Deseja contar a quantidade de caracteres de outra palavra (sim/nao)? ')
    
print('Obrigado por usar o sistema!!!')