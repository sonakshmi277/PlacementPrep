num=14
f=num
final_ans=[]
while(f!=0):
    m=f%10
    d={}
    l=[1,2,4]
    ans=[0,0,0]
    for i in range(3):
        if((m-l[i]) not in d):
            d[l[i]]=i
        if(l[i]==m):
            ans[i]=1
            break
        elif ( (m-l[i]) in d):
            ct1=i
            ct2=d[m-l[i]]
            ans[ct1]=1
            ans[ct2]=1
            break
    f=f//10
    final_ans.append(ans[::-1])
    ans=[0,0,0]
f_a=[]
final_ans=final_ans[::-1]
for i in range(len(final_ans)):
    for j in range(len(final_ans[0])):
        f_a.append(final_ans[i][j])
for i in f_a:
    print(i,end="")