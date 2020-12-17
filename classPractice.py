class Unit :
    def __init__(self, name , hp):
        self.name = name
        self.hp = hp
        
        print("{0} has been produced. Hp is {1}".format(self.name,self.hp))

class attackUnit (Unit):
    def __init__(self,name,hp,damage):
        Unit.__init__(self,name,hp)# 위로가서 Unit 클래스 init 함수실행후 결과를 여기로 가져와서 다 있다. 
        self.damage = damage
        print("{0} hp : {1}, damage: {2}".format(self.name,self.hp,self.damage))

# marine = attackUnit("marine",20,3)   
# marine2 = attackUnit("marine",20,3)
# marine2.Steampack = True
# if marine2.Steampack == True:
#     print("{0}`s steam pack is on".format(marine2.name))

class flyableUnit :
    def __init__(self, flyingspeed):
        self.flyingspeed = flyingspeed
    def fly(self,location):
        print("locatoin : {0}, speed {1}".format(location,self.flyingspeed))

# wraith = flyableUnit(20)
# wraith.fly("1 시")

class flyAttackUnit(attackUnit,flyableUnit) :
    def __init__(self,name,hp,damage,flyingspeed):
        attackUnit.__init__(self,name,hp,damage)
        flyableUnit.__init__(self,flyingspeed)

wraith = flyAttackUnit("wraith",30,8,20)
wraith.fly("1시")
