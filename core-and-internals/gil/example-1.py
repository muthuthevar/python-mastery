import threading
import time


def cpu_task(n):
    count = 0
    for _ in range(n):
        count += 1
    return count


N = 50_00_000

# Single threaded
start = time.time()
cpu_task(N)
cpu_task(N)
print(f"Single threaded: {time.time() - start:.2f}s")


# Multi threaded
start = time.time()
t1 = threading.Thread(target=cpu_task, args=(N,))
t2 = threading.Thread(target=cpu_task, args=(N,))
t1.start()
t2.start()
t1.join()
t2.join()
print(f"Multi threaded: {time.time() - start:.2f}s")
