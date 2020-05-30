import threading
import queue as qu
from widget import Message
import time

class Worker(threading.Thread):
    def __init__(self, message_queue:qu.Queue):
        self.message_queue = message_queue

    def run(self):
        for i in range(10):
            men = Message("mensage "+str(i),i*10,False)
            if(i== 10):
                men.lastmessage=True
            self.message_queue.put(men)
            time.sleep(2)         

