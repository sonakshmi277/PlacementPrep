## Sieve Eratosthenes way
## Time: O(n log logn)

import math
def primesInRange(queries):
        f_ans=[]
        for i in range (len(queries)):
            ct=0
            st=queries[i][0]
            lt=queries[i][1]
            ans=[1]*(lt+1)
            ans[0]=ans[1]=0
            for i in range(2,int(math.sqrt(lt))+1):
                if(ans[i]==1):
                    for j in range(i*i,lt+1,i):
                        ans[j]=0
            for k in range(st,lt+1):
                 if(ans[k]==1):
                      ct+=1
            f_ans.append(ct)
        return f_ans
h=primesInRange( [ [1, 7], [3, 7] ])
print(h)


