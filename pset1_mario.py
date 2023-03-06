
height = int(input("height: "))
temp_height = height
while height > 0 :
    for i in range(height):
        print(" ",end="")
    for t in range(temp_height-(height-1)):
        print("#",end="")
    print(" ", end="")
    print(" ", end="")
    for t in range(temp_height-(height-1)):
        print("#",end="")
    print()

    height = height - 1
