#first 2 characters should be alphabet
#maximum characters 6 and minimum 2
#numbers can not be in the middle of the plate, it can be at the end (always come after alphabets), first number can not be 0
#no special characters are allowed

#Start

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    digits = []
    digit_idxs = []
    alpha_idxs = []
    
    for char in s:
        if char.isalpha():
            alpha_idxs.append(s.index(char))
        elif char.isdigit():
            digits.append(char)
            digit_idxs.append(s.index(char))

    if s[0:2].isalpha():
        if len(s) <= 6:
            if s.isalnum():
                if digits:
                        return digit_idxs[0] > alpha_idxs[-1] and digits[0] != '0'
                else:
                    return True
            else:
                return False
        else:
            return False
    else:
        return False

main()


