from time import sleep, time
import threading

start = time()
def somthing(id):
    print(f"Thread {id} is starting.")
    sleep(2)
    print(f"Thread {id} is done.")

threads = [ threading.Thread(target=somthing, args=[i]) for i in range(10) ]

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()
    
end = time()

print(f"Total time taken: {end - start} seconds.")