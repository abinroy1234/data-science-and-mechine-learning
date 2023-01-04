import matplotlib.pyplot as plt

data ={'Walking':25,'Cycling':40,'Bus':25,'Car':10}

mode = list(data.keys())
freq = list(data.values())

fig = plt.figure(figsize=(10,5))

plt.bar(mode,freq,color="green",width=0.1)

plt.title("Mode of transportation")
plt.ylabel("frequency")
plt.xlabel("Modes")
plt.show()
