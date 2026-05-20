# stock_animation.py

import yfinance as yf
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

stock = "AAPL"

data = yf.download(stock, period="1mo", interval="1d")

fig, ax = plt.subplots()

x_data = []
y_data = []

def animate(i):
    if i < len(data):
        x_data.append(i)
        y_data.append(data["Close"].iloc[i])

        ax.clear()
        ax.plot(x_data, y_data)
        ax.set_title(f"{stock} Live Trend")
        ax.set_xlabel("Day")
        ax.set_ylabel("Price")

ani = FuncAnimation(fig, animate, interval=500)

plt.show()
