from datetime import datetime
import numpy as np

class ExtractCovidData:
    def __init__(self, columns):
        self.datacodiv = columns

    def getData(self, dataframe):
        start_date = datetime.strptime(dataframe['data'][0], "%Y-%m-%d %H:%M:%S").date()
        end_date = datetime.strptime(dataframe['data'][len(dataframe['data'])-1], "%Y-%m-%d %H:%M:%S").date()
        return start_date,end_date

    def prepareForFit(self, dataframe):
        x = range(dataframe[self.datacodiv[0]].size)
        y = {}
        columns = [c for c in dataframe.columns if c.lower() in self.datacodiv]
        for c in columns:
            y[c] = dataframe[c].values

        return x,y


class ExtractCSVReportData:
    def __init__(self, columns):
        self.datacodiv = columns

    def getMinMaxDate(self, dataframe):
        start_date = datetime.strptime(dataframe['EndDate'][0], "%Y-%m-%d").date()
        return start_date,dataframe['Function'][0]

    def getData(self, base_date, dataframe):
        dates = np.array([(datetime.strptime(d, "%Y-%m-%d").date()-base_date).days for d in dataframe['EndDate']])
        columns = {}
        for col in self.datacodiv:
            columns[col] = []
            for c in dataframe[col]:
                columns[col].append(self.splitData(c))
        return dates,columns

    def splitData(self, data):
        return np.asarray(data.split("#"), dtype=np.float64)
