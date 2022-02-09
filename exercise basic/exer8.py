# Write your code here :-)
lista1 = {57, 83, 29}
lista2 = {57, 83, 29, 67, 73, 43, 48}

print("1º lista ", lista1)
print("2º lista ", lista2)

print("O primeiro conjunto é um subconjunto do segundo conjunto -", lista1.issubset(lista2))
'''issubset() método retorna True se todos os elementos de um
conjunto estão presentes em outro conjunto (passado como um argumento).
Caso contrário, retorna False.'''
print("O 2º conjunto é um subconjunto do 1º conjunto - ", lista2.issubset(lista2))

print("O 1º conjunto é superconjunto do 2º conjunto - ", lista1.issuperset(lista2))
print("O 2º conjunto é superconjunto do 1º conjunto - ", lista2.issuperset(lista1))
'''b o código a seguir verifica se a é um superconjunto de b o valor de retorno de issuperset
issuperset retorna verdadeiro se a é um superconjunto de b false se a não é um superconjunto de ...'''

if lista1.issuperset(lista2):
    lista1.clear()

if lista2.issuperset(lista1):
    lista2.clear()

print("1º lista ", lista1)
print("2º lista ", lista2)
