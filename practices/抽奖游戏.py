import random

def getmoney():
    print("恭喜获得",random.randint(0,50),"金币")

def getgift():
    i =random.randint(0,30)
    if 0<i<=10:
        print("恭喜获得一个水杯")
    if 10<i<=20:
        print("恭喜获得一个洋娃娃")
    if 20<i<=30:
        print("恭喜获得一个大洋娃娃")

def main():
    while (1):
        s= eval(input("1,金币 2,玩偶 3,退出"))
        if s ==1:
            getmoney()
        elif s==2:
            getgift()
        elif s==3:
            break
        else:
            print("输入有误,重来")

main()        