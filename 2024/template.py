import time

t1 = time.time() * 1000


# Calc execution time
t2 = time.time() * 1000
print(f"Executed in {t2 - t1:0.3f} milliseconds")