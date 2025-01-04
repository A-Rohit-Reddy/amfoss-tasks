def countWays(x, n, num):
    power_num = num ** n
    if x == 0:
        return 1
    if x < 0 or power_num > x:
        return 0
    return countWays(x - power_num, n, num + 1) + countWays(x, n, num + 1)

x = int(input())
n = int(input())
print(countWays(x, n, 1))
