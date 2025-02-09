def main():
    name = input("What's your Name: ")
    hello(name)


def hello(to="world"):
    print("hello,", to)

hello()
main()