# 序列分解为单独的变量
p = (4 , 5)
x, y = p

# print(x, y)
# print(p)

# 循环
s = "Some text"
c = ("S", "o", "m", "e", "t", "e", "x", "t")
print(len(c))

cnt = 0
for n in s:
    if n == "e":
        cnt = cnt + 1
print("found",cnt, "'e'")

m = 0
p = 0
while m < len(c):
    m = m + 1
    p = p + m
print(p)

