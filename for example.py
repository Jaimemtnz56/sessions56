sum = 0
for x in range(1, 101): #the end of range is excluded
    sum = sum + x
print(sum)


#let's print the multiplication table until 10
for i in range(1, 11):
    for j in range (1, 11):
        print(f"{i} X {j} = {i*j}")
    print() #to add an extra line between each table in sets of 10

