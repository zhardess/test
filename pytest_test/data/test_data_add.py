import numpy as np

class TestDataAdd():
    def __init__(self, x=None):
        self.x = x

x1 = np.random.randint(-5, 5, (10, 8)).astype(float)
test_data_add = TestDataAdd(x = x1)