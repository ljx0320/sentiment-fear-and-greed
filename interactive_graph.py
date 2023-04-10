import pandas as pd
import plotly.express as px
from plotly.subplots import make_subplots
# Check this doc https://plotly.com/python/facet-plots/

# Fear and greed plot
fear_greed_csv_file = "datasets/fear-greed-2020-2023.csv"
fear_greed_df = pd.read_csv(fear_greed_csv_file)
fear_greed_fig = px.line(fear_greed_df, x='Date', y='Fear Greed', title='Fear&Greed')

# Market momentum plot
market_momentum_csv_file = "datasets/market-momentum-2020-2023.csv"
market_momentum_df = pd.read_csv(market_momentum_csv_file)
market_momentum_fig = px.line(market_momentum_df, x='Date', y='Market Momentum', title='Market Momentum')

# Stock Price Strength plot
stock_price_strength_csv_file = "datasets/stock-price-strength-2020-2023.csv"
stock_price_strength_df = pd.read_csv(stock_price_strength_csv_file)
stock_price_strength_fig = px.line(stock_price_strength_df, x='Date', y='Stock Price Strength', title='Stock Price Strength')

# Stock Price Breadth plot
stock_price_breadth_csv_file = "datasets/stock-price-breadth-2020-2023.csv"
stock_price_breadth_df = pd.read_csv(stock_price_breadth_csv_file)
stock_price_breadth_fig = px.line(stock_price_breadth_df, x='Date', y='Stock Price Breadth', title='Stock Price Breadth')

# Put and Call Options plot
put_call_csv_file = "datasets/put-and-call-options-2020-2023.csv"
put_call_df = pd.read_csv(put_call_csv_file)
put_call_fig = px.line(put_call_df, x='Date', y='Put and Call Options', title='Put and Call Options')

# Market Volatility plot
market_volatility_csv_file = "datasets/market-volatility-2020-2023.csv"
market_volatility_df = pd.read_csv(market_volatility_csv_file)
market_volatility_fig = px.line(market_volatility_df, x='Date', y='Market Volatility', title='Market Volatility')

# Market Volatility plot
safe_haven_demand_csv_file = "datasets/safe-haven-demand-2020-2023.csv"
safe_haven_demand_df = pd.read_csv(safe_haven_demand_csv_file)
safe_haven_demand_fig = px.line(safe_haven_demand_df, x='Date', y='Safe Haven Demand', title='Safe Haven Demand')

# Safe Haven Demand plot
safe_haven_demand_csv_file = "datasets/safe-haven-demand-2020-2023.csv"
safe_haven_demand_df = pd.read_csv(safe_haven_demand_csv_file)
safe_haven_demand_fig = px.line(safe_haven_demand_df, x='Date', y='Safe Haven Demand', title='Safe Haven Demand')

# Junk Bond Demand plot
junk_bond_demand_csv_file = "datasets/junk-bond-demand-2020-2023.csv"
junk_bond_demand_df = pd.read_csv(junk_bond_demand_csv_file)
junk_bond_demand_fig = px.line(junk_bond_demand_df, x='Date', y='Junk Bond Demand', title='Junk Bond Demand')

# Create a grid of subplots with 1 row and 2 columns
fig = make_subplots(rows=3, cols=3)

# Add each Plotly figure to a subplot in the grid
fig.add_trace(fear_greed_fig.data[0], row=1, col=1)
fig.add_trace(market_momentum_fig.data[0], row=1, col=2)
fig.add_trace(stock_price_strength_fig.data[0], row=1, col=3)
fig.add_trace(stock_price_breadth_fig.data[0], row=2, col=1)
fig.add_trace(put_call_fig.data[0], row=2, col=2)
fig.add_trace(market_volatility_fig.data[0], row=2, col=3)
fig.add_trace(safe_haven_demand_fig.data[0], row=3, col=1)
fig.add_trace(junk_bond_demand_fig.data[0], row=3, col=2)

# Update the layout of the grid
fig.update_layout(title='Fear and Greed Index')

# Show the Plotly figure
fig.show()
