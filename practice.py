from random import *

# 편의상 댓글은 20명이 작성하였고 아이디는 1~20 이라고 가정
# 댓글과 내용 모드 상관없이 무작위로 추첨하되 중복 불가
# random 모듈의 shuffle과 sample을 활용


def openAccount():
    print("new account is made.")
openAccount()
def deposit(balance,money):
    print("Deposit completed")
    print("money on account : {0}".format(balance+money))
    return balance + money
def withdraw(balance,money):
    if money > balance:
        print("not enough balance")
        return
    else : 
        print("you withdraw {0} from your account ".format(money))
        print("Left balance {0}".format(balance - money))
        return balance - money

def withdrawNight(balance , money):
    commission = 1

    if money > (balance+commission):
        print("not enough balance")
        return balance
    else : 
        print("you withdraw {0} from your account ".format(money))
        print("Left balance {0}".format(balance - money-commission))
        return commission , balance - money - commission

    
    



balance = 0
balance = deposit(balance,200)

balance = deposit(balance,300)

balance = withdraw(balance,300)

commission, balance = withdrawNight(balance,100)# 이렇게 두개의 값을 리턴받고 두개를 한번에 다른 값에 저장시켜줄수가 있음

