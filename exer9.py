from datetime import datetime

print ('-------------------------------------------------------------------------------------')
print ('------------------------------Verificador de Maioridade------------------------------')
print ('-------------------------------------------------------------------------------------')

usuario = input('Qual o seu nome? ')

hora_atual = datetime.now().hour

if 5 <= hora_atual < 12:
    saudacao = 'Bom dia'
elif 12 <= hora_atual < 18:
    saudacao = 'Boa tarde'
else:
    saudacao = 'Boa noite'

print(f'{saudacao}, {usuario}!')

def verificar():
    idade = int(input('Digite a sua idade para que possa verificar: '))
    
    if idade >= 18:
        print(f'{usuario} voce e maior de idade')
    else:
        print(f'{usuario} voce e menor de idade')
        
continuar = 'sim'
while continuar.lower() == 'sim':
    verificar()
    continuar = input('Você deseja continuar verificando? (sim/nao): ')

print('Obrigado por usar o sistema!')