def dectobase(n):
    b = 2
    newnumber = []
    n = int(n)
    b = int(b)
    for i in range (n):
        while n > 0:
            remainder = (int(n)%int(b))
            newnumber.append(str(remainder))
            n = n//b
    return newnumber

def basetodec(n):
    ib = 2
    decnum = 0
    ib = int(ib)
    n = list(reversed(n))
    for z in range (len(n)):
        decnum += (int(n[z]) * (ib**z))
    return decnum



def magic(low,high):
    ans = []
    low = int(low)
    top = dectobase(high)
    top = list(reversed(top))
    tablesneeded = len(top)
    high = int(high)
    tables = [[] for i in range (tablesneeded)]
    while low <= high:
        binvalue = dectobase(low)
        for j in range (len(binvalue)):
            if binvalue[j] == "1":
                (tables[j]).append(low)
        low = low + 1
    for k in range (tablesneeded):
        talk = "if your number is in this list, repy with a T, if not an F, list: "
        question = ''.join(str(tables[k]))
        if input(talk + question) == "T":
            ans.append("1")
        else:
            ans.append("0")
    ans = basetodec(list(reversed(ans)))
    congrats = "your number is: "
    print (congrats + str(ans))
    return -1


lower = input("please enter the lower range of your number possibility: ")
higher = input("please enter the higher range of your number possibility: ")
if int(lower) > int(higher):
    print ("ERROR: lower > higher")
elif (not lower.isdigit()) or (not higher.isdigit()):
    print ("ERROR: only numbers are allowed")
else:
    magic(lower,higher)
