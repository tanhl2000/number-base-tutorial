# number-base-tutorial
decreading = {'0': '0', '1': '1', '2': '2', '3': '3', '4': '4', '5': '5', '6': '6', '7': '7', '8': '8', '9': '9','A': '10', 'B': '11', 'C': '12', 'D': '13', 'E': '14', 'F': '15'}
decconvert = {'0': '0', '1': '1', '2': '2', '3': '3', '4': '4', '5': '5', '6': '6', '7': '7', '8': '8', '9': '9','10': 'A', '11': 'B', '12': 'C', '13': 'D', '14': 'E', '15': 'F'}
base = input("Please enter the base you want to convert your number to: ")
number = input("Please enter the number you want converted: ")
ibase = input("Please enter the base of the number you want converted: ")

def dectobase(n,b):
    newnumber = []
    n = int(n)
    b = int(b)
    for i in range (n):
        while n > 0:
            remainder = (int(n)%int(b))
            newnumber.append(str(remainder))
            n = n//b
    for i in range (len(newnumber)):
        newnumber[i] = decconvert[(newnumber[i])]
    newnumber = list(reversed(newnumber))
    decnumber = ''.join(newnumber)
    return decnumber

def basetodec(n,ib):
    decnum = 0
    ib = int(ib)
    n = list(reversed(n))
    for k in range (len(n)):
        decnum = decnum + (int(n[k]) * (ib**k))
    return decnum

num = []
if int(ibase) > 9:
    number = str(number)
    for j in range (len(number)):
        num.append(decreading[(number[j])])
    lol = basetodec(num,ibase)
    print (dectobase(lol,base))
elif int(ibase) == 10:
    print(dectobase(number,base))
else:
    lol = basetodec(number,ibase)
    print (dectobase(lol,base))
