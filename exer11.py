from datetime import datetime

print ('-------------------------------------------------------------------------------------')
print ('------------------------------Contador de Palavras Únicas------------------------------')
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

def contador():
    palavras = input('Qual a palavra que deseja contar os caracteres? ')
    palavras_unicas = palavras.lower().split()
    quantidade = len(set(palavras_unicas))
    print(f'A palavra "{palavras}" possui a quantidade de {quantidade} caracteres únicos')
    
continuar = 'sim'
while continuar.lower() == 'sim':
    contador()
    continuar = input('Deseja continuar contando a quantidade de caracteres de outra palavra (sim/nao)? ')
    
print('Obrigado por usar o sistema!')