from ast import literal_eval
class hexopen:
    def __init__(self, file, mode):
        self.file = file
        self.mode = mode
        self.open = open(self.file, self.mode)
    def readline(self, limit=-1):
        s = self.open.readline(limit).split(';')
        __q = ""
        __x = []
        for a in s:
            if a != "":
                __x.append(chr(literal_eval(a)))
                __q = "".join(__x)
        return __q
    def write(self, s):
        for char in s:
            self.open.write(str(hex(ord(char))) + ';')
    def writelines(self, lines):
        for char in lines:
            self.open.writelines(hex(ord(char)))
    def close(self, ):
        self.open.close()
    def flush(self):
        return self.open.flush()
    def seek(self, cookie, whence=0):
        return self.open.seek(cookie, whence)
    def fileno(self):
        return self.open.fileno()
    def tell(self):
        return self.open.tell()
    def truncate(self, pos=None):
        return self.open.truncate(pos)
    def isatty(self):
        return self.open.isatty()
    def seekable(self):
        return self.open.seekable()
    def readable(self):
        return self.open.readable()
    def writable(self):
        return self.open.writable()
def info():
    print("""
    Hardly Tested commands:
    write
    close
    readline
    
    Other could crash 
    """)

