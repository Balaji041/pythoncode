for row in range(1,7):
    for col in range(1,12):
        if row==1 or row==6 or col==1 or col==11:
            print("*",end="")
        else:
            print(end=" ")
    print()
