import socket
import threading
import queue

IP = '10.5.95.230'
q = queue.Queue()

#storing port numbers in a queue

for i in range (1, 1001):
    q.put(i)
    
def scan():
    while not q.empty():
        port = q.get()
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            try:
                s.connect((IP, port))
                print(f'port {port} is open')
                
            except:
                pass
            q.task_done()

        
    
#create the number of threads we want to use
for i in range (30):
    t = threading.Thread(target=scan, daemon=True)
    t.start()
    
q.join()
print('finished')