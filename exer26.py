from datetime import datetime

print ('-----------------------------------------------------------------------------------------')
print ('------------------------------Mesclagem de Dois Dicionários------------------------------')
print ('-----------------------------------------------------------------------------------------')

usuario = input('Quem deseja mesclar? ')

hora_atual = datetime.now().hour

if 5 <= hora_atual < 12:
    saudacao = 'Bom dia'
elif 12 <= hora_atual < 18:
    saudacao = 'Boa tarde'
else:
    saudacao = 'Boa noite'
    
print(f' {saudacao}, {usuario}!')

def mesclador():
    dict1 = eval(input('Digite o primeiro dicionário (ex: {"nome": "John", "idade": 25}): '))
    dict2 = eval(input('Digite o segundo dicionário (ex: {"cidade": "New York", "idade": 30}): '))
    
    mesclado = dict1.copy()
    for chave, valor in dict2.items():
        if chave in mesclado:
            mesclado[chave] += valor
        else:
            mesclado[chave] = valor
    
    print(f'Dicionário mesclado: {mesclado}')

continuar = 'sim'
while continuar.lower() == 'sim':
    mesclador()
    continuar = input('Deseja mesclar mais alguma coisa (sim/nao): ')

print('Obrigado por usar o sistema!')