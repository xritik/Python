# The TASK is:- 

# >  two list are give below L1 , L2.
# >  create a new list called L3 containing items in below given  pattern.
# >  From L1 it must take only odd index items.
# >  From L2 it must take only even index items.
# >  file name must be delvexlist.py in which you are going to write the code.
# >  commit this code on your github link under pythonbasic branch. 


# ***********************************************************************************************************


L1 = [1, 2, 3, "apple", "banana", 7]
L2 = ["orange", 10, 11, [1, 2, 3], "boy"]

L3 = L1[::2] + L2[1::2]
print(L3)