import time
class Convert:
    def __init__(self):
        self.Input = []
        self.Output = ""
    def Print(self, scan = ""):
        print("scanned : ", scan)
        print("input : ", self.Input, '\n')
    def Convert(self, input = ""):
        for char in input:
            self.Input.append(char)
    def Is_Operator(self, character):
        operators = "+-*/^"
        if character in operators:
            return True
    def Combine(self, value_1, value_2, operator):
        result = str('('+value_1+operator+value_2+')') 
        return result
    def Algorithm(self, input = [], index = 0):
        i = 0
        i += index
        while i < len(input):
            self.Print(input[i])
            if len(input)==1:
                break
            elif self.Is_Operator(input[i]) is True:
                input[i-2] = self.Combine(input[i-2], input[i-1], input[i])
                for j in range(0, 2):
                    input.pop(i-1)
                i -= 2
            i += 1
            time.sleep(1.5)

input = "123/456^*-7+8*+"
a = Convert()
a.Convert(input)
a.Algorithm(a.Input)
print("Result : ", ''.join(a.Input))