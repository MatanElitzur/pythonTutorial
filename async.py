import asyncio # Import the asyncio module

async def process_order(): # Define new coroutine, async function
    await asyncio.sleep(1) # Wait with await --> that not block the execution! like sleep(1)
    print("Order complete")

async def main(): # Define another coroutine, async function
    await process_order() # Call and wait for coroutine to finish
    await process_order() # Call and wait for coroutine to finish, this order waits for the process_order above to finish
    print("Finished processing")

print("*** The first print ***")
asyncio.run(main()) # start event loop and run the main coroutine

print("*** The last code line ***")
# While waiting the event loop takes care of executing other coroutines
# Therefore it maximizes the use of the CPU core.

# When to use Asyncio
# 1.) When you need to perform many I/O-bound tasks
# 2.) When you need to perform many network-bound tasks (Networking applications)
# 3.) When you need to perform many tasks that require waiting (Data processing pipelines)
# 4.) When you need to perform many tasks that require waiting for external resources (APIs, Databases) (Asynchronous dependencies)

# When to Avoid Using Asyncio
# 1.) When you need to perform many CPU-bound tasks (CPU intensive tasks)
# 2.) When you need to perform many blocking tasks (Tasks that require waiting for a long time) (Blocking code) (Blocking Dependencies)