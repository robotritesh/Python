# Generate Fibonacci sequence
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

fib_seq = list(fibonacci(10))
print("Fibonacci Sequence:", fib_seq)
