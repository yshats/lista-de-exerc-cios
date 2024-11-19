from datetime import datetime

print ('----------------------------------------------------------------------------------------------------------')
print ('------------------------------Calculadora Básica com Estruturas Condicionais------------------------------')
print ('----------------------------------------------------------------------------------------------------------')

usuario = input('Quem deseja calcular? ')

hora_atual = datetime.now().hour

if 5 <= hora_atual < 12:
    saudacao = 'Bom dia'
elif 12 <= hora_atual < 18:
    saudacao = 'Boa tarde'
else:
    saudacao = 'Boa noite'
    
print(f' {saudacao}, {usuario}!')

def calculadora():
    num1 = float(input('Digite o primeiro número: '))
    num2 = float(input('Digite o segundo número: '))
    operacao = input('Qual operação deseja realizar (+, -, *, /): ')
    
    if operacao == '+':
        resultado = num1 + num2
        print(f'Resultado da soma: {resultado}')
    elif operacao == '-':
        resultado = num1 - num2
        print(f'Resultado da subtração: {resultado}')
    elif operacao == '*':
        resultado = num1 * num2
        print(f'Resultado da multiplicação: {resultado}')
    elif operacao == '/':
        if num2!= 0:
            resultado = num1 / num2
            print(f'Resultado da divisão: {resultado}')
        else:
            print('Não é possível dividir por zero.')

continuar = 'sim'
while continuar.lower() == 'sim':
    calculadora()
    continuar = input('Deseja calcular mais alguma coisa (sim/nao): ')

print('Obrigado por usar o sistema!')