import time

@profile # type: ignore
def heavy_work():
    print('Do something')
    print('Do something')
    print('Do something')
    for _ in range(100_100_100):
        pass

    print('Do something')
    print('Do something')

start_time = time.time()
heavy_work()
end_time = time.time()
print(f"Time taken: {end_time - start_time}")
