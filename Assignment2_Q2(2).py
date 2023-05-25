L1=[1,2,3,4,[4,3]]

L2 =[]

for e in L1[0:4]:

    if e in L1[4]:

        L2.append(e)

print(L2)