class BikeShop:
    def __init__(self,stock):
        self.stock = stock
    def displaybike(self):
        print("TOTAL BIKES:",self.stock)
    def rentforbike(self,quan):

        if quan <=0:
            print("ENTER THE POSITIVE VALUE OR GREATER THAN ZERO")
        elif quan>self.stock:
            print("ENTER THE VALUE LESS THAN STOCK")
        else:
            self.stock = self.stock-quan
            print("TOTAL PRICE",quan*100)
            print("TOTAL STOCK",self.stock)

while True:
    obj=BikeShop(100)
    uc = int(input('''
    1 Display Stocks
    2 Rent A Bike
    3 Exit
    '''))

    if uc == 1:
        obj.displaybike()
    elif uc == 2:
        n = int(input("ENTER THE QUANTITY:"))
        obj.rentforbike(n)
    else:
        break;
