import pandas as pd

data = {
    'Name': ['nithin', 'nithya', 'nikhil', 'nishanth', 'nihal'],
    'Subject': ['be', 'msc', 'bca', 'mtech', 'bsc'],
    'Marks': [85.5, 80.5, 95.5, 75.5, 65.5]
}

df = pd.DataFrame(data)

print(df)
print(df.head(2))
print(df.tail(2))

# Display First Few Rows using head()
# head() displays the first 5 rows by default.
# Useful when working with large datasets.