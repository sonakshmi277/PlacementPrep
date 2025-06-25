from collections import defaultdict
s="aabcbaa"
ct=0
for i in range(len(s)):
            for j in range(i,len(s)):
                print(s[i:j+1])
                d=defaultdict(int)
                for k in s[i:j+1]:
                    d[k]+=1
                d=dict(sorted(d.items(),key=lambda item:item[0]))
                ct+=max(d.values())-min(d.values())
print(ct)