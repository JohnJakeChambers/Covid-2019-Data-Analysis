import matplotlib.pyplot as plt

class Plotter:
    def plot_covid_data(x, yn, label1, fun, arg_fun, label2):
        plt.figure()
        plt.plot(x, yn, 'ko', label=label1)
        plt.plot(x, fun(x, *arg_fun), 'r-', label=label2)
        plt.legend()
        plt.show()
