import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Load builtin dataset
df = sns.load_dataset("tips")     # Output: Loads the 'tips' dataset

# -----------------------------
# BASIC SEABORN STYLES
# -----------------------------
sns.set_style("darkgrid")         # Output: Background becomes dark grid
sns.set_palette("pastel")         # Output: Soft pastel colors everywhere

# -----------------------------
# LINE PLOT
# -----------------------------
sns.lineplot(x="total_bill", y="tip", data=df)
# Output: Smooth line chart connecting data trends
plt.show()

# -----------------------------
# SCATTER PLOT
# -----------------------------
sns.scatterplot(x="total_bill", y="tip", data=df)
# Output: Points showing relationship between bill & tip
plt.show()

# -----------------------------
# SCATTER WITH HUE & SIZE
# -----------------------------
sns.scatterplot(x="total_bill", y="tip", hue="time", size="size", data=df)
# Output: Colors by 'time', different sizes by 'size'
plt.show()

# -----------------------------
# BAR PLOT
# -----------------------------
sns.barplot(x="day", y="total_bill", data=df)
# Output: Bars showing average bill by day
plt.show()

# -----------------------------
# COUNT PLOT
# -----------------------------
sns.countplot(x="day", data=df)
# Output: Counts number of rows per category
plt.show()

# -----------------------------
# HISTOGRAM
# -----------------------------
sns.histplot(df['total_bill'])
# Output: Histogram showing distribution of total_bill
plt.show()

# -----------------------------
# DENSITY PLOT (KDE)
# -----------------------------
sns.kdeplot(df['total_bill'])
# Output: Smooth probability density curve
plt.show()

# -----------------------------
# DISTPLOT (Histogram + KDE)
# -----------------------------
sns.displot(df['total_bill'], kde=True)
# Output: Histogram + smooth curve together
plt.show()

# -----------------------------
# BOX PLOT
# -----------------------------
sns.boxplot(x="day", y="total_bill", data=df)
# Output: Shows median, quartiles, and outliers
plt.show()

# -----------------------------
# VIOLIN PLOT
# -----------------------------
sns.violinplot(x="day", y="total_bill", data=df)
# Output: Smoothed distribution shape + box inside
plt.show()

# -----------------------------
# SWARM PLOT
# -----------------------------
sns.swarmplot(x="day", y="total_bill", data=df)
# Output: Points spread to avoid overlap (slow for large data)
plt.show()

# -----------------------------
# PAIR PLOT
# -----------------------------
sns.pairplot(df)
# Output: Plots relationships for all numeric columns
plt.show()

# -----------------------------
# HEATMAP
# -----------------------------
corr = df.corr(numeric_only=True)   # Output: Correlation matrix
sns.heatmap(corr, annot=True)
# Output: Heatmap with numbers inside cells
plt.show()

# -----------------------------
# JOINT PLOT
# -----------------------------
sns.jointplot(x="total_bill", y="tip", data=df, kind="scatter")
# Output: Scatter + histograms on sides
plt.show()

# -----------------------------
# JOINT PLOT KDE
# -----------------------------
sns.jointplot(x="total_bill", y="tip", data=df, kind="kde")
# Output: Smooth bivariate density plot
plt.show()

# -----------------------------
# REGRESSION PLOT
# -----------------------------
sns.regplot(x="total_bill", y="tip", data=df)
# Output: Scatter + best-fit regression line
plt.show()

# -----------------------------
# LLM PLOT (Lowess curve)
# -----------------------------
sns.lmplot(x="total_bill", y="tip", hue="sex", data=df)
# Output: Regression line for each category (Male/Female)
plt.show()

# -----------------------------
# CATPLOT (General Purpose)
# -----------------------------
sns.catplot(x="day", y="total_bill", kind="bar", data=df)
# Output: Flexible categorical plot (bar here)
plt.show()

# -----------------------------
# STRIP PLOT
# -----------------------------
sns.stripplot(x="day", y="total_bill", data=df)
# Output: Simple scatter for categories
plt.show()

# -----------------------------
# BOXEN PLOT
# -----------------------------
sns.boxenplot(x="day", y="total_bill", data=df)
# Output: Enhanced boxplot for large datasets
plt.show()

# -----------------------------
# CLUSTermap
# -----------------------------
sns.clustermap(corr, annot=True)
# Output: Dendrogram + heatmap clustering similar columns
plt.show()

# -----------------------------
# STYLE + CONTEXT
# -----------------------------
sns.set_style("whitegrid")        # Output: White background with grid
sns.set_context("talk")           # Output: Larger labels for presentations
sns.barplot(x="day", y="tip", data=df)
plt.show()

# -----------------------------
# COLOR PALETTES
# -----------------------------
sns.color_palette("coolwarm", 5)  # Output: Returns list of 5 colors
sns.palplot(sns.color_palette("coolwarm", 5))
# Output: Shows palette visually
plt.show()

# -----------------------------
# SAVE PLOT
# -----------------------------
plt.figure()
sns.scatterplot(x="total_bill", y="tip", data=df)
plt.savefig("seaborn_plot.png")   # Output: Saves current figure
plt.show()
