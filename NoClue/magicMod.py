import messageMod as mM
import NoClue.nounMod
ms1 = mM.message("", name, "has turned inside out " )
ms2 = mM.message( "The",name, "grew an arm" )
ms3 = mM.message('the', name, "screams and then dies, you feel bad" )
ms4 = mM.message(  "the",name ,"smells like chiken")
ms5 = mM.message("The VOID inside",name , "grows louder" )
ms6 = mM.message( "",name, "grows weak" )
ms7 = mM.message('The', name, "becomes 2 rocks , the same total mass just 2 of the same voulme, you call this new meaterl Bruhium" )
ms8 = mM.message(  "Nothing happend to the",name ,"")

ms9 = mM.message("The", name, "was burnt so bad theres not even ash" )
ms10 = mM.message( "The",name, "was redused to ash" )
ms11 = mM.message('the', name, "mealts into lava" )
ms12 = mM.message(  "the",name ,"Get red hot ")
ms13 = mM.message("The",name , "is cooked thoroughly" )
ms14 = mM.message( "The",name, " is warm but alive " )
ms15 = mM.message('The', name, "is burnt on the outside" )
ms16 = mM.message(  "The",name ,"is warm,")
mSet2 = ["none",ms9,ms10,ms11,ms12,ms13,ms14,ms15,ms16]
mSet1 = ["none",ms1,ms2,ms3,ms4,ms5,ms6,ms7,ms8]

class magic:

    #mSet is a list of message objs to be said by this class, this is so that the if stament can be inharitaed but not the message
    def __init__(self, power,time):
        self.power = power # the stramgth of the spell , crit num is 50
        self.time = time # how long its "cast" , crit num is 5
        self.mSet = mSet1 # a list of things that can be said by a class

    #prints out calss
    def __str__(self):
        return  self.power

    def getPower(self):
        return self.power

    def setPower(self,newPower):
            self.power = newPower

    def setTime(self,newTime):
            self.time = newTime

    # incress power by 10% (needed for inharitance )
    def meditate(self):
        self.power = self.power * 1.1

    # this "uses" base magic on a Noun obj and has a luck and cost stat to detremin effect
    def use(self,noun): # this takes the class mSet and makes 4 outcomes with it
        for i in range(1, len(self.mSet)):
            self.mSet[i].setName(noun.getName())


        if self.power >= 50: # over 50
            if noun.getState() == 1 or 2 : #liveing thing
                if self.time >= 5:  # cast time
                    print(self.mSet[1]) # power over 50 , liveing thing time over 5
                else:
                    print(self.mSet[2]) # power over 50 , liveing thing time under 5

            else:
                if self.time >= 5:  # power over 50 , Nonliveing thing time over 5
                    print(self.mSet[3])
                else:
                    print(self.mSet[4]) # power over 50 , Nonliveing thing time under 5

        else:#numder 50
            if noun.getState() == 1 or 2:
                if self.time >= 5:
                    print(self.mSet[5]) # power under 50 , liveing thing time over 5
                else:
                    print(self.mSet[6]) # power under 50 , liveing thing time under 5
            else:
                if self.time >= 5:
                    print(self.mSet[7]) # power under 50 , Nonliveing thing time over 5
                else:
                    print(self.mSet[8]) # power under 50 , Nonliveing thing time under 5