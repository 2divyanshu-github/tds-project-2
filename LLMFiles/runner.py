
import pandas as pd

df = pd.read_csv("demo-audio-data.csv")

# The first column is unnamed, so let's assume it's the first column (index 0)
# and its name might be the first value if no header is explicitly set.
# However, pandas often infers the first row as header if no 'header' argument is given.
# Let's re-read assuming no header and then use the cutoff.

df = pd.read_csv("demo-audio-data.csv", header=None)

# The cutoff value from the page is 33025
cutoff = 33025

# Filter numbers greater than the cutoff and sum them
filtered_sum = df[df[0] > cutoff][0].sum()

print(f"The sum of numbers greater than {cutoff} is: {filtered_sum}")
