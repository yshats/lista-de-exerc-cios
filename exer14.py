from datetime import datetime

print ('--------------------------------------------------------------------------------------')
print ('------------------------------Verificador de Palíndromos------------------------------')
print ('--------------------------------------------------------------------------------------')

usuario = input('Quem deseja verificar? ')

hora_atual = datetime.now().hour

if 5 <= hora_atual < 12:
    saudacao = 'Bom dia'
elif 12 <= hora_atual < 18:
    saudacao = 'Boa noite'
else:
    saudacao = 'Boa noite'
    
print(f' {saudacao}, {usuario}!')

def verifica_palindromo():
    palavra = input('Digite a palavra que deseja verificar: ')
    palavra_verificar = palavra.lower().split()
    if palavra_verificar == palavra_verificar[::-1]:
        print(f'{palavra} e um palindromo.')
        return True
    
    else:
        print(f'{palavra} não é um palindromo.')
        return False
    
continuar = 'sim'
while continuar.lower() == 'sim':
    verifica_palindromo()
    continuar = input('Deseja verificar outra palavra (sim/nao)? ')
    
print('Obrigado por usar o sistema!')