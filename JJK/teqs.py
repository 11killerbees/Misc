class teqs:
    def __init__(self,name,dam,sureHit,cost):
        self.name = name
        self.dam = dam
        self.sureHit = sureHit
        self.cost = cost

    #prints out calss
    def __str__(self):
        return str(self.name)+ str(self.dam)+str(self.sureHit)

    #at this moment this calss wont need to have any seters

    #gets sure hit t/f
    def getSureHit(self):
        return self.sureHit

    #get name str
    def getName(self):
        return self.name

    #get name str
    def getDam(self):
        return self.dam

    #get name str
    def getCost(self):
        return self.dam