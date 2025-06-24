s="badam"
ans=s[0]
def expan(i1,i2):
    while(i1>=0 and i2<len(s) and s[i1]==s[i2]):
        i1-=1
        i2+=1
    return s[i1+1:i2]
for i in range(len(s)-1):
    odd=expan(i,i)
    even=expan(i,i+1)
    if(len(odd)>len(ans)):
        ans=odd
    if(len(even)>len(ans)):
        ans=even
print(ans)


