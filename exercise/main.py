from controller import fileOperator, mathematicalOperation, listOperator
from view import result

fileOperator = fileOperator.FileOperator()
mathematicalOperation = mathematicalOperation.MathematicalOperation()
listOperator = listOperator.ListOperator()
result = result.Result()

dates, names, coincidedTimes, listName = [], [], [], []

fileName = fileOperator.askFileName()
fileLines = fileOperator.countFileLines(fileName)
combination = mathematicalOperation.getCombination(fileLines, 2)

for i in range(fileLines):
    names.append(fileOperator.separateNames(names,i,fileName))

for i in range(fileLines):
    dates.append(fileOperator.separateDates(dates,i,fileName))

listName = listOperator.createListOnlyNames(fileLines, names)

for i in range(combination):
    coincidedTimes.append(listOperator.countTimesMatchOffice(dates, i, i-1))

result.printResult(combination, listName, coincidedTimes)