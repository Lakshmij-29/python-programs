
energy = {
    "Solar": 450,
    "Wind": 620,
    "Hydro": 380,
    "Biomass": 150
}

total = sum(energy.values())
share = energy["Solar"] / total * 100

print("Total Energy:", total, "MWh")
print("Solar Contribution:", round(share, 2), "%")
print("Leading Source:", max(energy, key=energy.get))

for source, output in energy.items():
    print(source, "-", output, "MWh")
