class ShoppingList:
    def __init__(self,shopping_list):
        self.shopping_list = shopping_list
       

    def get_total_price(self):
        total_price = 0
        for price in self.shopping_list.values():
            total_price += price
        return total_price

""" 
s1 = ShoppingList({"apple":10,"banana":20,"orange":30})
print(s1.get_total_price()) """
