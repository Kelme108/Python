#Escreva um programa onde terá o nome do professor, o nome da turma e o nome do aluno.
# Peça para escrever as 4 notas que foram tiradas e apresente a média final.
#Mostre todas as informações que foram cadastrados,
# os números armazenados tem que ser decimais e formate para mostrar'''

nome_professor = str(input('digite o nome do professor:')).title()
nome_turma = str(input('digite o nome da turma:')).title()
nome_aluno = str(input('digite o nome do aluno:')).capitalize()
nota1 = float(input('digite o número da primeira nota (Digite com ponto):'))
nota2 = float(input('digite o numero da segunda nota (Digite com ponto):'))
nota3 = float(input('digite o numero da terceira nota (Digite com ponto):'))
nota4 = float(input('digite o numero da quarta nota (Digite com ponto):'))
média = (nota1 + nota2 + nota3 + nota4) / 4
print(f'O professor {nome_professor} do curso de {nome_turma} deu a média de {média} para o aluno {nome_aluno}')