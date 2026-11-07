"""Line-by-line memory usage."""
import time
from memory_profiler import profile


@profile
def slow_function():
    time.sleep(2)
    total = 0
    for i in range(10000):
        total += i ** 2
    return total


@profile
def fast_function():
    total = 0
    for i in range(100):
        total += i ** 2
    return total


@profile
def memory_intensive_function():
    n = 10_000_000
    return n * (n - 1) * (2 * n - 1) // 6

@profile
def optimized_fast_function():
    return sum(i ** 2 for i in range(100))


def main():
    slow_function()
    optimized_fast_function()
    memory_intensive_function()


if __name__ == "__main__":
    main()
