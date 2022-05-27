import numpy as np

class simple_perceptron:
    def __init__(self, x1, x2):
        self.x1 = x1
        self.x2 = x2

    def AND(self):
        x = np.array([self.x1, self.x2])
        w = np.array([0.5, 0.5])
        b = -0.7
        temp = np.sum(w*x) + b
        if temp <= 0:
            return 0
        else: return 1
    