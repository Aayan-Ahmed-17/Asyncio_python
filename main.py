import time
import asyncio
#sync code first:
'''
def count():
    print("One")
    time.sleep(1)
    print("Two")
    time.sleep(1)
    
def main():
    for _ in range(3):
        count()
        
if __name__ == "__main__":
    start = time.perf_counter()
    main()
    elapsed = time.perf_counter() - start
    
    print(f"Code exceuted in {elapsed:.2f}s")
'''

# Aysnc code implementation for above code
async def count():
    print("One")
    await asyncio.sleep(1)
    print("Two")
    await asyncio.sleep(1)
    
async def main():
    await asyncio.gather(count(), count(), count())
    
if __name__ == "__main__":
    start = time.perf_counter()
    asyncio.run(main())
    elapsed = time.perf_counter() - start
    
    print(f"Code executed in {elapsed:.2f}s")
    
    