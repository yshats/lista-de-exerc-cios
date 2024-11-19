from datetime import datetime

print ('---------------------------------------------------------------------------------------')
print ('------------------------------Cálculo de Média Aritmética------------------------------')
print ('---------------------------------------------------------------------------------------')

usuario = input('Quem deseja caucular? ')

hora_atual = datetime.now().hour

if 5 <= hora_atual < 12:
    saudacao = 'Bom dia'
elif 12 <= hora_atual < 18:
    saudacao = 'Boa noite'
else:
    saudacao = 'Boa noite'
    
print(f' {saudacao}, {usuario}!')

def media():
    n1 = float(input('Digite os valor da nota 1: '))
    n2 = float(input('Digite os valor da nota 2: '))
    n3 = float(input('Digite os valor da nota 3: '))
    
    valores_escolhidos = [n1, n2, n3]
    
    soma = sum(valores_escolhidos)
    
    media_dos_valores = soma / len(valores_escolhidos)
    
    print(f'A media e {media_dos_valores}')
    
continuar = 'sim'
while continuar.lower() == 'sim':
    media()
    continuar = input('Você deseja continuar cauculando? (sim/nao): ')

print('Obrigado por usar o sistema!')