s="aaadddcccgggvvvsaagggbbbrrssshhhbrsffgghatz"
d={}
for i in s:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
for i, count in d.items():
    if count >=1:
        print("{x}: {y}".format(x=i,y=count))