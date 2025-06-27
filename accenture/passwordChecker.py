#You are given a function.
#int CheckPassword(char str[], int n);
#The function accepts string str of size n as an argument. Implement the function which returns 1 if given string str is 
#valid password else 0.
#str is a valid password if it satisfies the below conditions.

    #– At least 4 characters
    #– At least one numeric digit
   # – At Least one Capital Letter
  #  – Must not have space or slash (/)
 #   – Starting character must not be a number

#Assumption:
#Input string will not be empty.

#Example:

#Input 1: aA1_67
#Input 2: a987 abC012

#Output 1: 1
#Output 2: 0

def CheckPassword(password):
    if(len(password)<4 or password[0].isdigit()):
        return 0
    is_num=False
    is_cap=False
    for i in password:
        if(i.isupper()):
            is_cap=True
        elif(i.isdigit()):
            is_num=True
        elif(i==" " or i=="/"):
            return 0
    if(is_num and is_cap):
        return 1
    return 0
ans=CheckPassword("aA1_67")
print(ans)
        
            
        
