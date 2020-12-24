

class SoldOutError(Exception):
    
    def __init__(self,msg):
        self.msg = msg
    def __msg__(self):
        return self.msg



chicken = 10
waitinglist = []
people = 0

while True:
    
    try:
        order = int(input("how many chickens do you want? :"))

        if chicken <= 0 :
            print("no more chicken left ")
            break
        elif chicken < order :
            raise SoldOutError("we do not have enough chicken\n we have {0} many chickens left".format(chicken))
            
        
        else :
            waitinglist.append(people)
            print("waiting list {0} ordered {1} many chickens".format(people, order))
            people += 1
            chicken -= order
            print(chicken)
    
    except ValueError:
        print(" you did not put invale value, not number")

    except SoldOutError as err:
        print("Error has occurred")
        print(err)
    finally:
        print("thank you for ordering")