import random

ran = random.randint(1, 10)

while True:
    tmp = None
    num = None

    tmp = input("请输入一个数字")

    try:
        num = int(tmp)
        pass
    except:
        pass

    if type(num) == int:
        print("你输入的数字是：", num)

        if num == ran:
            print("恭喜你猜对了")
            break
        else:
            print("猜错了，再接再厉")
            pass
    else:
        print("你输入的不是数字")