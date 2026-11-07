"""Line-by-line timings."""
from line_profiler import LineProfiler
from profiler import slow_function, fast_function, memory_intensive_function, main, optimized_fast_function


def profile_main():
    profiler = LineProfiler()
    profiler.add_function(slow_function)
    profiler.add_function(optimized_fast_function)
    profiler.add_function(memory_intensive_function)
    profiler.runcall(main)
    profiler.print_stats()


if __name__ == "__main__":
    profile_main()
