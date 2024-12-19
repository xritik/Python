# The TASK is:- 

# >  Take input from user in string form only and calucate the length of string.
# >  IF length is greater than 7 then display only those character which are present in  even index number.
# >  if length is less than or equals to 7 then display only those character which are present in odd index number.
# >  file name must be delvexstrindex.py in which you are writing code.
# >  commit this code on your github link under pythonbasic branch.  


# ***********************************************************************************************************


myString = input("Enter a word:- ")
print(len(myString))

if len(myString) > 7:
    print(myString[1::2])
else:
    print(myString[0::2])