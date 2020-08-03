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


# for i in range(1, 10):
#     print("i开始值", i)
#     if i%2 == 0:
#         print("是偶数", i)
#         continue
#     i = i + 2
#     print("i的值为", i)

# import pymysql

# db = pymysql.connect('192.168.8.74', 'root','root', 'pystudy')

# cursor = db.cursor(
# tuplex = ('宿主机1', {'虚机1': '8', '虚机2': '8', '虚机3': '32'})
# m = (('2' , '3'), ('4', '5'))
# n = ('2' , '3')

# dict1 = dict(n)
# print(dict1)

# vmlist = {'虚机7': '16', '虚机8': '32', '虚机9': '32'}
# new_vm = {'虚机10' : '16'}


# for i in vmlist.keys():
#     pass
# print (i)

# i() in vmlist.keys()

# new_vm = { '虚机10' : '32' }
# i = new_vm.keys()

# print(str(i))

# i = {1:'1',2:'2',3:'3'}
# j = i.pop(1)
# print(j)
# print(i)


# 循环完成输出一次
i = (1,2,3,4,5)

for j in i:
    if j > 5:
        print(j)
else:
    print("i中没有大于5的数")