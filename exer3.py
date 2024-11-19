from datetime import datetime

print ('------------------------------------------------------------------------------------')
print ('------------------------------Conversor de Temperatura------------------------------')
print ('------------------------------------------------------------------------------------')

usuario = input('Quem deseja usar o conversor? ')

hora_atual = datetime.now().hour

if 5 <= hora_atual < 12:
    saudacao = 'Bom dia'
elif 12 <= hora_atual < 18:
    saudacao = 'Boa tarde'
else:
    saudacao = 'Boa noite'

print(f'{saudacao}, {usuario}!')

def conversor():
    graus_celsius = int(input('Digite o valor em graus °C: '))

    fahrenheit = graus_celsius * 1.8 + 32

    print(f'o valor da temperatura para Fahrenheit e igual a {fahrenheit}!!!')
    
continuar = 'sim'
while continuar.lower() == 'sim':
    conversor()
    continuar = input('Deseja converter outra temperatura (sim/nao)? ')
    
print('Obrigado por usar o sistema!')