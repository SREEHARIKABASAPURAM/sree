#threading
import time
start = time.perf_counter()
def calculateTime():
    print("Sleep for 5 second")
    time.sleep(5)
    print("Completed sleep")
calculateTime()
calculateTime()
calculateTime()
finish = time.perf_counter()
print(f'Finished in {finish - start} seconds')

