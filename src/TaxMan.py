class TaxMan:
    def __init__(self,items,percent):
        self.items = items
        self.sales = percent
        self.__total = 0
    def calc_total(self):
        self.__total = sum(list(map(lambda p: p['price'] * (1+ float(self.sales[:-1])/100),self.items)))
    def get_total(self):
        return self.__total
        