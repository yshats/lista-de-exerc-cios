from datetime import datetime

print ('-------------------------------------------------------------------------------------------')
print ('------------------------------Contador de Palavras Frequentes------------------------------')
print ('-------------------------------------------------------------------------------------------')

usuario = input('Quem deseja contar? ')

hora_atual = datetime.now().hour

if 5 <= hora_atual < 12:
    saudacao = 'Bom dia'
elif 12 <= hora_atual < 18:
    saudacao = 'Boa tarde'
else:
    saudacao = 'Boa noite'
    
print(f' {saudacao}, {usuario}!')

def frequentes():
    texto = input('Digite o texto: ')
    palavras = texto.lower().split()
    palavras_frequentes = {}
    
    for palavra in palavras:
        if palavra in palavras_frequentes:
            palavras_frequentes[palavra] += 1
        else:
            palavras_frequentes[palavra] = 1
    
    palavras_mais_frequentes = sorted(palavras_frequentes.items(), key=lambda x: x[1], reverse=True)[:5]
    
    print('5 palavras mais frequentes:')
    for palavra, frequencia in palavras_mais_frequentes:
        print(f'{palavra}: {frequencia}')

continuar = 'sim'
while continuar.lower() == 'sim':
    frequentes()
    continuar = input('Deseja contar mais alguma coisa (sim/nao): ')

print('Obrigado por usar o sistema!')