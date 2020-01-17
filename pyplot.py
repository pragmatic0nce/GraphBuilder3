import matplotlib.pyplot as plt
import numpy as np
from prettytable import PrettyTable


def f(x, eval1):

    return eval(eval1)


def f1(x, eval1):

    return eval(eval1)


table = PrettyTable()
table.field_names = ["x", "f0(x)", "f1(x)"]


def makeGraph(eval1, eval2, x, y, r, c1, c2):
    # table.field_names = ["x", eval1, eval2]
    m_eval1 = eval1
    m_eval2 = eval2

    if "cos" in str(m_eval1):
        m_eval1.replace("cos", "np.cos")

    if "cos" in str(m_eval2):
        m_eval2.replace("cos", "np.cos")

    r_x = np.arange(-r, r, 0.1)
    r_y1 = [eval(m_eval1) for x in r_x]
    r_y2 = [eval(m_eval2) for x in r_x]
    y_max = 0
    for i in range(len(r_y1)):
        if r_y1[i] > y_max:
            y_max = r_y1[i]
        if r_y2[i] > y_max:
            y_max = r_y2[i]

    x_max = 0
    for i in range(len(r_x)):
        if r_x[i] > x_max:
            x_max = r_x[i]

    x_axis = np.arange(-100, 100, 1)
    y_axis = [0 for i in range(len(x_axis))]
    print
    for x in r_x:
        n_x = 0
        if round(eval(m_eval1), 1) == round(eval(m_eval2), 1) and abs(x - n_x) > 0.2:
            table.add_row([round(x, 1), round(eval(m_eval1), 1), round(eval(m_eval2), 1)])
            plt.plot(round(x, 1), round(eval(m_eval1), 1), 'bo')
        n_x = x

    for i in table:
        print(i)

    print(table)
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.axis([-x_max, x_max, -y_max, y_max])
    plt.plot(x_axis, y_axis, 'k')
    x_axis, y_axis = y_axis, x_axis
    plt.plot(x_axis, y_axis, 'k')
    plt.plot(r_x, f(r_x, m_eval1), c1)
    plt.plot(r_x, f1(r_x, m_eval2), c2)
    plt.show()


if __name__ == '__main__':
    ev1 = input("Enter 1st function: ")
    ev2 = input("Enter 2nd function: ")
    makeGraph(ev1, ev2, 10, 10, 50)
