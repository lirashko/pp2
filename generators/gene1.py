def square_generator(n):
    for i in range(1, n + 1):
        yield i * i

# test
for num in square_generator(5):
    print(num)