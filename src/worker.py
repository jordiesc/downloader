import threading
import queue as qu
from widget import Message
import time

class Worker(threading.Thread):
    def __init__(self, message_queue:qu.Queue):
        # Daemon make destroy the threads when main trhead ends
        threading.Thread.__init__(self,daemon=True)
        self.message_queue = message_queue

    def run(self):
        size = 10
        for i in range(size):
            print("debug en")
            print(float(i*10))
            men = Message("mensage "+str(i)+"\n",float(10),False)
            if(i== size-1):
                men.lastmessage=True
            self.message_queue.put(men)
            time.sleep(2) 


