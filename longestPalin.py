s="malayalam"
ans=s[0]
def find(i1,i2):
    while(i1>=0 and i2<len(s) and s[i1]==s[i2]):
        i1-=1
        i2+=1
    a=s[i1+1:i2]
    return a
for i in range(len(s)-1):
    odd=find(i,i)
    even=find(i,i+1)
    if(len(odd)>len(ans)):
        ans=odd
    if(len(even)>len(ans)):
        ans=even
print(ans)
