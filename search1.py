

strings = ["Apple", "Boy", "C", "D", "E", "F", "G"]

target_strings = input("strings: ")

found = False

for i in range(len(strings)):
    if strings[i] == target_strings:
        print("Found\n")
        found = True
        break

if found == False:
    print("Not found")