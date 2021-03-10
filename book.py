import pandas as pd 

class Order:
    """
    Creéation d'un ordre
    """
    
    def __init__(self, quantity, price,id, buy=True):
        """
        initialise l'objet ordre
        quantity : quantité de l'ordre (int)
        price : price de l'ordre (float)
        id : identifiant de l'ordre géré dans la classe book (int)
        buy : true veut dire achat et false veut dire vente (booleen)
        """
        self.quantity=quantity
        self.price = price
        self.buy=buy
        self.id = id



    

class Book:
    """
    Contient et exécute tout les ordres et fait l'affichage 

    """


    def __init__(self, name, buy_orders=[], sell_orders=[]):

        """
        initalise le book
        name : nom du book (string)
        buy_orders : liste qui contient les ordres d'achats
        sell_orders : liste qui contient les ordres de ventes
        id : initialise l'id à 0
        """
        self.name=name
        self.buy_orders=buy_orders
        self.sell_orders=sell_orders
        self.id=0

    
    def execute_orders(self):

        """
        Execute les ordres de ventes et d'achats possibles.
        Met à jour les quantités. 

        """

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

        """
        Insert un ordre d'achat dans la liste buy_orders
        Trie la liste dans l'odre des prix décroissants
        Print le book 
        id : on incrémente l'id de 1
        qty : quantite de l'odre d'achat (int)
        price : prix de l'odre d'achat (float)


        """

        self.id =self.id + 1
        self.buy_orders.append(Order(qty,price,self.id, True))
        self.buy_orders.sort(key=lambda x: x.price, reverse= True)
        print("--- Insert BUY " + str(qty) +"@"+ str(price) + " id= "+ str(self.id) +" on "+ self.name)
        self.execute_orders()
        self.print_book()

    def insert_sell(self,qty, price):

        """
        Insert un ordre de vente la liste sell_orders
        Trie la liste dans l'ordre des prix décroissants
        Print le book
        id : on incrémente l'id de 1
        qty : quantite de l'ordre de vente (int)
        price : prix de l'ordre de vente (float)

        """

        self.id =self.id + 1  
        self.sell_orders.append(Order(qty,price,self.id,False))
        self.sell_orders.sort(key=lambda x: x.price, reverse= True)
        print("--- Insert SELL " + str(qty) +"@"+ str(price) + " id= "+ str(self.id) + " on "+ self.name)
        self.execute_orders()
        self.print_book()
        
    def print_book(self):

        """
        Affichage du book avec data frame
        Direction : ordre buy ou sell
        Quantity : quantité de l'odre
        Price : price de l'odre
        id : id de l'ordre 
        """

        print("Book on " + self.name)
        liste = []
        for sell in self.sell_orders:
            liste.append(["SELL", str(sell.quantity), str(sell.price), str(sell.id)])
        for buy in self.buy_orders :
            liste.append(["BUY", str(buy.quantity), str(buy.price), str(buy.id)])
        df = pd.DataFrame(liste, columns=['Direction', 'Quantity', 'Price', 'id'])
        print(df)
        print( "------------------------------------------------------" )
    

