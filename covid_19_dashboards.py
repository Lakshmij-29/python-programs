import pandas as pd
import plotly.express as px

# Load COVID data from URL
url = "https://covid.ourworldindata.org/data/owid-covid-data.csv"
data = pd.read_csv(url)
latest_data = data[data['date'] == data['date'].max()]

# Interactive Bar Chart for top 10 countries by cases
top10 = latest_data.nlargest(10, 'total_cases')
fig = px.bar(top10, x='location', y='total_cases', title="Top 10 Countries by COVID Cases")
fig.show()
