import timeit

#'0-1-2-3-4-5-....-99'

num_string = "-".join(str(n) for n in range(100)) 
print(num_string)

time = timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)
print(time)

time = timeit.timeit('"-".join([str(n) for n in range(100)])', number=10000)
print(time)

time = timeit.timeit('"-".join(map(str,range(100)))', number=10000)
print(time)