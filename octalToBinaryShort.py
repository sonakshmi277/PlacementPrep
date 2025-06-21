def octal(num):
    i=0
    s=0
    d=num
    while(d!=0):
        m=d%10
        s+=m*(8**i)
        i+=1
        d=d//10
    print("Decimal",s)
    ans=0
    pw=1
    rem=0
    while(s!=0):
        rem=s%2
        s=s//2
        ans+=pw*rem
        pw=pw*10
    print(ans)


octal(12)