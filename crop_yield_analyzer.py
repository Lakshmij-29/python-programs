
farm_data = {
    "Rice": [12, 4200],
    "Wheat": [8, 2800],
    "Maize": [10, 3500]
}

for crop, data in farm_data.items():
    area, production = data
    yield_per_acre = production / area
    print(crop, "-", round(yield_per_acre, 2), "kg/acre")

best_crop = max(
    farm_data,
    key=lambda crop: farm_data[crop][1] / farm_data[crop][0]
)

print("Highest Yield:", best_crop)
