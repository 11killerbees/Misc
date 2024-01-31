class sorcerer:
    def __init__(self,name, hp, teq ,speed):
        self.teq = teq
        self.name = name
        self.speed = speed
        self.hp = hp

    #prints out calss
    def __str__(self):
        return str(self.name)+ str(self.hp)+ str(self.teq) +str(self.speed)

    #hp set funtion
    def hpSet(self,set):
        self.hp = set

    #get speed funtion
    def speedGet(self):
        return self.speed

    # get hp funtion
    def hpGet(self):
        return self.hp

    # get dam funtion
    def damGet(self):
        return self.dam

    # get teqs funtion
    def teqGet(self):
        return self.teq

    # get name funtion
    def nameGet(self):
        return self.name