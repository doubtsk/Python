import random
num = 1
win_num = 0
lose_num = 0
while num <= 3:
    if lose_num == 2 or win_num == 2:
        break
    user = int(input('请出石头(0),剪刀(1),布(2)'))
    if user > 2:
        print('不能出大于2的值哦')
    else:
        data = ['石头', '剪刀', '布']
        com = random.randint(0, 2)
        print("您出的是{},电脑出的是{}".format(data[user], data[com]))
        if user == com:
            print("平局")
            continue
        elif (user == 0 and com == 1) or (user == 1 and com == 2) or (user == 2 and com == 0):
            print("你赢了")
            win_num += 1
        else:
            print("你输了")
            lose_num += 1
    num = + 1
