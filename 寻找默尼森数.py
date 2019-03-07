# 经典程序设计问题：找第n个默尼森数。P是素数且M也是素数，并且满足等式M=2**P-1，则称M为默尼森数。
# 例如，P=5，M=2**P-1=31，5和31都是素数，因此31是默尼森数。
# 提交方式直接将答案（M的值）写在txt文件中通过网络提交。

def isprime(n):
    if n <= 1:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False
        if i * i > n:
            return True



u = int(input("第n个默尼森数"))
flag=0

for j in range(2,10000):
  if flag < u:
     if isprime(j):
         l = 2 ** j - 1
         if isprime(l):
            flag+= 1
            print('No.',flag,j, '的默尼森数是', 2**j-1)


