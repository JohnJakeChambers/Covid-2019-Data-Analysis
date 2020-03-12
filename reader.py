from io import StringIO
from requests import get
from pandas import read_csv, DataFrame


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

class DataReportCSVReaderWriter:
    __encoding__ = 'utf-8'
    def __init__(self, path):
        self.path = path

    def __readFile(self):
        return open(self.path,'rb').read()
    def getData(self):
        return read_csv(StringIO(self.__readFile().decode(DataReader.__encoding__)))

    def createReport(self):
        df = DataFrame(columns=['EndDate', 'Function', 'ricoverati_con_sintomi', 'terapia_intensiva', 'totale_ospedalizzati',\
                                    'isolamento_domiciliare','totale_attualmente_positivi','nuovi_attualmente_positivi',\
                                        'dimessi_guariti','deceduti','totale_casi','tamponi'])
        return df

    def saveData(self, df):
        df.to_csv(self.path, index=False)
