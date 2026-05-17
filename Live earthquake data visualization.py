# earthquake_visualizer.py

import requests
import pandas as pd
import plotly.express as px

# Fetch live earthquake data
url = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_day.geojson"
data = requests.get(url).json()

# Extract features
features = data["features"]

earthquakes = []

for feature in features:
    props = feature["properties"]
    coords = feature["geometry"]["coordinates"]

    earthquakes.append({
        "Place": props["place"],
        "Magnitude": props["mag"],
        "Time": props["time"],
        "Longitude": coords[0],
        "Latitude": coords[1],
        "Depth": coords[2]
    })

df = pd.DataFrame(earthquakes)

# Create interactive map
fig = px.scatter_geo(
    df,
    lat="Latitude",
    lon="Longitude",
    size="Magnitude",
    color="Depth",
    hover_name="Place",
    projection="natural earth",
    title="Live Earthquakes Around the World"
)

fig.show()
