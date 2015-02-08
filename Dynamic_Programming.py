import time
import sys

startTime = time.clock()

target = int(sys.argv[1])
coins = [1, 2, 5, 10, 20, 50, 100, 200]
ways = [1] + [0]*target

for coin in coins:
    for i in range(coin, target+1):
        ways[i] += ways[i-coin]


endTime = time.clock()

print endTime - startTime

