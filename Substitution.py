
substitution = str((input("substitution key :")))

while len(substitution) != 26:
    substitution = str((input("substitution key :")))

substitution_upper = substitution.upper()

plain_text = input("plaintext: ")

for i in range(len(plain_text)):
    if plain_text[i].isalpha():
        if plain_text[i].islower():
            print((substitution_upper[ord(plain_text[i])-97]).lower(),end="")
        if plain_text[i].isupper():
            print(substitution_upper[ord(plain_text[i])-65],end="")
    else:
        print(plain_text[i],end="")



