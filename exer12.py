from datetime import datetime

print ('------------------------------------------------------------------------------------------')
print ('------------------------------Números Primos em um Intervalo------------------------------')
print ('------------------------------------------------------------------------------------------')

usuario = input('Quem deseja ver os numeros? ')

hora_atual = datetime.now().hour

if 5 <= hora_atual < 12:
    saudacao = 'Bom dia'
elif 12 <= hora_atual < 18:
    saudacao = 'Boa noite'
else:
    saudacao = 'Boa noite'
    
print(f' {saudacao}, {usuario}!')

def intervalo():
    inicio = int(input('Digite o valor do primeiro número: '))
    fim = int(input('Digite o valor do segundo número: '))

    def eh_primo(numero):
        if numero < 2:
            return False
        for i in range(2, int(numero ** 0.5) + 1):
            if numero % i == 0:
                return False
        return True

    def primos_no_intervalo(inicio, fim):
        primos = []
        for num in range(inicio, fim + 1):
            if eh_primo(num): 
                primos.append(num)
        return primos
    
    primos = primos_no_intervalo(inicio, fim)
    print(f"Números primos entre {inicio} e {fim}: {primos}")
    
continuar = 'sim'
while continuar.lower() == 'sim':
    intervalo()
    continuar = input('Você deseja continuar cauculando? (sim/nao): ')

print('Obrigado por usar o sistema!')