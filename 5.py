answer = 0
max_number = 0
elem = int(input())
while elem != 0:
    if elem > max_number:
        max_number = elem
        answer = 1
    elif elem == max_number:
        answer += 1
    elem = int(input())
print(answer)