'''
Manipulating lists
'''

def isPrime(n):
    prime = True
    n1=2
    while n1<=(n/2) :
        if n%n1 == 0:
            prime=False
            break
        n1=n1+1
    return prime

def getPrimeNumbers(list):
    list1 = []
    for element in list:
        if isPrime(element):
            list1.append(element)
    return list1

def mergeSort(list):
    if(len(list) <= 1):
        return list
    else:
        return merge(mergeSort(list[0:len(list)//2]),
                 mergeSort(list[len(list)//2 + 1:len(list) - 1]))

def merge(list1, list2):
    mergedList=[];i=0;j=0
    while i<len(list1) and j<len(list2):
        if list1[i]<=list2[j]:
            mergedList.append(list1[i])
            i=i+1
        else:
            mergedList.append(list2[j])
            j=j+1
    while i<len(list1):
        mergedList.append(list1[i])
        i=i+1
    while j<len(list2):
        mergedList.append(list2[j])
        j=j+1
    return mergedList

list=[8, 17, 96, 67, 83, 5, 11, 49, 79]
x=0

primeNumbers = getPrimeNumbers(list)
print("Prime Numbers: ", end=" ")
for prime in primeNumbers:
    print(prime, end=" ")
print("")

sortedList=mergeSort(list)
print("Sorted Numbers: ", end=" ")
for element in sortedList:
    print(element, end=" ")