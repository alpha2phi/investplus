import unittest

import investplus


class TestClass(unittest.TestCase):

    """Test case docstring."""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_stocks(self):
        investplus.get_stock()
