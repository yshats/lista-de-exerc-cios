from datetime import datetime

print ('-------------------------------------------------------------------------------------------')
print ('------------------------------Remoção de Elementos Duplicados------------------------------')
print ('-------------------------------------------------------------------------------------------')

usuario = input('Quem deseja remover? ')

hora_atual = datetime.now().hour

if 5 <= hora_atual < 12:
    saudacao = 'Bom dia'
elif 12 <= hora_atual < 18:
    saudacao = 'Boa tarde'
else:
    saudacao = 'Boa noite'
    
print(f' {saudacao}, {usuario}!')

def remove_elementos():
    numeros = list(map(int, input('Digite os numeros separados por virgula: ').split(',')))
    numeros_sem_duplicados = list(set(numeros))
    return numeros_sem_duplicados

def mostrar_lista(numeros_sem_duplicados):
    print(f'A lista sem elementos duplicados é: {numeros_sem_duplicados}')

mostrar_lista(remove_elementos())

continuar = 'sim'
while continuar.lower() == 'sim':
    remove_elementos()
    continuar = input('Deseja remover outros números duplicados(sim/nao): ')

print('Obrigado por usar o sistema!')