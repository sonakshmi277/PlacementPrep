num=394
d=num
pw=1
rem=0
ans=0
while(d!=0):
    rem=d%8
    ans+=rem*pw
    d=d//8
    pw=pw*10
print(ans)


