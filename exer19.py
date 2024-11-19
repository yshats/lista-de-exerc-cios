from datetime import datetime

print ('-----------------------------------------------------------------------------------------------')
print ('------------------------------Contador de Caracteres de uma Frase------------------------------')
print ('-----------------------------------------------------------------------------------------------')

usuario = input('Quem deseja contar? ')

hora_atual = datetime.now().hour

if 5 <= hora_atual < 12:
    saudacao = 'Bom dia'
elif 12 <= hora_atual < 18:
    saudacao = 'Boa tarde'
else:
    saudacao = 'Boa noite'
    
print(f' {saudacao}, {usuario}!')

def contador():
    frase_usuario = input('Digite uma frase: ')
    quantidade_caracteres = len(frase_usuario)
    
    print(f'A frase "{frase_usuario}" possui {quantidade_caracteres} caracteres.')
    
    def contador_caracteres(frase):
        contador = {}
        for caractere in frase:
            if caractere in contador:
                contador[caractere] += 1
            else:
                contador[caractere] = 1
        return contador

    frase = frase_usuario
    resultado = contador_caracteres(frase)
    print(resultado)
        
continuar = 'sim'
while continuar.lower() == 'sim':
    contador()
    continuar = input('Deseja contar outra frase? (sim/nao): ')

print('Obrigado por usar o sistema!')