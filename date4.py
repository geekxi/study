# 汉诺塔

def hanoi(n, x, y, z):
    if n == 1:
        print(x, '-->', z)
    else:
        # 将第n-1个盘子从x移动到y
        hanoi(n-1, x, z, y)  
        # 将第n个盘子移动到z
        print(x, '-->', z)
        # 将y上的n-1个盘子移动到z上
        hanoi(n-1, y, x, z)

hanoi(2, 'X', 'Y', 'Z')