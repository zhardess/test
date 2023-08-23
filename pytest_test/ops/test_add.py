############################# ADD BASE PATH TO ENV ############################
import os
import sys

DIR_PATH = os.path.dirname(os.path.realpath(__file__))
BASE_PATH = os.path.realpath(os.path.join(DIR_PATH, '../'))
sys.path.append(BASE_PATH)
###############################################################################

import pytest
from data.test_data_add import test_data_add
from gt.add_gt import add_gt

l = test_data_add.x
print(len(l))

@pytest.mark.parametrize("src", l)
def test_pow(src):
    val = 0
    for i in range(len(src)):
        val += src[i]

    val_gt = add_gt(src)
    assert val == val_gt
