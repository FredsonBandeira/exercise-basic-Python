# Write your code here :-)
list1 = [3, 6, 9, 12, 15, 18, 21]
list2 = [4, 8, 12, 16, 20, 24, 28]
res = list()
print("lista 1 ")
print( list1)
print("lista 2 ")
print( list1)
odd_elements = list1[1::2]
print("\nIndice impar lista 1")
print(odd_elements)

even_elements = list2[0::2]
print("\nIndice par da lista 2")
print(even_elements)

print("\n3º lista")
res.extend(odd_elements)
res.extend(even_elements)
print(res)
