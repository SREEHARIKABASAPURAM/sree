import threading
import time
start = time.perf_counter()
def calculateTime():
    print("Sleep for 5 second \n")
    time.sleep(5)
    print("Completed sleep \n")
t1 = threading.Thread(target = calculateTime)
t2 = threading.Thread(target = calculateTime)
t3 = threading.Thread(target = calculateTime)
t4 = threading.Thread(target = calculateTime)
t1.start()
t2.start()
t3.start()
t4.start()
t1.join()
t2.join()
t3.join()
t4.join()
finish = time.perf_counter()
print(f'Finished in {finish - start} seconds')
#using loops
import threading
import time
start = time.perf_counter()
def calculateTime():
    print("Sleep for 5 second \n")
    time.sleep(5)
    print("Completed sleep \n")
threads = []
for _ in range(5):
    thread = threading.Thread(target=calculateTime)
    thread.start()
    threads.append(thread)
for t in threads:
    t.join()
finish = time.perf_counter()


