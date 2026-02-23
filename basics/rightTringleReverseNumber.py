height = int(input("Enter height of pattern : "))

for i in range(1,height+1):
    for j in range(i,0,-1):
        print(j, end = " ")

    print()
