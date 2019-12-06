newlist = ['test']
def duplicateremovers(lst):
    for i in lst:
        check = 0
        for j in newlist:
            if i != j:
                check += 1
        if check == len(newlist):
            newlist.append(i)

lst= []
userwants = True
while userwants:
    num = int(input('please enter number (0 to stop) '))
    if num == 0:
              userwants = False
    else:
              lst.append(num)
              
duplicateremovers(lst)
newlist.pop(0)
print(newlist)