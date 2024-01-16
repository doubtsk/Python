# 系统提示
print("欢迎来到快递系统")
while 1 == 1:
    weight = int(input("请输入重量(kg)"))
    num = input("请输入地点编号(1.其他 2.东三省/宁夏/青海/海南 3.新疆/西藏 4.港澳台)")
    # 定义参数
    p = 0
    if weight > 3:
        if num == "1":
            p = 10+5*(weight-3)
        elif num == "2":
            p = 12+10*(weight-3)
        elif num == "3":
            p = 20+20*(weight-3)
        elif num == "4":
            p = 100000
            print("请联系总公司")
        else:
            print("输入错误")
    elif weight <= 3 and weight > 0:
        if num == "1":
            p = 10
        elif num == "2":
            p = 12
        elif num == "3":
            p = 20
        elif num == "4":
            p = 100000
            print("不接受寄件")
    else:
        print("输入错误")
    print("您好此件包裹的价格为", p, "元")
