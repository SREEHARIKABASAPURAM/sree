for x in range(65,90):
    alpha = chr(x)
    with open(str(alpha),'w')as file:
        file.write(alpha)

list_a = ["apple", "banana", "cherry"]
list_a.append("watermelon")
print(list_a[3])
