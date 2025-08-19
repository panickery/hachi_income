from collections.abc import Callable
import pytest
import hachi_income.income_utils as hutils

def test_str_hash() :
    print(hutils.get_random_id())