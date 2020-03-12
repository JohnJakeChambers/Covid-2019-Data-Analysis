import configparser
from os import path

from reader import DataReportCSVReaderWriter
from business import ExtractCSVReportData
from fit import CurveReport
from plot import LinearPlotter

if __name__ == "__main__":
    ############# CONFIGURATION #############
    config = configparser.ConfigParser()
    config.read('config.ini')

    assert ('COVID_DATA' in config and 'RUN' in config and 'CONFIGREPORT' in config)
    assert ('url' in config['COVID_DATA'] and 'datacolumns' in config['COVID_DATA'])
    assert('addreportcsv' in config['CONFIGREPORT'] and 'filereportcsvname' in config['CONFIGREPORT'])
    assert ('reader_mode' in config['RUN'] and 'report_dir' in config['RUN'] and\
                    'filereportname' in config['RUN'] and 'showplot' in config['RUN'] and\
                        'rawfilename' in config['RUN'] and 'fun' in config['RUN']\
                            and 'predictionfilename' in config['RUN'])

    data_columns = config['COVID_DATA']['datacolumns'].split(",")
    base_dir_report = config['RUN']['report_dir']
    filereportcsvname = config['CONFIGREPORT']['filereportcsvname']
    #############  #############

    ## PREPARE ##
    csvreport = DataReportCSVReaderWriter(path.join(base_dir_report,filereportcsvname))
    dataextract = ExtractCSVReportData(data_columns)
    curve = CurveReport()
    ## #####  ##

    df = csvreport.getData()
    start_date, fun = dataextract.getMinMaxDate(df)

    x,data = dataextract.getData(start_date,df)

    test1 = data['totale_casi']
    coefftest1 = [el[1] for el in test1]
    slope,intercept,r_value,p_value,std_err = curve.getCurve(x,coefftest1)

    testzero = -intercept / slope
    print(testzero)
    import numpy

    x = numpy.append(x, testzero)
    x = numpy.append(x, testzero+5)
    coefftest1 = numpy.append(coefftest1, intercept + slope * (testzero))
    coefftest1 = numpy.append(coefftest1, intercept + slope * (testzero+5))

    LinearPlotter.plot_line(x,coefftest1,intercept,slope)