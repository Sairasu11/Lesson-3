myfavfruitsnum = int(input("Enter num of fruits:"))
nameoffruits = []

for i in range(myfavfruitsnum):
    fruitsname = input("enter name of fruits:")
    nameoffruits.append(fruitsname) 

    if fruitsname == "banana":
        break
    elif fruitsname == "apple":
        print("Happy Eating")

print(nameoffruits)