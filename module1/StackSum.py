import Stack

class StackSum(Stack.Stack):

    def __init__(self):
        super().__init__()
        self.__sum = 0

    def getSum(self):
        return self.__sum

    def push(self, element):
        super().push(element)
        self.__sum += element

    def pop(self):
        element = super().pop()
        if element != None:
            self.__sum -= element
        return element

a = StackSum()

a.push(1)
a.push(5)
a.pop()
print(a.pop())
print(a.pop)

#objsum.pop()
#objsum.push()