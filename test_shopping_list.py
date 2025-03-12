import unittest
from shopping_list import ShoppingList
class TestShoppingList(unittest.TestCase):
    def setUp(self):
        self.s1 = ShoppingList({"apple":10,"banana":20,"orange":30})
    def test_get_totalPrice(self):
      
        self.assertEqual(self.s1.get_total_price(),60)
    
    def test_get_totalPrice2(self):
        
        self.assertEqual(self.s1.get_total_price(),90)
  