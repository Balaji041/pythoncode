n=int(input("enter a number:\n"))

for i in range(n):
    A=ord("A")+i
    for j in range(i+1):
        print (chr(A),end=" ")
        A+=1
    print ()
    """ 
enter a number:
8
A 
B C 
C D E 
D E F G 
E F G H I 
F G H I J K 
G H I J K L M 
H I J K L M N O 
    
    """
