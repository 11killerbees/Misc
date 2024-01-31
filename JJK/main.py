import sorcerer as s
import teqs as t
import random

#info. This is is like a bad turn based game bassed off of the anime jujutsu kaisen so if you doont know the show just think of
#the sorcerer class as a wizerd and teqs and spells, there are many type of spells and some of them hit nomater what ot hit the user etc


    #sor1 is who is attacking and sor2 is who is hit , atck is the attack.
    #this also handels acc
def Atck(sor1,sor2,atck):
    if atck.getSureHit() == True:

        sor2.hpSet(sor2.hpGet()-atck.getDam())
    else:
        acc = ((sor1.speedGet()/sor2.speedGet())-.1)*100
        check = random.randrange(0,100)

        if acc >= check:
            sor2.hpSet(sor2.hpGet() - atck.getDam())
            print(sor1.nameGet()+ "'s attack hit")
        else: return print(sor1.nameGet()+"'s attack missed")

#this handles picking an atck if teqs is a list
def pickAtck(teqs):
    for i in range(len(teqs)):
        print(teqs[i],"(",i,")")

    atck = int(input("pick a num for the teq you want: "))
    return teqs[atck]


#this starts a battle between to sors that ends when one dies
# this also handles picking a teq if a sor has more than 1
def battle(sor1,sor2):
    onGoing = True

    #gets speed to see who hits first
    if sor1.speedGet() > sor2.speedGet():
        first = sor1
        second = sor2
    else:
        first = sor2
        second = sor1

    #this is the start of a batle were one will be declaered the winner
    while onGoing:
        print()

        #this if/ else checks Hp
        if (first.hpGet()) <= 0:
            print(first.nameGet() , "is dead")
            print(second.nameGet(), "wins")
            return

        elif (second.hpGet()) <=0:
            print(second.nameGet(), "is dead")
            print(first.nameGet(), "wins")
            return

        #this makes the fater guy attck first and the the slower gut attck , this also handels what attck the user will select
        Atck(first,second,pickAtck(first.teqGet()))
        print()
        Atck(second, first, pickAtck(second.teqGet()))

        print((sor1.nameGet(),"hp is",sor1.hpGet()))
        print((sor2.nameGet(), "hp is", sor2.hpGet()))

"""
-add attack state to make rct works 
-add working exception hanedling , ie make it so that the cost works
-make file for funtions
-maybe add things into cvs file type
"""


# This is a list of premade teqs that the user can use to a sorcerer class
red = t.teqs("Red",500,False,750)
blue = t.teqs("Blue",250,False,325)
InfiniteVoid = t.teqs("Infinite Void",1000,True,2000)
devineDog = t.teqs("Devine Dogs",50,False,50)
Nue = t.teqs("Nue",30,False,20)
Mahoraga = t.teqs("Mahoraga",3000,True,5000)

#rct does not work corectly
RCTL = t.teqs("Reverse curse Technique",-25,True,50)
RCTM = t.teqs("Reverse curse Technique",-50,True,100)
RCTH = t.teqs("Reverse curse Technique",-75,True,150)
Punch = t.teqs("Punch",15,False,0)
HRPunch = t.teqs("heavenly restriction punch",100,True,0)
InvertedSpear = t.teqs("Inverted Spear",150,False,0)
Cleave = t.teqs("Cleave",150,False,0)
Dismantle = t.teqs("Dismantle",150,False,0)
MalevalentShrine = t.teqs("Malevalent Shrine",1000,True,0)
# here are some premade sorcerers for the useer to use

gojo = s.sorcerer("Gojo", 500,[red,blue,InfiniteVoid],501)
megumi = s.sorcerer("Megumi", 100,[devineDog,Nue,Mahoraga],100)
toji = s.sorcerer("Toji", 50,[InvertedSpear,HRPunch],1000)
sukuna = s.sorcerer("Sukuna", 500,[Cleave,Dismantle,MalevalentShrine],500)

# to fight call the battle(sor1,sor2): with sor1 and sor2
battle(gojo,sukuna)