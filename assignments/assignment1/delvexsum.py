# assignments are here:-       https://github.com/delvex-community/TaskTrove/tree/main/PythonTask/assignment2

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