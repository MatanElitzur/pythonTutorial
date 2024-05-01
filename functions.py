import random

# to test this code performance run the following command: kernprof -l -v functions.py OR python3 -m memory_profiler functions.py
def get_random_integer():
    return random.randint(0, 100)

@profile
def main():
  [random.randint(0, 100) for _ in range(100_000)] # This is the fastest
  [get_random_integer() for _ in range(100_000)] # This is the second fastest
  [(lambda: random.randint(0, 100))() for _ in range(100_000)] # This is the slowest

main()