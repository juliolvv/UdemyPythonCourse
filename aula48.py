"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis: append, insert, pop, del, clear, extend, +
"""



string = 'ABCDE'
lista = ['A', 'B', 'C', 'D', 'E']
print(lista)

"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis:
    append, insert, pop, del, clear, extend, +
Create Read Update   Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)

apped - Adiciona um item ao final da lista
insert - Adiciona um item no índice escolhido
pop - Remove o último item ou o item no índice escolhido
del - Apaga um item no índice escolhido ou a lista inteira
clear - Apaga todos os itens da lista

"""

lista = [10, 20, 30, 40]
print(lista)
lista[2] = 300
print(lista)
del lista[2]
print(lista)
lista.append(500)
lista.pop()
print(lista)

lista_a = [1, 2, 3]
lista_b = [4, 5, 6] 
lista_c = lista_a + lista_b
lista_a.extend(lista_b) # lista_a = lista_a + lista_b
print(lista_c)  

