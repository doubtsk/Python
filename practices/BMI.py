height = float(input("请输入你的身高(m)"))
weight = float(input("请输入你的体重(kg)"))
BMI = weight/(height*height)
if BMI < 18.1:
    print("你的BMI指数:"+str(BMI))
    print("过轻")

if BMI >= 18.5 and BMI < 24.9:
    print("你的BMI指数:"+str(BMI))
    print("适中")

if BMI >= 24.9 and BMI < 29.9:
    print("你的BMI指数:"+str(BMI))
    print("较重")

if BMI >= 29.9:
    print("你的BMI指数:"+str(BMI))
    print("肥胖")
# 在Python中，若在变量前面添加一段文字，那么需要将变量字符串化，也就是str，再利用“+”连接起来
