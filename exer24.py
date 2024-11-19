from datetime import datetime

print ('-----------------------------------------------------------------------------------')
print ('------------------------------Verificação de Anagrama------------------------------')
print ('-----------------------------------------------------------------------------------')

usuario = input('Quem deseja verificar? ')

hora_atual = datetime.now().hour

if 5 <= hora_atual < 12:
    saudacao = 'Bom dia'
elif 12 <= hora_atual < 18:
    saudacao = 'Boa tarde'
else:
    saudacao = 'Boa noite'
    
print(f' {saudacao}, {usuario}!')

def verificar():
    palavra1 = input('Digite a primeira palavra: ')
    palavra2 = input('Digite a segunda palavra: ')
    
    palavra1 = palavra1.lower().replace(' ', '')
    palavra2 = palavra2.lower().replace(' ', '')
    
    if sorted(palavra1) == sorted(palavra2):
        print(f'{palavra1} e {palavra2} sao anagramas.')
    else:
        print(f'{palavra1} e {palavra2} nao sao anagramas.')

continuar = 'sim'
while continuar.lower() == 'sim':
    verificar()
    continuar = input('Deseja verificar mais alguma coisa (sim/nao): ')

print('Obrigado por usar o sistema!')