# 学习continue
# 条件达成，不继续执行下面步骤，直接跳转到for循环体开头开始下轮循环

for i in range(1, 10):
    print("i开始值", i)
    if i%2 == 0:
        print("如果是偶数，则打印", i)
        continue
    i = i + 2
    print("i的值+2最后变为", i)