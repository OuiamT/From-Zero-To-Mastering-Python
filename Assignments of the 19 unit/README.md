# 🐼 Pandas Basics:
This document introduces the **pandas package** and covers the some common operations used when working with tabular data such as **CSV files**.
## Series vs DataFrame:
### 📌 Series:
Is a one-dimensional data structure, similar to a column in a table and holds a single data type.
```
import pandas as pd
s = pd.Series([10, 20, 30])
```
### 📌 DataFrame:
Is a two-dimensional data structure, similar to a table and can contain different data types.
```
df = pd.DataFrame({ "name": ["Ali", "Sara"],
                    "age": [20, 25]})
```
## Reading a CSV File:
To load data from a CSV file:
```
import pandas as pd
df = pd.read_csv("data.csv")
```
This creates a **DataFrame** from the **CSV file.**
## Saving Data to a CSV File:
To save a **DataFrame** as a **CSV file**:
```
df.to_csv("output.csv")
```
