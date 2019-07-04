def Multiples(value):    
    Sum = 0    
    for i in range(1,value):
        if i%3 == 0:
            Sum += i
        elif i%5 == 0:
            Sum += i
        elif i%15 == 0:
            Sum -= i

    return Sum
    
    
print(Multiples(1000))