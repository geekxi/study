# 内存分配

# 1. 假设有多组集合 A B C { name, memory },每组集合的memory元素的和小于等于一个常数M(100)
# 2. 新增加一个元素p name, memory 
# 3. 若p加入一个集合，集合memory小于M，则通过
#    若p加入每个集合，集合memory均大于M，则进行递归，直到有集合的memory元素小于M   

# 宿主机集合
# A = { '虚机1' : '8', '虚机2' : '8', '虚机3' : '32' }
# B = { '虚机4' : '4', '虚机5' : '8', '虚机6' : '32' }
# C = { '虚机7' : '16', '虚机8' : '32', '虚机9' : '32' }
pclist = { 
    '宿主机1' : { '虚机1' : '64', '虚机2' : '8' , '虚机3' : '32' },
    '宿主机2' : { '虚机4' : '16', '虚机5' : '24', '虚机6' : '32' },
    '宿主机3' : { '虚机7' : '16', '虚机8' : '32', '虚机9' : '32' }
 }

# 宿主机最大内存
MAX_MENMORY = 128

# 需要加入的虚机
new_vm = { '虚机10' : '64' }

# while true:
#     A.update(new_vm)
#     sum = 0
#     for eachvalue in B.values():
#         sum = sum + int(eachvalue)
#     print(sum)

def xxx():

    for eachitem in pclist.items():
        # 遍历每个子字典
        vmlist = eachitem[1]
        # 将新虚机字典插入每个子字典中
        vmlist.update(new_vm)
        # 每个子字典中求和
        sum = 0 
        for eachvalue in vmlist.values():
            sum = sum + int(eachvalue)
        # 若小于定值，则打印变更环境，若大于则进行递归
        if sum < MAX_MENMORY:
            print(new_vm.keys(), '-->', eachitem[0])
            break                 
    # 没有合适的主机，需要进行重新分配  迭代算法
    else:
        print("没有合适的主机，需要进行重新分配")

xxx()