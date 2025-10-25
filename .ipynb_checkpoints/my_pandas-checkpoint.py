# ============================================================
# 📘 PANDAS NOTES — DATAFRAMES, FILE HANDLING, AND STATISTICS
# ============================================================

import pandas as pd
import numpy as np
from statistics import mode

# ------------------------------------------------------------
# 1️⃣  Creating a DataFrame from a Python dictionary
# ------------------------------------------------------------

mydataset = {
    'cars': ['BMW', 'Volvo', 'Ford'],
    'ratings': [4, 4, 5]
}

myFormattedDataset = pd.DataFrame(mydataset)
print("Basic DataFrame:\n", myFormattedDataset, "\n")

# Accessing a specific row using .loc
print("Row at index 0:\n", myFormattedDataset.loc[0], "\n")


# ------------------------------------------------------------
# 2️⃣  Reading data from files (CSV / JSON)
# ------------------------------------------------------------

# Note: Make sure './static/data.csv' and './static/data2.json' exist
dfcsv = pd.read_csv('./static/data.csv')
dfjson = pd.read_json('./static/data2.json')

# Print the entire dataframe (to_string() prevents truncation)
# print(dfcsv.to_string())
# print(dfjson.to_string())


# ------------------------------------------------------------
# 3️⃣  Creating a DataFrame from a nested dictionary
# ------------------------------------------------------------

data = {
    "Duration": {
        "0": 60, "1": 60, "2": 60, "3": 45, "4": 45, "5": 60
    },
    "Pulse": {
        "0": 110, "1": 117, "2": 103, "3": 109, "4": 117, "5": 102
    },
    "Maxpulse": {
        "0": 130, "1": 145, "2": 135, "3": 175, "4": 148, "5": 127
    },
    "Calories": {
        "0": 409.1, "1": 479.0, "2": 340.0, "3": 282.4, "4": 406.0, "5": 300.5
    }
}

dfdict = pd.DataFrame(data)
print("Dictionary DataFrame:\n", dfdict.to_string(), "\n")


# ------------------------------------------------------------
# 4️⃣  Viewing top and bottom records
# ------------------------------------------------------------

print("First 2 rows:\n", dfdict.head(2), "\n")  # first n rows
print("Last 2 rows:\n", dfdict.tail(2), "\n")   # last n rows


# ------------------------------------------------------------
# 5️⃣  DataFrame info (structure, types, non-null counts)
# ------------------------------------------------------------

print("DataFrame Info:\n")
print(dfdict.info(), "\n")


# ------------------------------------------------------------
# 6️⃣  Handling Missing Data (NaN)
# ------------------------------------------------------------

# Drop rows with missing values
newdfcsv = dfcsv.dropna()
print("After dropping rows with NaN values:\n", newdfcsv.to_string(), "\n")

# Fill missing values with a constant value
dfcsv.fillna(130, inplace=True)
print("After filling NaN with 130:\n", dfcsv.to_string(), "\n")


# 7️⃣  Basic Statistical Operations (PANDAS Methods)
# ------------------------------------------------------------

print("===== Basic Statistics (Using Pandas) =====")

# Mean → Average of a column
print("Mean of 'Calories':", dfdict["Calories"].mean())

# Median → Middle value of sorted column
print("Median of 'Calories':", dfdict["Calories"].median())

# Mode → Most frequent value(s)
# Returns a Series, so we take [0] for the first mode value
print("Mode of 'Calories':", dfdict["Calories"].mode()[0], "\n")


# ------------------------------------------------------------
# 8️⃣  Descriptive Statistics Summary
# ------------------------------------------------------------
# describe() gives count, mean, std, min, max, and quartiles

print("Summary Statistics for all numeric columns:\n")
print(dfdict.describe(), "\n")

# Using numpy (alternative)
print("Mean (NumPy):", np.mean(dfdict["Pulse"]))
print("Median (NumPy):", np.median(dfdict["Pulse"]), "\n")

# Using Python statistics library (for single lists)
calories_mode = mode(list(dfdict["Calories"]))
print("Mode (statistics library):", calories_mode, "\n")


# ------------------------------------------------------------
# ✅ Quick Summary
# ------------------------------------------------------------
# .DataFrame()     → Create a DataFrame
# .loc[]           → Access specific rows
# .read_csv()      → Read CSV file
# .read_json()     → Read JSON file
# .head(n)         → Show first n rows
# .tail(n)         → Show last n rows
# .info()          → Show structure info
# .dropna()        → Remove missing rows
# .fillna(value)   → Replace missing values
# .mean()          → Average of column
# .median()        → Middle value
# .mode()          → Most frequent value

# ============================================================
# End of Notes
# ============================================================
