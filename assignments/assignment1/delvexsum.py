# assignments are here:-       https://github.com/delvex-community/TaskTrove/tree/main/PythonTask/assignment2


# The TASK is:-

# > Take 5 integrer input from user.
# > Remove all numbers less than 9.
# > calculate the sum of remaining numbers.
# > file name must be delvexsum.py in which you are writing code.
# > commit this code on your github link under pythonbasic branch. 



# ***********************************************************************************************************

a = input("Enter your 5 numbers like(1,2,3,4,5):- ").split(',')
# print(a)
# print(len(a))
# print(type(a))
x = []
for c in a:
    d = int(c)
    if d > 9:
        x.append(d)
        # print(x)
result = int()
if len(x) > 0:
    for y in x:
        result += y
print(result)