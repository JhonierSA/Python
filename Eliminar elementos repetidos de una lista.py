my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
resultantList = []

for element in my_list:
    if element not in resultantList:
        resultantList.append(element)
print("La lista con elementos únicos:", resultantList)
