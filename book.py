class Order:
    def __init__(self, quantity, price,id, buy=True):
        self.quantity=quantity
        self.price = price
        self.buy=buy
        self.id = id



    

class Book:
    def __init__(self, name, buy_orders=[], sell_orders=[]):
        self.name=name
        self.buy_orders=buy_orders
        self.sell_orders=sell_orders
        self.id=0

    
    def execute_orders(self):
        for sell in self.sell_orders[:] :
            for buy in self.buy_orders[:] :
                if sell.price <= buy.price:
                    if sell.quantity >= buy.quantity:
                        print( "Execute " + str(buy.quantity) + " at " + str(buy.price) + " on " + self.name)
                        sell.quantity = sell.quantity - buy.quantity
                        buy.quantity = 0
                    else:
                        print( "Execute " + str(sell.quantity) + " at " + str(buy.price) + " on " + self.name)
                        buy.quantity = buy.quantity - sell.quantity
                        sell.quantity = 0
                    if sell.quantity == 0:
                        self.sell_orders.remove(sell)
                        break;  
                    if buy.quantity == 0:
                        self.buy_orders.remove(buy)

    def insert_buy(self,qty, price):
        self.id =self.id + 1
        self.buy_orders.append(Order(qty,price,self.id, True))
        self.buy_orders.sort(key=lambda x: x.price, reverse= True)
        print("--- Insert BUY " + str(qty) +"@"+ str(price) + " id= "+ str(self.id) +" on "+ self.name)
        self.execute_orders()
        self.print_book()

    def insert_sell(self,qty, price):
        self.id =self.id + 1  
        self.sell_orders.append(Order(qty,price,self.id,False))
        self.sell_orders.sort(key=lambda x: x.price, reverse= True)
        print("--- Insert SELL " + str(qty) +"@"+ str(price) + " id= "+ str(self.id) + " on "+ self.name)
        self.execute_orders()
        self.print_book()
        
    def print_book(self):
        print("Book on " + self.name)
        for sell in self.sell_orders:
            print(" SELL " + str(sell.quantity)  +"@"+ str(sell.price) + " id= "+ str(sell.id))
        for buy in self.buy_orders :
            print(" BUY " + str(buy.quantity)  +"@"+ str(buy.price) + " id= "+ str(buy.id))
        print( "------------------------------------------------------" )
    
    

