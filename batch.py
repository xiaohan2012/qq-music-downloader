from threading import Thread
from Queue import Queue
from pickle import dump,load

from download import download_one
from util import get_tasks
from config import task_bin_name

class Worker(Thread):
    def __init__(self,q):
        Thread.__init__(self)
        self.q = q
    
    def run(self):
        while True:
            if q.unfinished_tasks == 0:
                break
            self.task = q.get()
            download_one(self.task)
            q.task_done()
            print "###remaining :%d" %q.unfinished_tasks

            self.notify_task_done()
    
    def notify_task_done(self):
        """remove the task in the task.bin pickle"""
        tasks = load(open(task_bin_name))
        del tasks[self.task["task_key"]]
        dump(tasks,open(task_bin_name,"w"))
        
if __name__ == "__main__":
    q = Queue()
    for k,t in get_tasks().items():
        t.update({"task_key":k})
        q.put(t)

    for i in xrange(5):
        worker = Worker(q)
        worker.setDaemon(True)
        worker.start()
    
    q.join()


