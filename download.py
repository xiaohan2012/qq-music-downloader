from urllib2 import Request, urlopen
from urlparse import urlparse
import os
import re

from util import *
from task import DownloadTask

    

def download_one(task, output_dir = "music"):

    music_name = task["piece_name"]
    composer = task["composer"]
    url = task["url"]

    print "downloading %s" %music_name
    headers = load_headers()
    headers["Host"] = urlparse(url).hostname#change the host accordingly
    #print url,music_name,headers
    #print headers
    req = urlopen(Request(url,headers = headers))

    output_dir = os.path.join(output_dir,composer)
    #create necessary subdir
    if not os.path.exists(os.path.join(output_dir,composer)):
        os.system("mkdir -p %s" %output_dir)

    f = open(os.path.join(output_dir,music_name + ".mp3"),"w")
    f.write(req.read())
    f.close()
    
if __name__ == "__main__":
    download_one("moonlight","http://stream13.qqmusic.qq.com/31638463.mp3")
