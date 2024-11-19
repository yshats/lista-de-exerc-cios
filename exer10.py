from datetime import datetime

print ('--------------------------------------------------------------------------------------------')
print ('------------------------------Calculadora de Área de Retângulo------------------------------')
print ('--------------------------------------------------------------------------------------------')

usuario = input('Quem deseja caucular? ')

hora_atual = datetime.now().hour

if 5 <= hora_atual < 12:
    saudacao = 'Bom dia'
elif 12 <= hora_atual < 18:
    saudacao = 'Boa noite'
else:
    saudacao = 'Boa noite'
    
print(f' {saudacao}, {usuario}!')

def area():
    altura = float(input('Digite o valor da altura: '))
    base = float(input('Digite o valor da base: '))
    
    area =(altura * base) / 2
    
    print(f'A area do retangulo e {area}')
    
continuar = 'sim'
while continuar.lower() == 'sim':
    area()
    continuar = input('Você deseja continuar cauculando? (sim/nao): ')

print('Obrigado por usar o sistema!')