f = open("input").readlines()
l = []
for line in f:
    l.append(int(line.strip('\n')))
print l

x = len(l)

def expenses():
    global a
    global b
    global c
    for a in l:
        for b in l:
            for c in l:
                if a+b+c==2020:
                    return(a, b, c)

expenses()
print(a, b, c)
value = a*b*c
print(value)
y = str(x)
print ("list length is " + y)
