# import random

# n = random.randint(1, 10)
# print(n)

# tmp = input("输入数字")
# # isinstance(int(tmp))
# isinstance(tmp, int)

# i = 0
# j = 0
# while i <= 100:
#     i = i + 1
#     j = j + i

# print(j)


for i in range(1, 10):
    print("i开始值", i)
    if i%2 == 0:
        print("是偶数", i)
        continue
    i = i + 2
    print("i的值为", i)