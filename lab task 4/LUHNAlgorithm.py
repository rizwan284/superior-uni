class Mastercard:
    def __init__(self):
        self.visaCard = [4,6,4,9,5,2,4,8,0,1,0,3,7,4,7,2]
        self.lastNumber = ''
#Remove the Last Digit
    def Lastnumberpop(self):
        self.lastNumber= self.visaCard.pop()
#Reverse the remaining digits
    def Reversethenumbers(self):
        reverselist = []
        for i in self.visaCard[15::-1]:
            reverselist.append(i)
        self.visaCard = reverselist
        
#Double digits at even indices
    def DoubleEvenNumber(self):
        emptylist = []
        for i in range(len(self.visaCard)):
            if i % 2 == 0:
                a = self.visaCard[i]
                b = a *2
                emptylist.append(b)
            else:
                a = self.visaCard[i]
                emptylist.append(a)
        self.visaCard = emptylist
#Subtract 9 if over 9
    def substract9 (self):
        for i in self.visaCard:
            if i > 9:
                a = i -9
                self.visaCard.remove(i)
                self.visaCard.append(a)
        self.visaCard.append(self.lastNumber)
#Sum the digits and add the checking digit
    def Addallthenumbers(self):
        a = 0
        for i in self.visaCard:
            a += i
        if a % 10 == 0:
            print("Valid MasterCard")
        else:
            print("Not Valid MasterCard")


obj = Mastercard()
obj.Lastnumberpop()
obj.Reversethenumbers()
obj.DoubleEvenNumber()
obj.substract9()
obj.Addallthenumbers()