import sys

print("Hello World!!")

argLen = len(sys.argv)
i = 0
while (i < argLen):
    print("Argument [" + str(i) + "] : " + sys.argv[i])
    i+=1
