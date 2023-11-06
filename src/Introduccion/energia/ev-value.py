import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

plt.rcParams.update({"font.size": 12})

fig, ax = plt.subplots()

for f, l in zip(
    [f"{v}-value.csv" for v in ("ev", "combustion")],
    ["eléctrico", "a combustión interna"],
):
    df = pd.read_csv(f)

    cheby = np.polynomial.chebyshev.Chebyshev.fit(df.year, df.cost, deg=4)

    ax.plot(df.year, cheby(df.year), lw=2, label=l)

ax.set_xticks(range(2016, 2031, 2))
ax.set_xlabel("Año")
ax.set_ylim((0, 45000))
ax.set_ylabel("Costo de vehículos medianos (USD$)")

ax.legend(title="Vehículo")

fig.tight_layout()
fig.savefig("ev-value.png", dpi=600)
plt.show()
