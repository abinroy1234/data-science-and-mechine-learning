import matplotlib.pyplot as plt

x = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
y1 = [173, 153, 195, 147, 120, 144, 148, 109, 174, 130, 172, 131]
y2 = [189, 189, 105, 112, 173, 109, 151, 197, 174, 145, 177, 161]
y3 = [185, 185, 126, 134, 196, 153, 112, 133, 200, 145, 167, 110]

plt.scatter(x,y1, color="pink")
plt.scatter(x,y2, color="yellow")
plt.scatter(x,y3, color="blue")

plt.title("Sales Data",fontsize=25)
plt.xlabel("Month of Year",fontsize=18)
plt.ylabel("Sale of segment",fontsize=18)
plt.show()
