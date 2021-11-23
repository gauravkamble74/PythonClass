from matplotlib import pyplot as pl

lst = ['flying beast','stocks trader','anuj bhaiya','loi liang yang','aib','sony']
subs = [7,5,19,7,10,15]

pl.plot(lst,subs,color='g',linestyle=':')
pl.xlabel('channel name')
pl.ylabel('subs count')
pl.ylim(2,20)
pl.title('Youtube survey')
pl.grid(True)
pl.scatter(lst,subs)
pl.legend(lst)

pl.show()
