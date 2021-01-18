import unittest
import investplus


class TestClass(unittest.TestCase):

    """Test case docstring."""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_stocks(self):
        url = "https://www.investing.com/equities/apple-computer-inc-balance-sheet"
        balance_sheet = investplus.get_stock_balance_sheet(url)
