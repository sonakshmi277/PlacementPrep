class Solution:
    def myAtoi(self, s):
        sign=1
        num=0
        INT_MAX=(2**31)-1
        INT_MIN=-2**31
        i=0
        l=len(s)
        while (i<l and s[i]==" "):
                i+=1
        if (i<l and (s[i] in ("-","+"))):
                sign=-1 if s[i]=="-" else 1
                i+=1
        while(i<l and ord(s[i])>=ord("0") and ord(s[i])<=ord("9")):
                num=num*10+int(s[i])
                i+=1
        num*=sign
        return min((max(num,INT_MIN)),INT_MAX)
