divisors = []
def gcd(numbers):
    mindivisor = min(numbers)
    currentdivisor = 2
    for i in range(2, mindivisor + 1):
        check = 0  # to keep a check that all the numbers of the list are factors of divisor or not
        for j in numbers:
            if j % currentdivisor == 0:
                check += 1
        if check == len(numbers):
            divisors.append(i)
        
numbers = []
userwants = True
while userwants:
    num = int(input('please enter number (0 to stop) '))
    if num == 0:
              userwants = False
    else:
              numbers.append(num)
gcd(numbers)
if len(divisors) == 0:
              print('GCD is 1')
else:
              print('GCD is ', max(divisors))
    