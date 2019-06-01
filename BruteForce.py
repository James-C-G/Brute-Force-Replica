import random
import sys
import time

def Brute(Target):
    targetArray = list(Target)
    stringArray = [""] * len(targetArray)
    i = 0
    while i < len(targetArray):
        if stringArray[i] != targetArray[i]:
            stringArray[i] = chr(random.randint(32, 126))
        
        if stringArray[i] == targetArray[i]:
            i += 1
        x = 0
        print("\n")
        while x <len(stringArray):
            print(stringArray[x], end = "")
            x += 1

    print("\nDone!")

def Load():
    print("Loading BruteFore.py : [",end="")
    for x in range(0,10):
        ranNum = random.uniform(0.5,2)
        time.sleep(ranNum)
        print("X",end="")
    print("] Done!")
        
Load()
Target = input("Input a something ")
Brute(Target)
