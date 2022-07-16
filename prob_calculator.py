"""
Probability Calculator
"""

import random


class Hat:

    def __init__(self, *args):
        self.list = list()
        self.aux = list()
        for arg in args:
            for name, value in arg.items():
                for i in range(value):
                    self.list.append(name)


    def __str__(self):
        return ''

    def draw(self, balls=1):
        random.shuffle(self.list)
        for i in range(balls):
            self.aux.append(self.list[i])
        self.list, self.aux = self.aux, self.list
        return self.list


def experiment(hat=object, expected_balls=dict, num_balls_drawn=1, num_experiments=1):
    prob = 0
    aux = expected_balls
    for experiment in range(num_experiments):
        ax = list()
        cont = 0
        li = hat.draw(num_balls_drawn)
        for key, val in aux.items():
            for i in range(val):
                ax.append(key)
        for key_li in range(len(li)):
            for key_ax in range(len(ax)):
                if ax[key_ax] == li[key_li]:
                    cont += 1
                if cont == len(ax):
                    prob += 1
        # print(len(ax), cont)
    cont = 0

    return f'The probability is {prob/num_experiments}%'
