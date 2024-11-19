from datetime import datetime

print ('------------------------------------------------------------------------------')
print ('------------------------------Inversor de String------------------------------')
print ('------------------------------------------------------------------------------')

usuario = input('Quem deseja deseja fazer a inversao? ')

hora_atual = datetime.now().hour

if 5 <= hora_atual < 12:
    saudacao = 'Bom dia'
elif 12 <= hora_atual < 18:
    saudacao = 'Boa tarde'
else:
    saudacao = 'Boa noite'
    
print(f'{saudacao}, {usuario}!')

def inversor():
    palavra = input('Digite a String de sua escolha: ')
    
    string = (palavra) [::-1]
    print(f'{string}')
    
continuar = 'sim'
while continuar.lower() == 'sim':
    inversor()
    continuar = input('Você deseja continuar invertendo as string? (sim/nao): ')

print('Obrigado por usar o sistema!')