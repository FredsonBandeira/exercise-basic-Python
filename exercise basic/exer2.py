# Write your code here :-)
numbers = [5, 10, 15, 20, 25, 30, 30]
print("lista inicial:")
print(numbers)
print("Soma do 1º e o proximo numero:")
for i in range(len(numbers)):
    if i == 0:
        print(numbers[i])
    else:
        print(numbers[i - 1] + numbers[i])
