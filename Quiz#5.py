from random import *

customers = range(1,51)
customers = list(customers)
print(customers)
available = 0
for i in customers : 
    time = randint(5,51)

    
    if 5<= time and time<=15:
        available +=1
        print("[O]{0}번째 손님 (소요시간 : {1})".format(i,time))
    else:
         print("[X]{0}번째 손님 (소요시간 : {1})".format(i,time))
print("총 탑승 승객 : {0}분 ".format(available)) 
