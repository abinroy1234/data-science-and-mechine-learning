import matplotlib.pyplot as plt

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

x1 = ['mon','tue','wed','thu','fri']
y1 = [100,200,150,400,300]
y2 = [50,100,300,250,300]

fig.suptitle("Depreciation",fontsize=25)
plt.subplot(1,2,1)
plt.title(label ="data1",loc="right")
plt.subplot(1,2,2)
plt.title(label ="data2",loc="center")

l1 = ax1.plot(x1,y1,linestyle="dashdot",color="yellow",marker="h",mfc="green",mec="red")
l2 = ax2.plot(x1,y2,linestyle="dashed",color="cyan",marker="D",mfc="orange",mec="blue")

ax1.set_xlabel("date")
ax1.set_ylabel("saledata1")
ax2.set_xlabel("date")
ax2.set_ylabel("saledata2")
plt.show()
