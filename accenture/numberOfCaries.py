#A carry is a digit that is transferred to left if sum of digits exceeds 9 while adding two numbers from 
#right-to-left one digit at a time

#You are required to implement the following function, Int NumberOfCarries(int num1 , int num2);

#The functions accepts two numbers ‘num1’ and ‘num2’ as its arguments. You are required to calculate and return 
#the total number of carries generated while adding digits of two numbers ‘num1’ and ‘ num2’.

#Assumption: num1, num2>=0

#Example:

#Input

#Num 1: 451
#Num 2: 349

#Output: 2

#Explanation:

#Adding ‘num 1’ and ‘num 2’ right-to-left results in 2 carries since ( 1+9) is 10. 1 is carried and (5+4=1) is 10,
#again 1 is carried. Hence 2 is returned.

#Sample Input

#Num 1: 23

#Num 2: 563

#Sample Output: 0


num1=451
num2=349
d1=num1
d2=num2
s=0
ct=0
r=0
while(d1!=0 or d2!=0):
    rem1=d1%10
    rem2=d2%10
    s=(rem1+rem2+r)
    if s>9:
        r=1
        ct+=1
    d1=d1//10
    d2=d2//10
    s=0
print(ct)
    