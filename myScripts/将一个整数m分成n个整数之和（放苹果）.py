# 放苹果 & 整数分解为m个数之和

# 把M个同样的苹果放在N个同样的盘子里，允许有的盘子空着不放，问共有多少种不同的分法？
# （用K表示）5，1，1和1，5，1 是同一种分法。

# 样例
#
# 输入：7, 3
#
# 输出：8

# 1
# 7 3
# 8
# 3
# 2 5
# 2
# 5 2
# 3
# 8 5
# 18

# 思路：
#
# 设i个苹果，k个盘子
# 若k>i，一定有盘子为空，则发f(i,k)=f(i,i)，
# 若k<=i，则有两种情况，
# 1：有盘子为空
# 2：都放有苹果
# 总方法数=情况一+情况二 ( 当没有空盘子时也就是说每个盘子中至少有一个苹果，
# 先把所有盘子填满，这时候会剩下 m - n 个苹果，所以现在问题变成了 m - n 个苹果放在 n 个盘子有多少种方法，
# 即 f ( i-k , k )。)
# 总：f(i,k)=f(i,k-1)+f(i-k,k)


def f(n, m):
    if n == 0 or m == 1:
        return 1
    if n < m:
        return f(n, n)
    else:
        return f(n, m - 1) + f(n - m, m)

# 典型的用动态递归解法，其实这根将一个整数m分成n个整数之和是类似的。
# 设f[m][n]为将m分成最多n份的方案数，且其中的方案不重复，即每个方案前一个份的值一定不会比后面的大。
# 则有：f[m][n] = f[m][n - 1] + f[m - n][n]，其中f[m][1]=1、f[0][n]=1.其中的含义是：
# 分的方案包含两种，一是方案中不含有空的情况，则从每个盘子里面拿出一个来也不影响最终的结果，
# 即f[m][n] = f[m - n][n]，二是方案中含有的空的情况，至于含有几个空暂时不考虑，
# 只用考虑一个空的就行，即f[m][n] = f[m][n - 1]，在这种递归调用中会重复调用含有空的情况，
# 也就是最终包含了各种可能为空的情况。

# f(n, m) =
# 1. 1. n=1, m=1
# 2. f(n,n). n < m
# 3. 1+f(n,n-1). n=m
# 4. f(n, m-1)+f(n-m, m). n >m>1

# Description
#
# 把M个同样的苹果放在N个同样的盘子里，允许有的盘子空着不放，问共有多少种不同的分法？（用K表示）5，1，1和1，5，1 是同一种分法。
# Input
#
# 第一行是测试数据的数目t（0 <= t <= 20）。以下每行均包含二个整数M和N，以空格分开。1<=M，N<=10。
# Output
#
# 对输入的每组数据M和N，用一行输出相应的K。
# Sample Input
#
# 1
# 7 3
# Sample Output
#
# 8


N = 7
M = 3
print(f(N, M))
