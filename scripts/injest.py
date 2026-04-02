import pandas as pd

# load sample dataset (keep small)
orders = pd.read_csv('../data/orders.csv')

print("Preview:")
print(orders.head())

print("\nInfo:")
print(orders.info())