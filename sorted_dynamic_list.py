list=[]
n=int(input("enter a number:"))
for i in range(n):
    values=int(input("enter a values:"))
    list.append(values)
list.sort()
print(list)
"""enter a number:5
enter a values:3
enter a values:4
enter a values:2
enter a values:5
enter a values:1
[1, 2, 3, 4, 5]"""
