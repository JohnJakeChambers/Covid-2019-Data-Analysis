from datetime import datetime

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
