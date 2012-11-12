import codecs
import os
from pickle import load,dump
from hashlib import sha1

from task import DownloadTask

from config import task_bin_name 

def load_headers(path="headers.txt"):
    f = open(path,"r")
    hd = dict(l.strip().split(":",1) for l in f.readlines())
    f.close()
    return hd

def _gen_key(msg):
    return sha1(msg).hexdigest()

def get_tasks(task_file="tasks.txt"):
    if os.path.exists(task_bin_name):#if pickle exists, return it
        tasks = load(open(task_bin_name,"r"))
    else:
        tasks = dict()
    
    f = codecs.open(task_file,"r","utf8")
    for l in f.readlines():
        if l.strip():
            music_name,composer,urls = l.strip().split(",")
            for url in urls.strip().split(" "):
                key = _gen_key(url)

                task = DownloadTask()
                task["task_key"] = key
                task["composer"] = composer.strip()
                task["url"] = url.strip()
                task["piece_name"] =  "%s_%s" %(music_name.strip(),key)
                tasks[key] = task
    open(task_file,"w").close()#clear task file content
    dump(tasks,open(task_bin_name,"w"))
                    
    return tasks                
if __name__ == "__main__":
    #print load_headers()
    tasks = get_tasks()
    print len(tasks)
    for k in tasks.keys():
        print k
