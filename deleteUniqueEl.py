from collections import defaultdict
arr=[1,2,3,5,6,6]
d=defaultdict(int)
for i in arr:
    d[i]+=1
for i in d:
    if (d[i]==1):
        arr.remove(i)
print(arr)

