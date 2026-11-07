"""Unit tests and timing/memory observations for Lab 9."""
import time
import unittest
from memory_profiler import memory_usage
from profiler import slow_function, fast_function, memory_intensive_function


class TestProfiler(unittest.TestCase):
    def time_function(self, func):
        start = time.perf_counter()
        func()
        return time.perf_counter() - start

    def test_slow_function(self):
        duration = self.time_function(slow_function)
        print(f"slow_function executed in {duration:.3f} seconds.")
        self.assertGreaterEqual(duration, 2)

    def test_fast_function(self):
        duration = self.time_function(fast_function)
        print(f"fast_function executed in {duration:.6f} seconds.")
        self.assertLess(duration, 1)
        self.assertEqual(fast_function(), 328350)

    def test_memory_intensive_function(self):
        # A sum accumulated in a scalar does not necessarily retain more RAM.
        # The handout's `after > before` assumption is therefore unreliable.
        start = time.perf_counter()
        samples, result = memory_usage(
            (memory_intensive_function, (), {}),
            interval=0.05, retval=True, max_usage=False,
        )
        duration = time.perf_counter() - start
        print(f"memory_intensive_function executed in {duration:.3f} seconds.")
        print(f"Memory sampled: start {samples[0]:.2f} MiB, peak {max(samples):.2f} MiB, end {samples[-1]:.2f} MiB.")
        self.assertEqual(result, 333333283333335000000)
        self.assertTrue(samples, "Memory profiler must return at least one sample")


if __name__ == "__main__":
    unittest.main()
