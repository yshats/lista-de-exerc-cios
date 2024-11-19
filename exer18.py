from datetime import datetime

print ('----------------------------------------------------------------------------------------------------')
print ('------------------------------Soma de Diagonais de uma Matriz Quadrada------------------------------')
print ('----------------------------------------------------------------------------------------------------')

usuario = input('Quem deseja somar? ')

hora_atual = datetime.now().hour

if 5 <= hora_atual < 12:
    saudacao = 'Bom dia'
elif 12 <= hora_atual < 18:
    saudacao = 'Boa tarde'
else:
    saudacao = 'Boa noite'
    
print(f' {saudacao}, {usuario}!')

def matriz():
    matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    for l in range(0, 3):
        for c in range(0, 3):
            matriz[l] [c] = int(input(f'Digite um valor para [{l},{c}]: '))
    
    for l in range(0, 3):
        for c in range(0, 3):
            print(f'[{matriz[l] [c]:^5}]', end='')
        print()
    
    def soma_diagonal_principal():
        soma_diagonal_principal = 0
        for i in range(0, 3):
            soma_diagonal_principal += matriz[i][i]
        return soma_diagonal_principal
    
    print(f'Soma da diagonal principal: {soma_diagonal_principal()}')
    
    def soma_diagonal_secundaria():
        soma_diagonal_secundaria = 0
        for i in range(0, 3):
            soma_diagonal_secundaria += matriz[i][2 - i]
        return soma_diagonal_secundaria
    
    print(f'Soma da diagonal secundária: {soma_diagonal_secundaria()}')
    
continuar = 'sim'
while continuar.lower() == 'sim':
    matriz()
    continuar = input('Deseja somar outra matriz? (sim/nao): ')

print('Obrigado por usar o sistema!')