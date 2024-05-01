from empty_loop import heavy_work

# For this to run you should execute the command pytest from the terminal
def test_benchmark_heavy_work(benchmark):
    benchmark(heavy_work)
   