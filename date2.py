#
# 猜数字游戏
#
import random

ran = random.randint(1, 10)
# print(ran)

while True:
    tmp = None  
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
        # else:
        #     print("猜错了，再接再厉")
        #     pass
        elif num < ran:
            print("猜小了，再接再厉")
            pass
        elif num > ran:
            print("猜大了，再接再厉")
            pass
    else:
        print("你输入的不是数字")