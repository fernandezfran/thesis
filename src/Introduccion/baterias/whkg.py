import matplotlib.pyplot as plt

for year, whkg in [
    (1992, 81),
    (1995, 111),
    (1996, 122),
    (1998, 141),
    (2000, 160),
    (2001, 166),
    (2002, 171),
    (2005, 212),
    (2008, 227),
    (2012, 263),
    (2015, 301),
    (2023, 360),
]:
    if year == 1992:
        x, y = 1992, 200
        plt.text(x, y, "Sony")
        plt.arrow(x + 1, y - 5, -0.85, -100, fc="k", head_width=0.5, head_length=5)
    elif year == 2023:
        x, y = 2019, 200
        plt.text(2019, 200, "WeLion")
        plt.arrow(x + 2, y + 15, 1.85, 130, fc="k", head_width=0.5, head_length=5)

    plt.scatter(year, whkg, c="tab:blue")

plt.xticks(range(1990, 2026, 5))
plt.xlabel("Año")
plt.ylabel("Densidad de energía (Wh/kg)")
plt.ylim((0, 400))

plt.savefig("whkg.png", dpi=600)
