from unicodedata import name


def main():
    name = input("What's your name? ")
    hello(name)
    
def hello(name):
    print("hello,", name)
    
main()

