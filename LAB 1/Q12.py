#WAP to find the sum of all items in a dictionary
def getDictionaryFromUser():
    n = int(input("Enter the number of items in the dictionary: "))
    dataDict = {}
    for _ in range(n):
        key = input("Enter key: ")
        value = int(input("Enter value (integer): "))
        dataDict[key] = value
    return dataDict

def sumOfDictionaryItems(dataDict):
    return sum(dataDict.values())

dataDict = getDictionaryFromUser()
result = sumOfDictionaryItems(dataDict)

print("The sum of all values in the dictionary is:",result)