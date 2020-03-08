class CovidPrediction:
    def __init__(self):
        self.prediction_date = {'TOMORROW':1,'ONEWEEK':7,'30DAYS':30,'90DAYS':90}

    def predict(self, last_known_position, fun, arg_fun):
        _datapred_ = {}
        for d in self.prediction_date:
            _datapred_[d] = fun(last_known_position+self.prediction_date[d], *arg_fun)
        return _datapred_
