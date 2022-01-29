import sys

exitKeywords = ["q", "exit", "exit()", "quit", "quit()"]

while True:
    inputValue = input("")
    if inputValue in exitKeywords:
        break
    if inputValue.isdigit():
        binary = bin(int(inputValue))
        print(binary[2:])
    else:
        print("make sure you type in an integer")
