import galpynostatic
import matplotlib.pyplot as plt

greg = galpynostatic.model.GalvanostaticRegressor()
greg.fit([[4.0], [5.0]], [0.8, 0.9])
ax = greg.plot.render_map(clb_label="valor máximo del SOC")

ax.plot([-4, 1.75], [0, 0], ls="--", color="tab:gray")
ax.text(-3.8, 0.2, "(b)", color="tab:gray")

ax.plot([-4, 1.75], [-2, -2], ls="--", color="tab:gray")
ax.text(-3.8, -1.8, "(c)", color="tab:gray")

ax.scatter(-1, -1, marker="^", color="tab:blue")
ax.text(-1.07, -0.9, "A", color="tab:blue")

ax.scatter(1.5, 1, marker="v", color="tab:red")
ax.text(1.43, 0.7, "B", color="tab:red")

ax.text(-4.5, 2.5, "(a)")

plt.savefig("diagnosis-map.png", dpi=600)
