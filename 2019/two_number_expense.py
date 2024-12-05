f = open("input").readlines()
l = []
for line in f:
    l.append(int(line.strip('\n')))
print l

x = len(l)

def expenses():
    global a
    global b
    for a in l:
        for b in l:
            if a+b==2020:
                return(a, b)

expenses()
print(a, b)
value = a*b
print(value)
y = str(x)
print ("list length is " + y)
