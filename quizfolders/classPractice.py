class Unit :
    def __init__(self,name,hp,speed):
        self.name = name
        self.hp = hp
        self.speed = speed
        print("{0} 유닛이 생성 되었습니다.".format(self.name))
    
    def move(self, location):
        print("{0} 는 {1}방항으로 움직입니다 [속도{2}] ".format(self.name,location,self.speed))
    
class attackUnit(Unit):
    def __init__(self,name,hp,speed,damage):
        Unit.__init__(self,name,hp,speed)
        self.damage = damage
        
    def attack(self,location):
        print("{0}: {1}방향으로 공격 [공격력: {2}]".format(self.name,location,self.damage))
class Marine(attackUnit):
    def __init__(self,name,hp,speed,damage):
        attackUnit.__init__(self,name,hp,speed,damage)
        self.stimpack = False
    def steampack(self):
        if self.stimpack == False :
            self.stimpack = True
            self.damage = self.damage*2
        else:
            self.stimpack = False
            self.damage = self.damage/2
        print("현재 공격력[{0}]".format(self.damage))



m1 = Marine("marine",20,3,4)
m1.move("1시")
m1.attack("1시")
m1.steampack()
m1.attack("2시")


