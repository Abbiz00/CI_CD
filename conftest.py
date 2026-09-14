#%%
import pytest


@pytest.fixture
def test_numbers():
    return [2, 5, 10, -3]


@pytest.fixture
def test_pairs():
    return [(2, 3), (5, 5), (-1, 1), (0, 100)]