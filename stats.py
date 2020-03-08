import numpy as np

class ComputeStat:
    def computeRSquare(self, x, yn, popt, fun):
        residuals = yn - fun(x, *popt)
        ss_res = np.sum(residuals ** 2)
        ss_tot = np.sum((yn - np.mean(yn)) ** 2)
        r_squared = 1 - (ss_res / ss_tot)

        return r_squared
