
def load_headers(path="headers.txt"):
    f = open(path,"r")
    hd = dict(l.split(":",1) for l in f.readlines())
    f.close()
    return hd

if __name__ == "__main__":
    print load_headers()
