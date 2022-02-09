numbers = [5, 25, 45, 180, 50]
# iterate each item of a list
for i in numbers:
    if i > 50:
        break
    elif i > 150:
        continue

    elif i % 5 == 0:
        print(i)
