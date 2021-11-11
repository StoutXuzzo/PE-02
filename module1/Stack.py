class Stack():

    def __init__(self):
        self.stack = []
    
    #def __init__(self, data):
    #    stack = data[:]

    def push(self, element):
        self.stack.append(element)

    def pop(self):
        if len(self.stack) > 0:
            return self.stack.pop()
        else:
            return None

# To create this clas: varName = Stack() or varName = Stack(listToAdd).

# By default all the variables and methods are public, to change it to pribate we have to put "__"
#   in the begining of his name.