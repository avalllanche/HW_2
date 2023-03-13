x = int(input())

if x == 0:
    divider = "¯\_(ツ)_/¯"
elif x == 1:
    divider = 1
else:
    divider = 2 
    for i in range(2, int(x/2)+1): 
        if x % i == 0:
            divider += 1
print(divider)