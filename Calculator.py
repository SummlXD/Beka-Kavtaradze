class calculator():
    def __init__(self, x, y):
        self.x= x
        self.y= y
    def mimateba(self):
        return self.x + self.y
    def gamokleba(self):
        return self.x - self.y
    def gayofa(self):
        return self.x/self.y
    def gamravleba(self):
        return self.x*self.y
ricxvebi = calculator(2,3) # რადგან არ მთხოვდა დავალება იუზერის ინფუტს პირდაპირ განვუსაზღვრე
print("Sum =",ricxvebi.mimateba(),"Subtr =",ricxvebi.gamokleba(),"Div =",ricxvebi.gayofa(),"Mult =",ricxvebi.gamravleba())



