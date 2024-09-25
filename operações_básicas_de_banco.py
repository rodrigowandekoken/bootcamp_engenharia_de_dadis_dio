menu = '''
Digite o número da operação desejada:

[1]Saldo
[2]Deposito
[3]Saque
[4]Extrato
[5]Sair

'''

saldo_carteira = 0
limite = 500
extrato = ''
número_saque = 0
limite_saque = 3

while True:
    
    opcao = input(menu)

    if opcao == '1':
       print(f'Seu saldo é de R$',saldo_carteira)


    elif opcao == '2':
         valor = float(input('Digite o valor de depósito: '))

         if valor > 0:
            saldo_carteira += valor 
            extrato += f'\nDeposito R$       {valor: .2f}'

         else:
            print('Operação inválida, tentar novamente')


    elif opcao == '3':
         valor = float(input('Digite o valor para saque: '))

         excedeu_saldo = valor > saldo_carteira

         excedeu_limite = valor > limite

         excedeu_saque = número_saque >= limite_saque

         if excedeu_saldo:
            print('Saldo indisponível no momento')

         elif excedeu_limite:
            print('Não foi possível realizar operação, valor desejado exede o limite.')  

         elif excedeu_saque:
            print('Não foi possível realizar operação, limite de saque diário excedido')

         elif valor > 0:
              saldo_carteira -= valor
              extrato += f'\nSaque R$          {valor: .2f}'
              print('Saque R$',valor,'realizado com sucesso.')
              número_saque += 1
         else:
            print('Operação inválida, tentar novamente')


    elif opcao == '4':
         print('\n========== Extrato Detalhado ==========')
         print('Não teve nenhuma operação' if not extrato else extrato)
         print(f'Seu saldo é de R$ {saldo_carteira: .2f}')
         print('\n=======================================')


    elif opcao == '5':
         print('Acesso finalizado com sucesso. Até breve!')
         break


    else:
         print('Opção inválida, digite o número da operação correta.')  