import nounMod
# if the message doesnt use a noun then put 0 for noun and string2 as ""
class message:
    def __init__(self, string1,name,string2):
        if name !=0:
            self.name = name
        self.string1 = string1
        self.string2 = string2


    def __str__(self):
        return self.string1 +" "+ self.name +" "+ self.string2

    def setName(self, newName):
        self.name = newName

