from datetime import datetime

print ('-------------------------------------------------------------------------------------------')
print ('------------------------------Contagem de Vogais e Consoantes------------------------------')
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

def vogais_consoantes():
    frase = input('Digite uma frase: ')
    frase = frase.lower()
    vogais = 0
    consoantes = 0
    
    for letra in frase:
        if letra in 'aeiou':
            vogais += 1
        elif letra.isalpha():
            consoantes += 1
            
    print(f'Número de vogais: {vogais}')
    print(f'Número de consoantes: {consoantes}')

continuar = 'sim'
while continuar.lower() == 'sim':
    vogais_consoantes()
    continuar = input('Deseja contar outras consoantes e consoantes (sim/nao): ')

print('Obrigado por usar o sistema!')