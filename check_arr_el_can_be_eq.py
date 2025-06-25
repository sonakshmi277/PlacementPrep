#Function to check whether an array is equal or not
def check(array,length):
     for i in range(0, length):
     
          # Divide number by 2
            while array[i] % 2 == 0:
                array[i] //= 2

          # Divide number by 3
            while array[i] % 3 == 0:
                array[i] //= 3

     if array[i] != array[0]:
         return False
     print(array)
     return True

#input array from user
array = [50, 100, 75]

#determine length of array and assign to length variable
length=len(array)
d=check(array,length)
print(d)