import sys

exitKeywords = ["q", "exit", "exit()", "quit", "quit()"]

for line in sys.stdin:
    if line.rstrip() in exitKeywords:
        break
    if line.rstrip().isdigit():
        binary = bin(int(line))
        print(binary[2:])
    else:
        print("make sure you type in an integer")
