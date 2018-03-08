import random
n = int(input("Enter desired array size: "))
a1 = [int(input("Integer " + str(i + 1) + ": ")) for i in range(n)]
a2 = list(a1)
del a2[random.randint(0, n)]
print("Original Array: " + str(a1) + "\nNew Array: " + str(a2))
print("Removed integer: " + str(list(set(a1) - set(a2))))