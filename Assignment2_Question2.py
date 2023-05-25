L=[1,2,3,4,5,6,7,8,9,10]

minimum,maximum=1,0

for e in L:

    if e>maximum:

        maximum=e

s = sum(L)

length = len(L)

Avg=s/length

if e<minimum:

    minimum=e

print(maximum)

print(Avg)

print(minimum)