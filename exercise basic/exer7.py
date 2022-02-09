# Write your code here :-)
list = [4, 5, 6, 9, 11, 23]

print("Lista ", list)
element = list.pop(4) # pop que é responsavel para eliminar elemento
print("\n Remover indice 4 da lista ", list)

list.insert(2, element)# insert pra inserir element, 2 é o indice que vai ser inserido o elemento
print("\nAdicionar elemento no  indice 2 \n", list)

list.append(element)
print("\n Adicionar no final da lista ", list)
