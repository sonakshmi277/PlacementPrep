num="89052"
def func(num):
    for i in range(len(num)-1,-1,-1):
        if(int(num[i])%2==1):
            return (num[:i+1])
    return ""
ans=func(num)
print(ans)