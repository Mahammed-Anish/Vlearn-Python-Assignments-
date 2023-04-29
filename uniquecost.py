name = input("Enter a string : ")
lst = []
for i in range(len(name)):
    if name[i] not in lst:
        lst.append(name[i])
for i in lst:
    if (i == lst[-1]):
        print(i,end="\n")
    else:
        print(i,end=",")
print("Number of unique characters in a string are : ",len(lst))