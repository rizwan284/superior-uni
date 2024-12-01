#Sort text (word) in Alphabetical Order (without using sort function)

class A:
    def __init__(self, inputstr):
        self.stack = []
        self.inputstr = inputstr
       
    
    def convert(self):
        print(f"Orignal Text: {self.inputstr}")
        word = self.inputstr.split()
        self.stack = word
        
       
    def sort(self):
        n = len(self.stack)
        for i in range(n):
            for j in range(0, n-i-1):
                if self.stack[j].lower() > self.stack[j+1].lower():
                    self.stack[j], self.stack[j+1] = self.stack[j+1], self.stack[j]
        print(f"Ordered String is: {' '.join(self.stack)}")


usage = input("Write What you want: ")
obj = A(usage)
obj.convert()
obj.sort()