answer = 1
number = int(input())

for i in range(1, number + 1):
    fact = 1
    for num in range(2, number + 1):
            fact *= num
    answer += 1 / fact
print(round(answer, 5))