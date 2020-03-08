from io import StringIO
from requests import get
from pandas import read_csv


class DataReader:
    __encoding__ = 'utf-8'
    def __init__(self, url, reader_mode):
        self.url = url
        self.reader_mode = reader_mode

    def __requestURL(self):
        return get(self.url).content
    def __readFile(self):
        return open(self.url,'rb').read()

    def getData(self):
        if self.reader_mode == 'URL':
            s = self.__requestURL()
        elif self.reader_mode == "FILE":
            s = self.__readFile()
        return s, read_csv(StringIO(s.decode(DataReader.__encoding__)))
