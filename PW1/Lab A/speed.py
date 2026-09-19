import time
from decay import simulate, simulate_loop

N0 = 200_000
lam = 0.4
dt = 0.05
steps = 200
seed = 0

start = time.perf_counter()
simulate_loop(N0, lam, dt=dt, steps=steps, seed = seed)
loop_time = time.perf_counter() - start

start = time.perf_counter()
simulate(N0, lam, dt = dt, steps= steps, seed = seed)
numpy_time = time.perf_counter() - start

speedup = loop_time/numpy_time

print(f"Pure-Python loop: {loop_time: .4f} s")
print(f"Numpy vectorised: {numpy_time: .4f} s")
print(f"Numpy is {speedup : .1f}x faster")