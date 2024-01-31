
# a noun is a person place ot thing that is used to demonstart magic ie fire works on a person but not a rock
class noun:
    # a state means if the item is 1: a animal , 2: a plant 3: a nonliving object
    def __init__(self, name, state):
        self.state = state
        self.name = name

    def __str__(self):
        return  self.state , self.name

    def getState(self):
        return self.state

    # this would make it alive ig?
    def setState(self,newState):
        self.state = newState

    def getName(self):
        return self.name
