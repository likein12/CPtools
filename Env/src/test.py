import itertools


count = 0
for c in itertools.permutations(range(1,75*75+1)):
    count+=1
    if count==1:
        print(*c)
        break