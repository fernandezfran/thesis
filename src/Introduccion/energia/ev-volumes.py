import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({"font.size": 12})

years = np.arange(2014, 2024)
sales = 1_000 * np.array([320, 543, 791, 1262, 2082, 2276, 3245, 6768, 10532, 14000])

print(np.diff(sales) / sales[1:])

fig, ax = plt.subplots()

ax.bar(years, sales, width=0.6)

ax.set_xticks(years)
ax.set_xlabel("Año")
ax.set_ylabel("Ventas anuales de vehículos eléctricos")

fig.tight_layout()
fig.savefig("ev-volumes.png", dpi=600)
plt.show()
