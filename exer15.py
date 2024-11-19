from datetime import datetime
import random

print ('-------------------------------------------------------------------------------')
print ('------------------------------Jogo de Adivinhação------------------------------')
print ('-------------------------------------------------------------------------------')

usuario = input('Quem deseja jogar? ')

hora_atual = datetime.now().hour

if 5 <= hora_atual < 12:
    saudacao = 'Bom dia'
elif 12 <= hora_atual < 18:
    saudacao = 'Boa noite'
else:
    saudacao = 'Boa noite'
    
print(f' {saudacao}, {usuario}!')

def edivinha():
    numero_secreto = random.randint(1, 100)
    tentativas = 10
    
    print('Escolhendo um número de 1 a 100')
    
    print('Começando...')
    
    for i in range(tentativas):
        print(f'Tentativa {i+1}:')
        print(f'Você tem {tentativas - i} tentativas restantes.')
        
        palpite = int(input('Chute um numero: '))
    
        if numero_secreto == palpite:
            print('Parabéns, você acertou!')
            return True
        elif numero_secreto > palpite:
            print('Você errou! O número secreto é maior.')           
        else:
            print('Você errou! O número secreto é menor.')
            
        if tentativas - i == 1:
            print('Você não conseguiu adivinhar o número.')
            print(f'O número secreto era {numero_secreto}.')
        
        if tentativas - i == 2:
            print('Você está quase acertando.')
            continue
        
        elif tentativas - i == 3:
            print('Você está perto de acertar.')
            continue
        
        elif tentativas - i == 4:
            print('Você está longe de acertar.')
            continue
        
        elif tentativas - i == 5:
            print('Você está muito longe de acertar.')
            continue
    
continuar = 'sim'
while continuar.lower() == 'sim':
    edivinha()
    continuar = input('Deseja jogar novamente? (sim/nao): ')
        
print('Obrigado por jogar!')
