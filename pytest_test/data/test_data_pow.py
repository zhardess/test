import numpy as np

class TestDataPow():
    def __init__(self, x=None, n=None):
        self.x = x
        self.n = n


x1 = np.random.randint(-5, 5, 10).astype(float)
n1 = np.random.randint(-2, 2, 10)
test_data_pow = TestDataPow(x = x1, n = n1)