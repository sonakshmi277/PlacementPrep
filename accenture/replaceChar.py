#Problem Statement

#You are given a function,

#Void *ReplaceCharacter(Char str[], int n, char ch1, char ch2);

#The function accepts a string ‘str’ of length n and two characters ‘ch1’ and ‘ch2’ as its 
#arguments. Implement the function to modify and return the string 'str' in such a way that all 
#occurrences of ‘ch1’ in original string are replaced by ‘ch2’ and all occurrences of ‘ch2’  in 
#original string are replaced by ‘ch1’.

#Assumption: String Contains only lower-case alphabetical letters.

#Return null if string is null.
#If both characters are not present in string or both of them are same , then return the string 
#unchanged.

#Example:

#Input:

#Str: apples
#ch1: a
#ch2: p

#Output:

#paales

#Explanation:

#‘A’ in original string is replaced with ‘p’ and ‘p’ in original string is replaced with ‘a’, 
#thus output is paales.
 
def ReplaceCharacter(st,n, ch1, ch2):
    if st is None:
        return None
    if (ch1 not in st and ch2 not in st) or (ch1==ch2):
        return st
    l=[i for i in st]
    for i in range(len(l)):
        if(l[i]==ch1):
            l[i]=ch2
        elif l[i]==ch2:
            l[i]=ch1
    return "".join(l)
ans=ReplaceCharacter("apples",6,"a","p")
print(ans)    
