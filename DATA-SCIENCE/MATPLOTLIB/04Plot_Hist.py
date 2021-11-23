import matplotlib.pyplot as pl

lst = ['oppo','one plus','poco','samsung','vivo','iphone']
price = [21,30,15,18,15,30]

pl.hist(price,bins=15,color='green')
pl.grid()
pl.show()