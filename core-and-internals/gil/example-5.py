import numpy as np
import threading
import time


def numpy_task(arr):
    return np.sum(arr**2)


arr = np.random.rand(10_000_000)

start = time.time()
t1 = threading.Thread(target=numpy_task, args=(arr,))
t2 = threading.Thread(target=numpy_task, args=(arr,))
t1.start()
t2.start()
t1.join()
t2.join()
print(f"NumPy threaded: {time.time() - start:.2f}s")
