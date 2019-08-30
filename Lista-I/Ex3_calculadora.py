'''3 - Crie uma classe calculadora com as quatro operações básicas (soma, subtração, multiplicação e divisão).
O usuário deve informar dois números e o programa deve fazer as quatro operações'''

class Calculadora():
    def soma(self):
        n1 = int(input('Digite o primeiro valor: '))
        n2 = int(input('Digite o segundo valor: '))
        print(f'{n1} + {n2} = {n1+n2}')

    def subtracao(self):
        n1 = int(input('Digite o primeiro valor: '))
        n2 = int(input('Digite o segundo valor: '))
        print(f'{n1} - {n2} = {n1-n2}')

    def multiplicacao(self):
        n1 = int(input('Digite o primeiro valor: '))
        n2 = int(input('Digite o segundo valor: '))
        print(f'{n1} * {n2} = {n1*n2}')

    def divisao(self):
        n1 = int(input('Digite o primeiro valor: '))
        n2 = int(input('Digite o segundo valor: '))
        print(f'{n1} / {n2} = {n1/n2}')

nova_calculadora = Calculadora()
calculando = True

print('Calculadora')
while calculando:
    opcao=int(input('\nQual o cálculo desejado?'
                    '\n1: Adição'
                    '\n2: Subtração'
                    '\n3: Multiplicação'
                    '\n4: Divisão'
                    '\n0: Sair\n'))
    if opcao == 1:
        nova_calculadora.soma()
    elif opcao == 2:
        nova_calculadora.subtracao()
    elif opcao == 3:
        nova_calculadora.multiplicacao()
    elif opcao == 4:
        nova_calculadora.divisao()
    elif opcao == 0:
        calculando = False
    else:
        print('Opção inválida, tente novamente.')