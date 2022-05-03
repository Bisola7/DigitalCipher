import art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print(art.logo)
print("Welcome to Bisola's Cypher")


def My_cypher(m, s, d):
    message = ""
    for i in m:
        if i in alphabet:
            # print(alphabet.index(i))
            p = (alphabet.index(i)) + s
            if d == "decode":
                p = (alphabet.index(i)) - s
            message += alphabet[p]
        else:
            message += i
    print(f"{d}d text: {message}")


again = True
while again:
    direction = input('Please enter "encrypt" to encrypt your message or "decode" to decode your message\n').lower()
    shift = int(input("Please enter the number of shift\n"))
    shift = shift % 26
    text = input("Please type your message\n").lower()
    My_cypher(d=direction, s=shift, m=text)
    ra = input("Do you wanna run the cypher again? yes or no\n").lower()
    if ra == "no":
        again = False
        print("Thank you for using Bisola's Cypher")


# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
