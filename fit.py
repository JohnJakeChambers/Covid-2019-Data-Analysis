import numpy as np
from scipy.optimize import curve_fit

### UPDATE - 8 March 2020 ###
### In this period, the spreading of Covid-2019 follows exponential logics ###

def _exponential(x, a, b, c):
    return a * np.exp(b * x) + c

def _exponential_simple(x, a, b):
    return a*np.exp(b * x)

def _power_of_two(x, a, b):
    return a*np.power(2, b*x)

class CovidFitFunctions:
    def __init__(self):
        self.functions = {}
        self.funrepr = {}
        self.__loadFunctions()

    def __loadFunctions(self):
        self.functions['EXP'] = _exponential
        self.functions['EXPSIMPLE'] = _exponential_simple
        self.functions['POWEROFTWO'] = _power_of_two

        self.funrepr['EXP'] = "y = {0}*exp^{1}*x  +  {2}"
        self.funrepr['EXPSIMPLE'] = "y = {0}*exp^{1}*x"
        self.funrepr['POWEROFTWO'] = "y = {0}*2^{1}*x"


    def fitData(self, x, yn, function_label):
        return curve_fit(self.functions[function_label], x, yn)

    def getFun(self, label):
        return self.functions[label]

    def getFunRepr(self, label, format_arg):
        format_arg_round = (round(a,2) for a in format_arg)
        return self.funrepr[label].format(*format_arg_round)
