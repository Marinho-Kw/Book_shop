from time import sleep
from random import randrange

print('='*80)
print('-'*80)
print('Bem vindo a Book shop')
print('-'*80)
print('='*80)
sleep(1)

entrada = input('Digite o seu Email:')
sleep(1)
senha = input('Agora cadastre a sua senha:')
sleep(1)
print('Parece o saldo dac sua carteira é de R$')
saldo = randrange(150, 200)
sleep(1)
print(saldo)
sleep(1)
print('''
Essa é a lista de livros disponiveis para compra
1 = Herry Potter e a Criança Amaldiçoada 150 R$
2 = Mindset 80 R$
3 = Propósito 120 R$
''')
sleep(1)
while True:
    compra = input('Deseja comprar algum deles?:').lower()
    if compra == 'sim':
        sleep(1)
        print('Òtimo! Qual deles você deseja?')
        compra_livro = input(':')

        if compra_livro == '1' or compra_livro == 'Herry Potter e a Criança Amaldiçoada' and saldo > 150 :
            sleep(1)
            print('Òtima escolha, Agora digite a sua senha e o seu email para confirmar a sua compra')
            conf_e = input('Email:')
            sleep(1)
            conf_s = input('Senha:')

            if conf_e == entrada and conf_s == senha:
                print('bom trabalho')

            else:
                print('Senha ou Email invalidos')

        else:
            print('você não tem saldo o suficiente')
            sleep(1)
         
    
    elif compra == 'não' or compra =='nao':
        print('Encerrando o programa')
        sleep(1)
        break
    
    else:
        print('opção invalida')
