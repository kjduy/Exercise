class FileOperator:

    def askFileName(self):
        fileName = input("Enter the file name: ")
        fileName = "./model/" + fileName
        return fileName

    def separateNames(self, lists, personNumber, fileName):
        with open(fileName, "r") as fileName:
            lists = fileName.read().split('\n')
            names = lists[personNumber].split('=')
            return names

    def separateDates(self, names, personNumber, fileName):
        names = self.separateNames(names, personNumber, fileName)
        dates = names[1].split(',')
        return dates

    def countFileLines(self, fileName):
        with open(fileName) as fileName:
            return sum(1 for line in fileName)