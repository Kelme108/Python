'''Soma Par e Impar
Crie um programa que o usuario pode digitar quantos números desejar, 
no final do programa mostre quantos números par ele digitou, quantos números impar ele digitou,
 a soma dos valores do números pares, a soma dos valores dos números impares'''

numeros_pares = []
numeros_impares = []
while True:
    num = int(input("Digite um número (digite 0 para parar): "))
    if num == 0:
        break
    if num % 2 == 0:
        numeros_pares.append(num)
    else:
        numeros_impares.append(num)
soma_pares = sum(numeros_pares)
soma_impares = sum(numeros_impares)
quantidade_pares = len(numeros_pares)
quantidade_impares = len(numeros_impares)
print(f"\nForam digitados {quantidade_pares} números pares, com soma total de {soma_pares}.")
print(f"Foram digitados {quantidade_impares} números ímpares, com soma total de {soma_impares}.")