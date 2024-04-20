'''Pagamento
Crie um programa onde leia o valor da compra e 
fale para o usuário os tipos de pagamento que oferece:
Avista Dinheiro
Avista Cartão
Avista PIX
2x no Cartão
3x ou mais no Cartão
Após selecionar fale para ele de acordo com o selecionado
 qual será o valor com desconto ou juros que será dado:
10% de desconto
2% de desconto
25% de desconto
0% de desconto
20% de juros
'''

valor_compra = float(input('Digite o valor da sua compra: R$').replace(',','.'))
print('1-A vista Dinheiro\n2-A vista Cartão\n3-A vista PIX\n4-2x no Cartão\n5-3x ou mais no Cartão')

opção_pagamento = int(input('Selecione a opção de pagamento:'))
if opção_pagamento==1:
    calculo = valor_compra * 0.90
    print(f'O seu produto de {valor_compra} com a opção 1 vai custar no final:{calculo}')
    
elif opção_pagamento==2:
    calculo = valor_compra *0.98
    print(f'O seu produto de {valor_compra} com a opção 2 vai custar no final:{calculo}')
    
elif opção_pagamento==3:
    calculo = valor_compra * 0.75
    print(f'O seu produto de {valor_compra} com a opção 3 vai custar no final:{calculo}')

elif opção_pagamento==4:
    calculo = valor_compra 
    print(f'O seu produto {valor_compra} com a opção 3 vai custar no final:{calculo}') 

elif opção_pagamento==5:
    calculo = valor_compra + valor_compra * 1.20

else:
    print('Digite uma opção válida.')    
   
print(f'O seu produto de {valor_compra} com a opção 3 vai custar no final:{calculo}')  