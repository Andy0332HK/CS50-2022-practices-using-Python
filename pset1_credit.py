credit_card = str(input("credit card: "))
card_length = len(credit_card)
card_start = credit_card[0:2]
temp = 0

if card_length > 0:
    for i in range(0, card_length, 2):
        if (int(credit_card[i])*2 >= 10):
            temp_timestwo = str(int(credit_card[i])*2)
            temp_one = int(temp_timestwo[0])
            temp_two = int(temp_timestwo[1])
            temp = temp + temp_one + temp_two
        else:
            temp = temp + int(credit_card[i])*2

    for i in range(1, card_length+1, 2):
        temp = temp + int(credit_card[i])

IBM = temp

if IBM != 20:
    print("invalid")
if (card_start == "34" or card_start == "37") and card_length == 15:
    print("American Express")
if (card_start == "51" or card_start == "52" or card_start == "53" or card_start == "54" or card_start == "55") and card_length == 16:
    print("Mastercard")
if (card_start[0] == "4") and card_length == 13 or card_length == 16:
    print("Visa")







