############################# ADD BASE PATH TO ENV ############################
import os
import sys

DIR_PATH = os.path.dirname(os.path.realpath(__file__))
BASE_PATH = os.path.realpath(os.path.join(DIR_PATH, '../'))
sys.path.append(BASE_PATH)
###############################################################################

import pytest
from data.test_data_pow import test_data_pow
from gt.pow_gt import pow_gt

x = test_data_pow.x
n = test_data_pow.n
x_n = [(x[i], n[i])for i in range(len(x))]
@pytest.mark.parametrize("x, n", x_n)
def test_pow(x, n):
    print("x:", x, "n:", n)
    val = 1
    for i in range(n):
        val = val * x

    val_gt = pow_gt(x, n)
    assert val == val_gt

if __name__ == "__main__":
    x = 2
    n = 4
    val = test_pow(x, n)
    print(val)
