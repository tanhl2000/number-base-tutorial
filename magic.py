answer = []
convert = {"T": "1", "F": "0"}
a = input("Enter T if your number is 1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29 or 31 if not enter F: ")
b = input("Enter T if your number is 2, 3, 6, 7, 10, 11, 14, 15, 18, 19, 22, 23, 26, 27, 30 or 31 if not enter F: ")
c = input("Enter T if your number is 4, 5, 6, 7, 12, 13, 14, 15, 20, 21, 22, 23, 28, 29, 30 or 31 if not enter F: ")
d = input("Enter T if your number is 8, 9, 10, 11, 12, 13, 14, 15, 24, 25, 26, 27, 28, 29, 30 or 31 if not enter F: ")
e = input("Enter T if your number is 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30 or 31 if not enter F: ")
answer.append(a)
answer.append(b)
answer.append(c)
answer.append(d)
answer.append(e)
answer = list(reversed(answer))
for i in range (len(answer)):
    answer[i] = convert[(answer[i])]

def basetodec(n):
    ib = 2
    decnum = 0
    ib = int(ib)
    n = list(reversed(n))
    for k in range (len(n)):
        decnum = decnum + (int(n[k]) * (ib**k))
    return decnum

print (basetodec(answer))
