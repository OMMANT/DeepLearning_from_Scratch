import numpy as np

class simple_perceptron:
    def __init__(self, x1, x2):
        self.x1 = x1
        self.x2 = x2

    def AND(self):
        w1, w2, theta = 0.5, 0.5, 0.7
        temp = self.x1 * w1 + self.x2 * w2
        if temp <= theta:
            return 0
        else: return 1
    