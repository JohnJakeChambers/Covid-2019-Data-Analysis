import matplotlib.pyplot as plt

class Plotter:
    def plot_covid_data(x, yn, label1, fun, arg_fun, label2):
        plt.figure()
        plt.plot(x, yn, 'ko', label=label1)
        plt.plot(x, fun(x, *arg_fun), 'r-', label=label2)
        plt.legend()
        plt.show()


class LinearPlotter:
    def plot_line(x,y,intercept,slope):
        plt.plot(x, y, 'o', label='original data')
        plt.plot(x, intercept + slope * x, 'r', label='fitted line')
        plt.axhline(y=0, xmin=x[0], xmax=x[len(x)-1], color='black')
        plt.legend()
        plt.show()
