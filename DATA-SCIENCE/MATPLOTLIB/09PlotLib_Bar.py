from matplotlib import pyplot as pl 

x=[5,7,9]
y=[13,15,10]

x1=[6,8,10]
y1=[7,19,13]

pl.bar(x,y,align='center')
pl.bar(x1,y1,color='g',align='center')

pl.show()
