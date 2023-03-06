

numbers = [20, 500, 10, 5, 100, 1, 50]

target_nums = int(input("Number: "))

found = False

for i in range(len(numbers)):
    if numbers[i] == target_nums:
        print("Found\n")
        found = True
        break

if found == False:
    print("Not found")