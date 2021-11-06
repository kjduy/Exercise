class Result:

    def printResult(self, combination, listName, coincidedTimes):
        for i in range(combination):
            print(listName[i] + "-" + listName[i-1] + ":" , coincidedTimes[i])