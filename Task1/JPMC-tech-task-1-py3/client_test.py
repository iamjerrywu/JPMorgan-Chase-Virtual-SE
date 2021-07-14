import unittest
from client3 import getDataPoint, getRatio

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
      self.assertEqual(getDataPoint(quote), (quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'], (quote['top_bid']['price'] + quote['top_ask']['price'])/2))


  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
      self.assertEqual(getDataPoint(quote), (quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'], (quote['top_bid']['price'] + quote['top_ask']['price'])/2))
  
  def test_getRatio_priceA_is_zero(self):
    prices = [
      [0, 129.85],
      [0, 90.74]
    ]
    """ ------------ Add the assertion below ------------ """
    for price_a, price_b in prices:
      self.assertEqual(getRatio(price_a, price_b), 0)
  
  def test_getRatio_priceB_is_zero(self):
    prices = [
      [68.58, 0],
      [119.24, 0]
    ]
    """ ------------ Add the assertion below ------------ """
    for price_a, price_b in prices:
      self.assertIsNone(getRatio(price_a, price_b))
  
  def test_getRatio_greater_than_one(self):
    prices = [
      [245.19, 98.52],
      [409.39, 199.87]
    ]
    """ ------------ Add the assertion below ------------ """
    for price_a, price_b in prices:
      self.assertGreater(getRatio(price_a, price_b), 1)
  
  def test_getRatio_less_than_one(self):
    prices = [
      [68.72, 119.45],
      [125.81, 682.13]
    ]
    """ ------------ Add the assertion below ------------ """
    for price_a, price_b in prices:
      self.assertLess(getRatio(price_a, price_b), 1)
  
  def test_getRatio_equal_to_one(self):
    prices = [
      [1095.32, 1095.32],
      [72.45, 72.45]
    ]
    """ ------------ Add the assertion below ------------ """
    for price_a, price_b in prices:
      self.assertEqual(getRatio(price_a, price_b), 1)    

if __name__ == '__main__':
    unittest.main()
