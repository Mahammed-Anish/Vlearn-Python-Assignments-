print("The books that are available with us are : ")
print("1.Introduction to python programming\n2.Python libraries cookbook\n3.Data Science in Python\n")
print("The cost of each Introduction to Python Programming Book is : Rs.499")
print("The cost of each Python Libraries Cookbook Book is : Rs.855")
print("The cost of each Data Science in Python Book is : Rs.645")
Tcost = 0
while(True):
    print("\n")
    choice = int(input("Enter the book number that you want to purchase in the below list : "))
    if(choice!=1 and choice!=2 and choice!=3):
        print("Sorry! The book you want to purchase is not available")
    else:
        count = int(input("Enter the number of books that you want to purchase : "))
        if(choice == 1):
            Tcost += (499 * count)
        elif(choice == 2):
            Tcost += (855 * count)
        else:
            Tcost += (645 * count)
    print("Do you want to purchase some more books : ")
    if(eval(input("yes-1/no-0 : "))):
        continue
    else:
        break
Tcost += (Tcost * 0.12)+250
print("\n\nDelivary Charges = Rs.250")
print("GST = 12%")
print("Total Cost Of Books including all Taxes and Additional Charges is : Rs.",end="")
print(Tcost)