# taking convert function to convert text into emojis.
def convert(h):
    h = h.replace(":)", "🙂")
    h = h.replace(":(", "🙁")
    return h


def main():
    text = input("hello hassnain, ")
    print(convert(text))


# now writing main to run my program...
main()
