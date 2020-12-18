class House:
    def __init__(self,location, house_type,deal_type,price,completion_year):
        self.location = location
        self.house_type = house_type
        self.deal_type = deal_type
        self.price = price
        self.completion_year = completion_year
    
    def show_detail(self):
        print("{0} {1} {2} {3} {4}".format(self.location, self.house_type,self.deal_type,self.price,self.completion_year))

class apt(House):
    def __init__(self,location, house_type,deal_type,price,completion_year):
        House.__init__(self,location,house_type,deal_type,price,completion_year)




hous = []

hous1 = apt("강남","아파트","매매","10억","2010년")
hous2 = apt("마포","오피스텔","전세","5억","2007년")
hous3 = apt("송파","빌라","월세","500/50","2000년")

hous.append(hous1)
hous.append(hous2)
hous.append(hous3)


for house in hous : 
    house.show_detail()