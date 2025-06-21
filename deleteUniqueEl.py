from collections import defaultdict
arr=[1,2,3,4,3]
curr=arr[0]
d=defaultdict()
for i in arr:
    if(i in d):
        d[i]+=1
    else:
        d[i]=1
arr=[i for i in arr if d[i]>1]
print(arr)

