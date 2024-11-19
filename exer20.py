from datetime import datetime

print ('--------------------------------------------------------------------------------------------------------')
print ('------------------------------Gerador de Números da Sequência de Fibonacci------------------------------')
print ('--------------------------------------------------------------------------------------------------------')

usuario = input('Quem deseja gerar? ')

hora_atual = datetime.now().hour

if 5 <= hora_atual < 12:
    saudacao = 'Bom dia'
elif 12 <= hora_atual < 18:
    saudacao = 'Boa tarde'
else:
    saudacao = 'Boa noite'
    
print(f' {saudacao}, {usuario}!')

def fibonacci(n):
    sequencia = [0, 1]
    while len(sequencia) < n:
        sequencia.append(sequencia[-1] + sequencia[-2])
    return sequencia[:n]
    
def gerar_fibonacci():
    n = int(input("Digite um número: "))
    resultado = fibonacci(n)
    print(f"Os {n} primeiros números da sequência de Fibonacci são: {resultado}")

continuar = 'sim'
while continuar.lower() == 'sim':
    gerar_fibonacci()
    continuar = input('Deseja gerar outros números (sim/nao): ')

print('Obrigado por usar o sistema!')