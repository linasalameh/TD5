class Order:
    def __init__(self, quantity, price, buy=True):
        self.quantity=quantity
        self.price = price
        self.buy=buy

class Book:
    def __init__(self, name, buy_orders=[], sell_orders=[]):
        self.name=name
        self.buy_orders=buy_orders
        self.sell_orders=sell_orders


