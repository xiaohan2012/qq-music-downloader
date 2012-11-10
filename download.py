from urllib2 import Request, urlopen
from urlparse import urlparse
from os import path

from util import *

def download_one(music_name,url,output_dir = "music"):
    headers = load_headers()
    headers["Host"] = urlparse(url).hostname#change the host accordingly
    print headers
    req = urlopen(Request(url,headers = headers))
    
    f = open(path.join(output_dir,music_name + ".mp3"),"bw")
    f.write(req.read())
    f.close()
    
if __name__ == "__main__":
    download_one("1","http://stream17.qqmusic.qq.com/30585637.mp3")
