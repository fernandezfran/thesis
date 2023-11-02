import pandas as pd

files = [
    "lithium_battery.csv",
    "lithium_battery_fast-charging.csv",
    "lithium_battery_Si-anodes.csv",
]

print("archivo: % promedio de incremento anual")
for file in files:
    df = pd.read_csv(file)

    df = df.sort_values(by="year", ascending=True)

    df["pct_change"] = df["npub"].pct_change()

    print(f"{file}: {df['pct_change'][10:].mean():.2f}")
