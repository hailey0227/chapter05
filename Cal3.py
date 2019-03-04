#-*-coding:utf8

class Calc:
    def setNumber(self, first, second):
        self.first = first
        self.second = second

    def plus(self):
        return self.first + self.second

    def minus(self):
        return self.first - self.second

    def multi(self):
        return self.first * self.second

    def divide(self):
        return self.first / self.second

    # def totalCal(self, *args):
    #     if args[0] == "+":
    #         x = 0
    #         while x < 5 in args:
    #             x = x + 1
        
    #     elif args[0] == "-":
    #         x = 0
    #         while x < 4 in args:
    #             x = x + 1

    #     elif args[0] == "*":
           

    #     elif args[0] == "/":


    #     input()
