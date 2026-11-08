print("hello world")
numbers = [11, 21, 5, 16, 28]
temp = numbers[0]
for num in numbers:
    if temp > num:
        temp = num
print(temp)