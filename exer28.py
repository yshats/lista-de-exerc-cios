from datetime import datetime

print ('---------------------------------------------------------------------------------')
print ('------------------------------Verificador de Sudoku------------------------------')
print ('---------------------------------------------------------------------------------')

usuario = input('Quem deseja verificar? ')

hora_atual = datetime.now().hour

if 5 <= hora_atual < 12:
    saudacao = 'Bom dia'
elif 12 <= hora_atual < 18:
    saudacao = 'Boa tarde'
else:
    saudacao = 'Boa noite'
    
print(f' {saudacao}, {usuario}!')

def verificar_sudoku(tabuleiro):
    def verificar_unicos(lista):
        return len(lista) == len(set(lista))

    for linha in tabuleiro:
        if not verificar_unicos([num for num in linha if num != 0]):
            return False

    for coluna in zip(*tabuleiro):
        if not verificar_unicos([num for num in coluna if num != 0]):
            return False

    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            bloco = [tabuleiro[x][y] for x in range(i, i+3) for y in range(j, j+3) if tabuleiro[x][y] != 0]
            if not verificar_unicos(bloco):
                return False

    return True

def sudoku():
    tabuleiro = [[0 for x in range(9)] for y in range(9)]
    
    for i in range(9):
        for j in range(9):
            num = int(input(f'Digite o número [{i+1},{j+1}]: '))
            if num < 1 or num > 9:
                print('Número inválido. Digite um número entre 1 e 9.')
                return
            tabuleiro[i][j] = num
    
    if verificar_sudoku(tabuleiro):
        print('O tabuleiro de Sudoku é válido!')
    else:
        print('O tabuleiro de Sudoku não é válido.')

continuar = 'sim'
while continuar.lower() == 'sim':
    sudoku()
    continuar = input('Deseja verificar mais alguma coisa (sim/nao): ')

print('Obrigado por usar o sistema!')