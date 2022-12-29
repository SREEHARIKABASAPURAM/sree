import threading
import time
start = time.perf_counter()
def calculateTime(seconds):
    print(f"Sleep for {seconds} second \n")
    time.sleep(seconds)
    print(f"Completed {seconds} sleep \n")
threads = []
for _ in range(3):
    thread = threading.Thread(target=calculateTime, args=[3])
    thread.start()
    threads.append(thread)
for t in threads:
    t.join()
finish = time.perf_counter()
print(f'Finished in {finish - start} seconds')