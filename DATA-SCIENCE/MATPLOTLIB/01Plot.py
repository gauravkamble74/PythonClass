import matplotlib.pyplot as pl

lst = ['flying beast','stocks trader','anuj bhaiya','loi liang yang','aib','sony']
subs = [7,.5,19,7,10,15]

pl.plot(lst,subs,color='red',linestyle='--')
pl.xlabel("channel name")
pl.ylabel("subscribers count")
pl.ylim(2,20)
pl.title("Youtube survey 2021")

pl.show()