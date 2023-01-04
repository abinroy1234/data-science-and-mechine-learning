import matplotlib.pyplot as plt

x=[2001,2002,2003,2004,2005,2006,2007]
y=[24000, 22500, 19700, 17500, 14500, 10000, 5800]

plt.plot(x,y,linestyle="dashdot",marker="*",color ="red",mfc="green",markersize=20)

plt.title("Deprecation")
plt.ylabel("Car Value")
plt.xlabel("Year")
plt.show()
