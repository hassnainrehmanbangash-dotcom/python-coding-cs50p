def twttr():
    text = input("Input: ")
    print("Output:", shorten(text))


def shorten(word):
    result = ""
    for letter in word:
        if letter.lower() not in "aeiou":
            result += letter
    return result


twttr()