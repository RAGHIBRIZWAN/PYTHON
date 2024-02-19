import random
while True:
    compnumber = random.randrange(1,101)
    userinput = int(input("ENTER YOUR NUMBER:"))

    if userinput > compnumber:
        print("COMPUTER NUMBER",compnumber)
        print("YOUR GUESS NUMBER IS HIGH")
    elif userinput < compnumber:
        print("COMPUTER NUMBER",compnumber)
        print("YOUR GUESS NUMBER IS LOW")
    else:
        print("COMPUTER NUMBER",compnumber)
        print("YOUR GUESS NUMBER IS EQUAL")
