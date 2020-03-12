# Covid-2019-Data-Analysis
A project that gives an analys about the spreading of Covid-2019 in Italy.

The source data is Protezione Civile Italiana that mantains the repository https://github.com/pcm-dpc/COVID-19.
The code is ready to read any CSV. The config must contains the matching columns for data analysis.
The first commit contains the columns listed in https://github.com/pcm-dpc/COVID-19/blob/master/dati-andamento-nazionale/dpc-covid19-ita-andamento-nazionale.csv.

You can also switch to source to a CSV file stored on your disk. You can simply change the variabile reader_mode in config.ini to FILE.

The config.ini contains all the program variables:
- url: It's the url that points to a web resource that contains the CSV file, or it's the path to your CSV file
- datacolumns. Comma separated values that lists the CSV columns that must be analyzed.

- fun: The curve fitting function. Currently We have 3 functions available (exp, exp simple, power of two). See the fit module.
- reader_mode: URL or TXT. Depending on the source that has been set on the "url" variable.
- report_dir: The directory that contains the report of the analysis. The program will create a new dir under this report_dir for every analysis You made.
- filereportname, predictionfilename: The filename you want to assing to the Report log and to the Prediction Log.
- rawfilename: Once the program read the input, it will be saved in this file.
- showplot: The value should be 0 or 1. If the value is 1 then the plot module is launched and it shows on video the results of curve fitting.
- filereportcsvname: A csv file that contains each result of curve processing
- addreportcsv: The value should be 0 or 1. If the value is 1 then the result will be added to the filereportcsvname



