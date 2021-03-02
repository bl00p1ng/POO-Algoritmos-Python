import time


def factorial(n):
    answer = 1

    while n > 1:
        answer *= n
        n -= 1

    return answer


def recursive_factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


if __name__ == '__main__':
    n = 10000

    start = time.time()
    factorial(n)
    end = time.time()
    print(end - start)

    start = time.time()
    recursive_factorial(n)
    end = time.time()
    print(end - start)
