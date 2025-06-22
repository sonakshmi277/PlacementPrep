s="abcgha"
ct=0
for i in range(len(s)):
    st=""
    for j in range(i,len(s)):
                st+=s[j]
                if("a" in st and "b" in st and "c" in st):
                    ct+=1
print(ct)