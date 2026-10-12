import time
# Fibbnachi sequence
# 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 2584 4181 6765 10946 17711 28657 46368 75025 121393 196418 317811
def fib(num):
    if num<=1:
        return 1
    else:
        return fib(num-1)+fib(num-2)
start=time.time()
print(fib(38))
print("Time taken: ", time.time()-start)
# Highly inefficient. In fact, an exponential increase in time complexity. Time complexity is 2^n. 
# To fix this, we'll use Memoization. We'll store the results of previous calculations in a dictionary so that we don't have to recalculate them.
# Memoization is a technique that can be used to optimize recursive algorithms by storing the results of expensive function calls and returning the cached result when the same inputs occur again.
def memo(num, dic):
    if num in dic:
        return dic[num]
    else:
        dic[num] = memo(num-1, dic) + memo(num-2, dic)
        return dic[num]
dic={0:1,1:1}
start=time.time()
print(memo(38, dic))
print("Time taken: ", time.time()-start)