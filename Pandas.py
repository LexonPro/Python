# ===================== PANDAS ALL-IN-ONE CHEATSHEET WITH OUTPUTS =====================

import pandas as pd
import numpy as np

# Sample Series & DataFrame
s = pd.Series([10, 20, 30], index=['a','b','c'])

df = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [10, 20, 30],
    'C': ['x', 'y', 'z']
})

# -------------------- CREATE --------------------
pd.Series([1,2,3])                       # → 0 1 2
pd.DataFrame({'A':[1,2], 'B':[3,4]})      # → 2×2 table

pd.read_csv("file.csv")                  # → read CSV file
pd.DataFrame(np.random.randn(3,3))       # → random 3x3 DF

# -------------------- INFO --------------------
df.head()                                # → first 5 rows
df.tail()                                # → last 5 rows
df.info()                                # → column info
df.describe()                            # → statistics summary
df.shape                                 # → (3,3)
df.columns                               # → Index(['A','B','C'])
df.index                                 # → Index([0,1,2])

# -------------------- SELECTING DATA --------------------
df['A']                                  # → column A (Series)
df[['A','B']]                             # → multiple columns
df.loc[0]                                # → row with index 0
df.loc[0,'A']                            # → 1
df.iloc[1]                               # → second row
df.iloc[:,1]                             # → column B

# Boolean selection
df[df['A'] > 1]                          # → rows where A > 1
df[(df['A'] > 1) & (df['B'] < 30)]       # → filtered rows

# -------------------- ADD / UPDATE COLUMNS --------------------
df['D'] = df['A'] + df['B']              # → new column D = A+B
df['E'] = np.where(df['A'] > 1, 'High', 'Low')  # → conditional column

# -------------------- DELETE COLUMNS --------------------
df.drop('C', axis=1)                     # → C column removed
df.drop([0,2], axis=0)                   # → delete rows 0 & 2

# -------------------- SORTING --------------------
df.sort_values('B')                      # → sort by column B
df.sort_values(['A','B'], ascending=[1,0])  # → multiple column sort

# -------------------- AGGREGATIONS --------------------
df['A'].sum()                            # → sum of A
df['A'].mean()                           # → mean of A
df['B'].min()                            # → 10
df['B'].max()                            # → 30
df['B'].count()                          # → 3

df.agg({'A':'sum', 'B':'mean'})          # → apply multiple functions

# -------------------- GROUPBY --------------------
df.groupby('C')['A'].sum()               # → sum of A grouped by C
df.groupby('C').agg({'A':'mean','B':'sum'})  # → multiple agg

# -------------------- MERGING / JOINING --------------------
df1 = pd.DataFrame({'key':[1,2],'val1':[10,20]})
df2 = pd.DataFrame({'key':[1,2],'val2':[100,200]})

pd.merge(df1, df2, on='key')             # → merged table on 'key'
pd.concat([df1, df2], axis=0)            # → vertical stack
pd.concat([df1, df2], axis=1)            # → horizontal stack

# -------------------- FILLING / DROPPING NA --------------------
df3 = pd.DataFrame({'A':[1,np.nan,3], 'B':[4,5,np.nan]})

df3.isna()                               # → check NaN
df3.fillna(0)                            # → replace NaN with 0
df3.dropna()                             # → drop rows with NaN
df3.fillna(df3.mean())                   # → fill with column mean

# -------------------- APPLY / LAMBDA --------------------
df['A'].apply(lambda x: x*10)            # → multiply A by 10
df.apply(np.sum)                         # → column-wise sum

# -------------------- STRING OPERATIONS --------------------
df['C'].str.upper()                      # → 'X','Y','Z'
df['C'].str.contains('x')                # → boolean mask

# -------------------- VALUE COUNTS --------------------
df['C'].value_counts()                   # → counts per value

# -------------------- REPLACE --------------------
df['C'].replace({'x':'new_x'})           # → replace values

# -------------------- RENAME --------------------
df.rename(columns={'A':'Alpha'})         # → rename column A→Alpha

# -------------------- RESET & SET INDEX --------------------
df.reset_index()                         # → reset index to 0,1,2
df.set_index('A')                        # → set column A as index

# -------------------- EXPORT --------------------
# df.to_csv("file.csv")                  # → save to CSV
# df.to_excel("file.xlsx")               # → save to Excel
# df.to_json("file.json")                # → save to JSON

# -------------------- READ --------------------
# pd.read_excel("file.xlsx")             # → load Excel
# pd.read_json("file.json")              # → load JSON

# -------------------- PIVOT TABLE --------------------
df.pivot_table(values='B', index='C', aggfunc='mean')  # → pivot summary

# -------------------- UNIQUE & DUPLICATES --------------------
df['C'].unique()                         # → ['x','y','z']
df['C'].nunique()                        # → 3
df.duplicated()                          # → check for duplicates
df.drop_duplicates()                     # → remove duplicate rows

# ===================== END OF PANDAS CHEATSHEET =====================
