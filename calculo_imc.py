altura = float(input('Digite sua altura: ').replace(',','.'))   
peso = float(input('Digite seu peso: ').replace(',','.'))
idade = int(input('Qual a sua idade? '))
calculo = peso // altura **2

if  idade >=15 and calculo < 18.5:
    print('\033[37m MAGREZA \033[m')

elif idade >=15 and calculo >= 18.5 and calculo <= 24.9:
    print('\033[32m NORMAL \033[m')      

elif idade >=15 and calculo >= 25 and calculo <= 29.9:
    print('\033[30m SOBREPESO \033[m')   

elif idade >=15 and calculo >= 30 and calculo <= 34.9:
    print('\033[35m OBESIDADE GRAU 1 \033[m')  

elif idade >=15 and calculo >= 35 and calculo <= 39.9:
    print('\033[36m OBESIDADE GRAU 2 \033[m')   

elif idade >=15 and calculo >= 40:
    print('\033[33m OBESIDADE GRAU 3 \033[m')  

if idade <15 and calculo >=30:
    print('\033[1;31m OBESIDADE INFANTIL \033[m')

if idade <15 and calculo <30:
    print('\033[32m NORMAL \033[m') 


print(f'O calculo utilizado para chegar no resultado foi peso / altura², seu resultado é {calculo}')  