for i in range(3):
        s=l[i]
        if((m-s) not in d):
            d[s]=i
        if(s==m):
            ans[i]=1
            break
        elif ( (m-s) in d):
            ct1=i
            ct2=d[m-s]
            ans[ct1]=1
            ans[ct2]=1
            break