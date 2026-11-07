"""Computation functions for profiling."""
import time


def slow_function():
    time.sleep(2)
    total = 0
    for i in range(10000):
        total += i ** 2
    return total


def fast_function():
    total = 0
    for i in range(100):
        total += i ** 2
    return total


def memory_intensive_function():
    """Compute the same sum of squares without 10 million loop iterations."""
    n = 10_000_000
    return n * (n - 1) * (2 * n - 1) // 6



def optimized_fast_function():
    return sum(i ** 2 for i in range(100))


def main():
    slow_function()
    optimized_fast_function()
    memory_intensive_function()


if __name__ == "__main__":
    main()
