from reader import DataReader
from business import ExtractCovidData
from fit import CovidFitFunctions
from stats import ComputeStat
from plot import Plotter
from utils import LOGROW,PREDICTIONLOG
from prediction import CovidPrediction

from datetime import datetime

from os import path,mkdir

import configparser

if __name__ == "__main__":
    ############# CONFIGURATION #############
    config = configparser.ConfigParser()
    config.read('config.ini')

    assert('COVID_DATA' in config and 'APP' in config)
    assert('url' in config['COVID_DATA'] and 'datacolumns' in config['COVID_DATA'])
    assert ('reader_mode' in config['APP'] and 'report_dir' in config['APP'] and\
                    'filereportname' in config['APP'] and 'showplot' in config['APP'] and\
                        'rawfilename' in config['APP'] and 'fun' in config['APP']\
                            and 'predictionfilename' in config['APP'])

    data_columns = config['COVID_DATA']['datacolumns'].split(",")

    base_dir_report = config['APP']['report_dir']

    filereportname = config['APP']['filereportname']
    rawfilename = config['APP']['rawfilename']
    predictionfilename = config['APP']['predictionfilename']

    funname = config['APP']['fun']
    #############  #############

    ## PREPARE ##
    reader = DataReader(config['COVID_DATA']['url'],config['APP']['reader_mode'])
    dataextract = ExtractCovidData(data_columns)
    fittingclass = CovidFitFunctions()
    statcalc = ComputeStat()
    prediction = CovidPrediction()

    _idelab_ = datetime.now().strftime("%Y%m%d_%H%M%S")
    _reportdir_ = path.join(base_dir_report, _idelab_)
    if not path.exists(base_dir_report):
        mkdir(base_dir_report)
    _reportlog_ = []
    if not path.exists(_reportdir_):
        mkdir(_reportdir_)


    _reportlog_.append(LOGROW.format(dt = str(datetime.now()), tx = "Start Process "+_idelab_))
    _reportlog_.append(LOGROW.format(dt=str(datetime.now()), tx="Dir Report" + _reportdir_))


    ## READ AND ANALYZE DATA ##
    raw, dataframe_covid = reader.getData()
    with open(path.join(_reportdir_,rawfilename),'wb') as fraw:
        fraw.write(raw)
    _reportlog_.append(LOGROW.format(dt=str(datetime.now()), tx="Raw data saved"))

    start_date, end_date = dataextract.getData(dataframe_covid)
    x, y_series = dataextract.prepareForFit(dataframe_covid)

    _reportlog_.append(LOGROW.format(dt=str(datetime.now()), tx="Start Date" + str(start_date)+" End Date" + str(end_date)))
    _reportlog_.append(LOGROW.format(dt=str(datetime.now()), tx="Fit Function:" + funname))

    ## DATA FIT  AND PREDICTION ##
    _predictionlog_ = []

    for y in y_series:
        yn = y_series[y]
        popt, pcov = fittingclass.fitData(x, yn, funname)
        r_squared = statcalc.computeRSquare(x, yn, popt, fittingclass.getFun(funname))

        #print(y, *popt, " R2: ", r_squared)
        _results_ = y + " "+ str([round(p,5) for p in popt])+" R2: ", str(r_squared)
        _reportlog_.append(LOGROW.format(dt=str(datetime.now()), tx=_results_))
        data_prediction = prediction.predict(x[len(x)- 1],fittingclass.getFun(funname), popt)
        for d in data_prediction:
            _predictionlog_.append(PREDICTIONLOG.format(subj = y, pd = d, val = str(round(data_prediction[d],5))))


        if config['APP']['showplot'] == "1":
            _funlabel_ = fittingclass.getFunRepr(funname, popt)
            _funlabel_ += "  R2: "+str(round(r_squared,3))
            Plotter.plot_covid_data(x, yn, y, fittingclass.getFun(funname), popt, _funlabel_)

    _reportlog_.append(LOGROW.format(dt=str(datetime.now()), tx="End Process "+_idelab_))

    with open(path.join(_reportdir_,filereportname),'w') as fw:
        fw.write("\n".join(_reportlog_))
    with open(path.join(_reportdir_,predictionfilename),'w') as fw:
        fw.write("\n".join(_predictionlog_))
