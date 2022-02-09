def multiplication_or_sum(num1, num2):
    # calculate product of two number
    product = num1 * num2
    # check if product is less then 1000
    if product >= 1000:
        return product
    else:
        return num1 + num2



num1=int(input("Digite 1º numero: "))

num2=int(input("Digite 2º numero: "))

x= multiplication_or_sum(num1, num2)
print(x)
