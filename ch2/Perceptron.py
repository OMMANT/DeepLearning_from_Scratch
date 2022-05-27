import numpy as np

class simple_perceptron:
    def __init__(self, x: np.ndarray):
        self.x = x
        assert isinstance(self.x, np.ndarray), 'numpy 배열이 아님'
        # 1차원 배열이 아닐경우 1차원 배열로
        if np.ndim(self.x) != 1:
            self.x = self.x.ravel()
        self.n = len(self.x)

    def AND(self, w=None, b=-0.7):        
        w = np.array([1 / self.n] * self.n) if w is None else w
        temp = np.sum(w*self.x) + b
        if temp <= 0:
            return 0
        else: return 1
    
    def NAND(self, w=None, b=0.7):
        w = np.array([-1 / self.n] * self.n) if w is None else w
        temp = np.sum(w*self.x) + b
        if temp <= 0:
            return 0
        else: return 1