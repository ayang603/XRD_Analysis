# File Name: XRD.py
#
# Description: Plots XRD data given in .txt file
#
# Notes:  Remember REMOVE the "?" line in the beginning of your text file
#

import numpy as np
import matplotlib.pyplot as plt


# Returns a list of the maximum of the xrd data
def peak_finder(given, num):
    lst = []
    s_rng = .5

    for i in range(given[0][0], given[0][-1], s_rng):
        given = 0

    return lst[:-1 * num]


# Plots XRD data
def plot_xrd(data, num_peaks):
    # Creates a list of "ordered pairs"
    data_lst = []
    xData, yData = zip(*data)
    for i in range(len(xData)):
        data_lst.append([xData[i], yData[i]])

    # Creates a list of Relative Maximum "ordered pairs"
    max_lst = peak_finder(data_lst, num_peaks)

    # Plotting Stuff

    for i, label in enumerate(num_peaks):
        plt.annotate(label, (max_lst[i][0], max_lst[i][1]))
        plt.scatter(max_lst[i][0], max_lst[i][1], color='red')

    plt.plot(xData, yData)
    plt.title("Intensity vs 2*Theta")
    plt.xlabel("2*Theta")
    plt.ylabel("Intensity (AU)")
    plt.xticks(np.arange(20, 82, step=4))
    plt.grid(True)

    plt.show()


def main():
    # Remember REMOVE the "?" line in the beginning of your text file
    # Filename of your XRD data and number of peaks desired in plot

    # filename = input("Enter File Name: ")
    filename = "Ravi.txt"
    num_peaks = 12

    data = np.genfromtxt(filename, delimiter='    ')  # Extracts data from .txt file
    print(data)
    
    for i in range(len(data)):
        data[i][0] = data[i][0]/len(data)

    # plot_xrd(data, num_peaks)  # Plots
    sp = np.fft.fft(data)
    sp = np.power(sp, 2)

    plt.plot(sp)
    plt.show()


if __name__ == "__main__":
    main()
