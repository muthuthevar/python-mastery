from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
import time


def cpu_task(n):
    return sum(range(n))


N = 10_000_000


if __name__ == "__main__":

    # Threads
    with ThreadPoolExecutor(max_workers=4) as ex:
        start = time.time()
        results = list(ex.map(cpu_task, [N] * 4))
        print(results)
        print(f"Threads: {time.time() - start:.2f}s")

    # Processes
    with ProcessPoolExecutor(max_workers=4) as ex:
        start = time.time()
        results = list(ex.map(cpu_task, [N] * 4))
        print(results)
        print(f"Processes: {time.time() - start:.2f}s")
