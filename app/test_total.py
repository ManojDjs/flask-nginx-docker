import pytest
import json
from app import app
from app.large_number_addition import findSum
import unittest
def test_sum_large_number():
    assert findSum("50000000","60000000") == "110000000"


def test_index_route():
    response = app.hello_world()
    print(response)
    assert response == "Hello, World - From a container!"
