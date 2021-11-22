class Shop:
    city = 'Nagpur'

    def shopInfo(self):
        print('Shop name ',self.shop_cat)
        print('Shop city ',self.city)
        print('Shop owner ',self.owner)
    

parvati = Shop()
parvati.shop_cat = 'Fertilizers'
parvati.owner = 'Sunil'
parvati.offers = 'No'

parvati.shopInfo()
