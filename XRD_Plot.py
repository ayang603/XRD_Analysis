import matplotlib.pyplot as plt
from numpy import genfromtxt


def plot_2var(filename, title, x_axis, y_axis):
    if filename is None:
        return

    # Gets data from file to array
    data = genfromtxt(filename)
    x_data, y_data = zip(*data)

    # Plots data
    plt.plot(x_data, y_data)

    # Plot name and axis name
    plt.title(title)
    plt.xlabel(x_axis)
    plt.ylabel(y_axis)

    return plt.show()


def main():
    title = "YBCO XRD Analysis"
    x_axis = "2Theta"
    y_axis = "Intensity (Au)"

    file_name = input("File Name?")
    print("\n" + file_name + "selected")

    plot_2var(file_name, title, x_axis, y_axis)


if __name__ == "__main__":
    main()
