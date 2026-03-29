import yfinance as yf
import plotly.graph_objects as go

# Download stock data
ticker = 'AAPL'
data = yf.download(ticker, period='6mo', interval='1d')

# Candlestick chart
fig = go.Figure(data=[go.Candlestick(x=data.index,
                open=data['Open'], high=data['High'],
                low=data['Low'], close=data['Close'])])
fig.update_layout(title=f'{ticker} Candlestick Chart')
fig.show()
