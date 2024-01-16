import random

def age():
    age = random.randint(0, 99)
    print("系统已经想好了一个年龄,你来猜")
    while True:
        guess = input("请输入年龄")
        if guess.isalpha():
            print("输入错误，重来!")
            continue
        # elif not guess.isdigit():
        #     print("请输入一个数字")
        else:
            guess = int(guess)
            if guess<0:
                print("这。。。。这不对吧?")
                continue
            if guess < age:
                print("小了")
            elif guess > age:
                print("大了")
            else:
                print("恭喜", age)
                break
    print("游戏结束,感谢参与")


while True:
    age()
    play_again = input("还想继续玩吗？(不想玩请输入-1)")
    if play_again == "-1":
        break
