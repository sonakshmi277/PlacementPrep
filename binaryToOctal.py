s=10011011
count_digit=0
d=s
final=[0]*32
pos=0
ct=0
while(d!=0):
    m=d%10
    ct+=m*(2**count_digit)
    count_digit+=1
    d=d//10
    final[pos]=ct
    if(count_digit%3==0):
        count_digit=0
        ct=0
        pos+=1
   
    
f=final[::-1]
for i in f:
    if(i!=0):
        print(i,end="")
