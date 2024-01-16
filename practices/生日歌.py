def happysing(name):
    print("happy brithday to", name, "!")


def happy():
    name = input("告诉我你的名字")
    for i in range(3):
        happysing(name)

happy()