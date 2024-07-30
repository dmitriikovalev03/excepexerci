import pandas as pd

# Sample data for two entities' top holdings
data1 = {
    'Ticker': ['AAPL', 'MSFT', 'AMZN', 'GOOGL', 'FB'],
    'Shares': [1000, 2000, 1500, 500, 800]
}

data2 = {
    'Ticker': ['AAPL', 'MSFT', 'AMZN', 'GOOGL', 'TSLA'],
    'Shares': [1200, 1800, 1600, 600, 700]
}

df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)

# Set 'Ticker' column as index (if not already set)
df1.set_index('Ticker', inplace=True)
df2.set_index('Ticker', inplace=True)

print("DataFrame 1:")
print(df1)

print("\nDataFrame 2:")
print(df2)
