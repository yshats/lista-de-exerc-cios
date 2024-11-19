from datetime import datetime

print ('------------------------------------------------------------------------------')
print ('------------------------------Gerador de Tabuada------------------------------')
print ('------------------------------------------------------------------------------')

usuario = input('Quem deseja gerar a taboada? ')

hora_atual = datetime.now().hour

if 5 <= hora_atual < 12:
    saudacao = 'Bom dia'
elif 12 <= hora_atual < 18:
    saudacao = 'Boa tarde'
else:
    saudacao = 'Boa noite'

print(f'{saudacao}, {usuario}!')

def tabuada():  
    numero = int(input('Digite o numero desejado: '))

    for i in range(1, 11):
        resultado = numero * i
        print(f'{numero} x {i} = {resultado}')
        0
continuar = 'sim'
while continuar.lower() == 'sim':
    tabuada()
    continuar = input('Deseja saber sobre outra tabuada (sim/nao)? ')
    
print('Obrigado por usar o sistema!')