class Convert:
    def __Init__(self):
        self.Input = []
        self.Stack = []
        self.Output = ""
    def Print(self, scan = ""):
        print("scanned : ", scan)
        print("Stack : ", self.Stack)
    def Convert(self, input):
        for char in input:
            self.Input.append(char)
    def Is_Operator(self, character):
        operators = "+-*/^"
        if character in operators:
            return True
    def Algorithm(self, input = [], index = 0):
        for i in range(index, len(input)):
            if len(input)==1:
                break
            elif input[i].isdigit():
                self.Algorithm(input, i+1)
                print("A")
            elif self.Is_Operator(input[i]) is True:
                print("B")

input = "123/456^*-7+8*+"
a = Convert
a.Convert(a.Input)