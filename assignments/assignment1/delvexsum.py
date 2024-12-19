a = input("Enter your 5 numbers:- ").split(',')
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