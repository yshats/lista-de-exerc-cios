from datetime import datetime

print ('-----------------------------------------------------------------------------------------')
print ('------------------Remoção de Elementos Duplicados de uma Lista Aninhada------------------')
print ('-----------------------------------------------------------------------------------------')

usuario = input('Quem deseja remover? ')

hora_atual = datetime.now().hour

if 5 <= hora_atual < 12:
    saudacao = 'Bom dia'
elif 12 <= hora_atual < 18:
    saudacao = 'Boa tarde'
else:
    saudacao = 'Boa noite'
    
print(f' {saudacao}, {usuario}!')

def remocao():
    lista_aninhada = []
    
    while True:
        sublista = []
        while True:
            numero = input('Digite um numero (0 para sair): ')
            if numero == '0':
                break
            sublista.append(int(numero))
            
        if sublista:
            lista_aninhada.append(sublista)
        else:
            break
    
    nova_lista_aninhada = []
    for sublista in lista_aninhada:
        nova_sublista = []
        [nova_sublista.append(item) for item in sublista if item not in nova_sublista]
        nova_lista_aninhada.append(nova_sublista)
    
    print(f'Lista aninhada sem duplicados: {nova_lista_aninhada}')

continuar = 'sim'
while continuar.lower() == 'sim':
    remocao()
    continuar = input('Deseja remover mais alguma coisa (sim/nao): ')

print('Obrigado por usar o sistema!')