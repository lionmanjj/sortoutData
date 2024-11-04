import time

length = 15000000
a = range(length)

# 使用 for 循环
start_time = time.perf_counter()
b = [x for x in a if x % 2 == 0]
print("For 循环耗时:", time.perf_counter() - start_time)

# 使用 filter
start_time = time.perf_counter()
c = filter(lambda x: x % 2 == 0, a)
print("Filter 耗时:", time.perf_counter() - start_time)