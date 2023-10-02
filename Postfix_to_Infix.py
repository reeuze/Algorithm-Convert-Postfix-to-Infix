class Convert:
    def __init__(self):
        self.Input = []
        # self.Stack = []
        self.Output = ""
    def Print(self, scan = ""):
        print("scanned : ", scan)
        print("input : ", self.Input, "\n")
    def Convert(self, input = ""):
        for char in input:
            self.Input.append(char)
    def Is_Operator(self, character):
        operators = "+-*/^"
        if character in operators:
            return True
    def Combine(self, value_1, value_2, operator):
        return value_1+operator+value_2
    def Algorithm(self, input = [], index = 0):
        for i in range(index, len(input)):
            self.Print(input[i])
            if len(input)==1:
                break
            elif input[i].isdigit():
                again = self.Algorithm(input, i+1)
                if again is True:
                    return False
            elif self.Is_Operator(input[i]) is True:
                input[i-2] = self.Combine(input.pop(i-2), input.pop(i-2), input.pop(i-2))

input = "123/456^*-7+8*+"
a = Convert()
a.Convert(input)
a.Algorithm(a.Input)