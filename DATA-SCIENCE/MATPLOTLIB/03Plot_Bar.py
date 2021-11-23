import matplotlib.pyplot as pl

lst = ['oppo','one plus','poco','samsung','vivo','iphone']
price = [21,30,15,18,15,130]

clr = ['red','green','yellow','blue','black','pink']

pl.bar(lst,price,color=clr)
pl.xlabel('Mobile phone')
pl.ylabel('price ')
pl.title('Mobile phone average rates')
pl.grid(True)

pl.show()