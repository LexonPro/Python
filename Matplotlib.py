import matplotlib.pyplot as plt
import numpy as np   # (Some examples need data generation)

# -----------------------------
# BASIC PLOT
# -----------------------------
x = [1, 2, 3, 4]
y = [10, 20, 15, 25]

plt.plot(x, y)               # Output: Creates a simple line plot
plt.title("Basic Plot")      # Output: Adds title to the plot
plt.xlabel("X-Axis")         # Output: Labels X-axis
plt.ylabel("Y-Axis")         # Output: Labels Y-axis
plt.show()                   # Output: Displays the plot window

# -----------------------------
# MULTIPLE LINES
# -----------------------------
plt.plot(x, y)               # Output: First line
plt.plot(x, [5, 15, 10, 20]) # Output: Second line on same graph
plt.show()                   # Output: Shows both lines

# -----------------------------
# CHANGE LINE STYLE, MARKER, WIDTH
# -----------------------------
plt.plot(x, y, linestyle='--', marker='o', linewidth=2)
# Output: Dashed line with circular markers and thick width
plt.show()

# -----------------------------
# SCATTER PLOT
# -----------------------------
plt.scatter(x, y)            # Output: Scatter plot of points
plt.show()

# -----------------------------
# BAR CHART
# -----------------------------
plt.bar(x, y)                # Output: Vertical bar chart
plt.show()

plt.barh(x, y)               # Output: Horizontal bar chart
plt.show()

# -----------------------------
# HISTOGRAM
# -----------------------------
data = np.random.randn(1000)
plt.hist(data, bins=20)       # Output: Histogram showing distribution
plt.show()

# -----------------------------
# PIE CHART
# -----------------------------
sizes = [40, 30, 20, 10]
labels = ["A", "B", "C", "D"]
plt.pie(sizes, labels=labels, autopct='%1.1f%%')
# Output: Pie chart with percentage labels
plt.show()

# -----------------------------
# SUBPLOTS
# -----------------------------
fig, axs = plt.subplots(2, 2)
# Output: Creates 2x2 plot grid

axs[0,0].plot(x, y)           # Output: Line plot in top-left
axs[0,1].scatter(x, y)        # Output: Scatter plot in top-right
axs[1,0].bar(x, y)            # Output: Bar plot bottom-left
axs[1,1].hist(data)           # Output: Histogram bottom-right
plt.show()

# -----------------------------
# FIGURE SIZE
# -----------------------------
plt.figure(figsize=(8,4))     # Output: Creates wider figure
plt.plot(x, y)
plt.show()

# -----------------------------
# ADD GRID
# -----------------------------
plt.plot(x, y)
plt.grid(True)                # Output: Shows grid lines
plt.show()

# -----------------------------
# AXIS LIMITS
# -----------------------------
plt.plot(x, y)
plt.xlim(0, 5)                # Output: X-axis from 0 to 5
plt.ylim(0, 30)               # Output: Y-axis from 0 to 30
plt.show()

# -----------------------------
# LOG SCALE
# -----------------------------
plt.plot(x, y)
plt.yscale("log")             # Output: Logarithmic scale on Y-axis
plt.show()

# -----------------------------
# ADD LEGEND
# -----------------------------
plt.plot(x, y, label="Line 1")
plt.plot(x, [5,10,7,15], label="Line 2")
plt.legend()                  # Output: Adds legend box
plt.show()

# -----------------------------
# SAVE PLOT
# -----------------------------
plt.plot(x, y)
plt.savefig("plot.png")       # Output: Saves plot as 'plot.png'
plt.show()

# -----------------------------
# ANNOTATIONS
# -----------------------------
plt.plot(x, y)
plt.annotate("Peak", xy=(4,25), xytext=(3,26),
             arrowprops=dict(arrowstyle="->"))
# Output: Adds text + arrow
plt.show()

# -----------------------------
# FILL AREA
# -----------------------------
plt.fill_between(x, y, color='lightgray')
# Output: Shade region under line
plt.plot(x, y)
plt.show()

# -----------------------------
# STEM PLOT
# -----------------------------
plt.stem(x, y)               # Output: Vertical line markers
plt.show()

# -----------------------------
# BOX PLOT
# -----------------------------
plt.boxplot(data)            # Output: Box-and-whisker plot
plt.show()

# -----------------------------
# HEATMAP (IMSHOW)
# -----------------------------
matrix = np.random.rand(5,5)
plt.imshow(matrix, cmap='viridis')
plt.colorbar()                # Output: Adds color scale
plt.show()
