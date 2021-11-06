class MathematicalOperation:

    def getFactorial(self, n):
        factorial = 1
        for i in range(2, n+1):
            factorial *= i
        return factorial

    def getCombination(self, n, k):
        return self.getFactorial(n)//(self.getFactorial(n-k)*self.getFactorial(k)) 