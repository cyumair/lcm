lcm = []  
def LCM(numbers):
    maximum = max(numbers)   
    highestpossiblemultiple = 1
    for i in numbers:                                                # calculating what can be highest possible factor
        highestpossiblemultiple = highestpossiblemultiple * i        # for example higest possible factor for 3 and 4 is 3*4 = 12
                                                                     
    while maximum <= highestpossiblemultiple:                  # if number a has no lcm then highest possible factor is its factor
        mults = 0                                              # so end the loop on that highest possible factor  
        for i in numbers:                                           
            if maximum % i == 0:
                mults += 1    #this will keep a check if all (not one) the numbers in the list are factor of maximum(lcm) 
        if mults == len(numbers):  # if the number(maximum) is divided by all the numbers of list
            lcm.append(maximum)
            break                 #if this happens we found our lcm break out of loop
        else:
            maximum += 1         #else try some other number greater than maximum, that number might be lcm
                   
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
