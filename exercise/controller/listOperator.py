class ListOperator:
    
    def countTimesMatchOffice(self, dates, dateFirstPerson, dateSecondPerson):
        result = 0
        for i in dates[dateFirstPerson]:
            for j in dates[dateSecondPerson]:
                if((i[0:2]==j[0:2]) 
                and ((int(i[2:4])==int(j[2:4]) 
                and int(i[8:10])==int(j[8:10])) 
                or (int(i[2:4])>=int(j[2:4]) 
                and int(i[8:10])<=int(j[8:10])))):
                    result += 1
                    break
        return result

    def createListOnlyNames(self, fileLines, names):
        listName = []
        for i in range(fileLines):
            for j in range(fileLines):
                listName.append(names[i][j])
                break
        return listName