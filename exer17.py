from datetime import datetime

print ('----------------------------------------------------------------------------------------------------------------')
print ('------------------------------Ordenação de Lista com Números Negativos e Positivos------------------------------')
print ('----------------------------------------------------------------------------------------------------------------')

usuario = input('Quem deseja ordenar? ')

hora_atual = datetime.now().hour

if 5 <= hora_atual < 12:
    saudacao = 'Bom dia'
elif 12 <= hora_atual < 18:
    saudacao = 'Boa tarde'
else:
    saudacao = 'Boa noite'
    
print(f' {saudacao}, {usuario}!')

def ordenar():
    numeros = input('Digite os numeros a serem ordenados (SEM A VIRGULA): ')
    coloca_virgula = str.split(numeros)
    lista = [int(x) for x in coloca_virgula]
    ordenador = sorted(lista)
    print(f'{ordenador}')
    
continuar = 'sim'
while continuar.lower() == 'sim':
    ordenar()
    continuar = input('Deseja ordenar outros números? (sim/nao): ')
        
print('Obrigado por usar o sistema!')