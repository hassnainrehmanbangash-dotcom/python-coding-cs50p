#making plates.py
#firstly we'll make def function..
def main():
    plate = input("plate: ")
    if is_valid(plate):
        print("valid")
    else:
        print("Invalid")

def is_valid(s):
    if not (2 <= len(s) <= 6):
        return False

    if not (s[0].isalpha() and s[1].isalpha()):
        return False

    if not s.isalnum():
        return False

    for i, ch in enumerate(s):
        if ch.isdigit():
            #First number checking..
            if ch == "0":
                return False
            if not s[i:].isdigit():
                return False
            break #no scaning if first digit found...
    return True


main()

                   #<<<<>>>>#