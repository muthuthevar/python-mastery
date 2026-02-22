import multiprocessing
import time


def cpu_task(n):
    count = 0
    for _ in range(n):
        count += 1
    return count


N = 50_000_000


if __name__ == "__main__":
    start = time.time()
    with multiprocessing.Pool(processes=2) as pool:
        results = pool.map(cpu_task, [N, N])
    print(f"Multi processing: {time.time() - start:.2f}s")
