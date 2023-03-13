answer = 0
last_answer = 0
last = 0
prelast = -1
elem = int(input())
while elem != 0:
    if elem < last and last < prelast:
        answer += 1
    elif elem > last and last > prelast:
        answer += 1
    else:
        if answer > last_answer:
            last_answer = answer
        answer = 1
    prelast = last
    last = elem 
    elem = int(input())

print(max(answer, last_answer))