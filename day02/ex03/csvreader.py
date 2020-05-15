import re

class CsvReader():
    def __init__(self, filename=None, sep=',', header=False, skip_top=0, skip_bottom=0):
        self.filename = filename
        self.sep = sep
        self.header = header
        self.skip_top = skip_top
        self.skip_bottom = skip_bottom
        self.fd = None
        self.data = []
        self.head = []

    def __enter__(self):
        try:
            self.fd = open(self.filename, 'r', errors='ignore')
        except FileNotFoundError:
            exit(f"File {self.filename} not found.")
        else:
            PATTERN = re.compile(r'''((?:[^'''+self.sep+'''"]|"[^"]*")+)''')
            self.filedata = self.fd.read().split("\n")
            for line, n in zip(self.filedata, range(len(self.filedata))):
                if len(line) > 0 and n == 0:
                    self.data.append(PATTERN.split(line)[1::2])
                elif len(line) > 0 and n > self.skip_top and len(self.filedata) - n > self.skip_bottom:
                    self.data.append(PATTERN.split(line)[1::2])
            self.head = self.data[0]
            if not self.header:
                self.data.pop(0)
            for line in self.data:
                if len(line) != len(self.head):
                    return None
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.fd.close()

    def getdata(self):
        return self.data

    def getheader(self):
        return self.head