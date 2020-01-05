from random import shuffle

import matplotlib
import matplotlib.pyplot as plt
import numpy as np

matplotlib.use("TkAgg")

plt.ion()


def create_random_list(length):
    l = [i for i in range(1, length + 1)]
    shuffle(l)
    return l


def display(l, curr=-1, next=-1, color="#1E77B4", x=None, title=""):
    plt.clf()
    if not x:
        x = range(len(l))

    if not len(l) == len(x):
        l = l + [0] * (len(x) - len(l))

    bar_l = plt.bar(x, l, color=color)

    if curr >= 0:
        # change the color of current bar to red
        bar_l[curr].set_color('yellow')

    if next >= 0:
        # change the color of next bar to green
        bar_l[next].set_color('g')
    axes = plt.gca()
    axes.set_title(title)
    axes.set_ylim([0, 10])
    axes.set_ylabel("Value")
    axes.set_xlabel("Index")

    plt.xticks(np.arange(0, 10 + 1, 1))
    plt.yticks(np.arange(0, 11, 1))
    plt.draw()
    plt.pause(0.5)


def display_list(l):
    display(l, color="#AF9AB2", x=range(10), title="List")


def display_heap(h):
    plt.clf()
    c1 = "#84B4D6"
    c2 = "#468FC1"
    c3 = "#1C6DA4"
    c4 = "#144C73"
    h = h + [0] * (10 - len(h))
    bar_l = plt.bar(range(10), h, color=[c1] + [c2] * 2 + [c3] * 4 + [c4] * 3)
    axes = plt.gca()
    axes.set_title("Heap")
    axes.set_ylim([0, 10])
    axes.set_ylabel("Value")
    axes.set_xlabel("Index")
    plt.xticks(np.arange(0, 11, 1))
    plt.yticks(np.arange(0, 11, 1))
    plt.draw()
    plt.pause(0.5)


def display_end(l):
    # TODO: use a more elegant method to keep the graph
    plt.clf()
    plt.bar(range(len(l)), l)
    plt.draw()
    plt.pause(10000000)


def display_match(l, match, *iter):
    # TODO: change the bar color to default blued
    if match:
        for i in range(2):
            bar_l = plt.bar(range(len(l)), l, color="#1E77B4")
            bar_l[iter[0]].set_color("#e74c3c")
            bar_l[iter[1]].set_color("#e74c3c")
            plt.draw()
            plt.pause(0.2)
            bar_l = plt.bar(range(len(l)), l, color="#1E77B4")
            bar_l[iter[0]].set_color("white")
            bar_l[iter[1]].set_color("white")
            plt.draw()
            plt.pause(0.2)
    else:
        for i in range(2):
            bar_l = plt.bar(range(len(l)), l, color='#1E77B4')
            bar_l[iter[0]].set_color("#7f8c8d")
            bar_l[iter[1]].set_color("#7f8c8d")
            plt.draw()
            plt.pause(0.2)
            bar_l = plt.bar(range(len(l)), l, color='#1E77B4')
            bar_l[iter[0]].set_color("white")
            bar_l[iter[1]].set_color("white")
            plt.draw()
            plt.pause(0.2)
