lcm = []
def LCM(numbers):
    maximum = max(numbers)
    highestpossiblemultiple = 1
    for i in numbers:
        highestpossiblemultiple = highestpossiblemultiple * i
    
    while maximum <= highestpossiblemultiple:
        mults = 0
        for i in numbers:
            if maximum % i == 0:
                mults += 1
        if mults == len(numbers):
            lcm.append(maximum)
            break
        else:
            maximum += 1
        
            
            
                
numbers = []
check = 1
while check == 1:
    n = int(input('please enter number '))
    numbers.append(n)
    check = int(input('press 1 to add more numbers '))

LCM(numbers)
if len(lcm) == 0:
    print('no lcm')
else:
    print('Lcm is ' , min(lcm))