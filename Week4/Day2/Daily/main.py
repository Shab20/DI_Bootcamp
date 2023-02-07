num = int(input("Enter a number: "))
length = int(input("Enter a length: "))

result = []
for i in range(1, length+1):
    result.append(num * i)
print(result)
