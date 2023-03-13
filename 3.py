number = int(input())
sum = 0
len = 0
while number != 0:
    sum += number
    len += 1
    number = int(input())
print(sum/len)
