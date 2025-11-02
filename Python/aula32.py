"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
 
entrada = input('Digite um número: ')

if entrada .isdigit():
    entrada_int = int(entrada)
    par_impar = entrada_int % 2 == 0
    par_impar_texto = 'impar'

    if par_impar:
        par_impar_texto = 'par'
    print(f'O número {entrada_int} é {par_impar_texto}')         
else:
    print('Você não digitou um número inteiro.')

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

hora =input('Digite a hora atual, por favor: ')
if hora.isdigit():
    hora_double = int(hora)
    if hora_double >=0.0 and hora_double <=11.00:
        print('Bom dia, meu lindo!')
    elif hora_double >=12.00 and hora_double <= 17.00:
        print('Boa tarde, meu lindo!')
    elif hora_double >=18.00 and hora_double <=23.00:
        print('Boa noite, meu lindo!')
    else:
        print('Hora inválida. Por favor, digite uma hora entre 0 e 23.')    