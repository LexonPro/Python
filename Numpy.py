# ---------------------------
# 1. Import NumPy
# ---------------------------
import numpy as np   # import numpy

# ---------------------------
# 2. Creating Arrays
# ---------------------------
np.array([1, 2, 3])               # create 1D array
np.array([[1, 2], [3, 4]])        # create 2D array
np.zeros(5)                       # array of zeros
np.ones((2, 3))                   # array of ones
np.full((2, 2), 7)                # constant array
np.eye(3)                         # identity matrix
np.arange(0, 10, 2)               # range with step size
np.linspace(0, 1, 5)              # evenly spaced values

# ---------------------------
# 3. Array Attributes
# ---------------------------
a.shape                           # rows, columns
a.size                            # total number of elements
a.ndim                            # number of dimensions

# ---------------------------
# 4. Reshaping Arrays
# ---------------------------
a.reshape(3, 2)                   # reshape array
a.ravel()                         # flatten to 1D
a.flatten()                       # also flatten

# ---------------------------
# 5. Indexing & Slicing
# ---------------------------
a[0]                              # first element
a[-1]                             # last element
a[1:4]                            # slicing
a[:, 1]                           # all rows, column 1
a[1, :]                           # row 1
a[0:2, 1:3]                       # submatrix

# ---------------------------
# 6. Boolean Masking
# ---------------------------
a[a > 5]                          # filter values > 5
a[(a % 2 == 0)]                   # even values

# ---------------------------
# 7. Mathematical Operations
# ---------------------------
a + b                             # addition
a - b                             # subtraction
a * b                             # multiplication
a / b                             # division
a ** 2                            # square

np.add(a, b)                      # add() function
np.subtract(a, b)                 # subtract() function
np.multiply(a, b)                 # multiply() function
np.divide(a, b)                   # divide() function

# ---------------------------
# 8. Aggregate Functions
# ---------------------------
np.sum(a)                         # sum
np.mean(a)                        # mean
np.median(a)                      # median
np.std(a)                         # standard deviation
np.var(a)                         # variance

np.min(a)                         # minimum value
np.max(a)                         # maximum value
np.argmin(a)                      # index of minimum
np.argmax(a)                      # index of maximum

# ---------------------------
# 9. Axis = 0 / 1
# ---------------------------
np.sum(a, axis=0)                 # column-wise sum
np.sum(a, axis=1)                 # row-wise sum

# ---------------------------
# 10. Random Module
# ---------------------------
np.random.rand(2, 3)              # uniform random
np.random.randn(2, 3)             # normal distribution
np.random.randint(1, 10, 5)       # random integers
np.random.seed(42)                # set seed for reproducibility

# ---------------------------
# 11. Stacking Arrays
# ---------------------------
np.hstack((a, b))                 # horizontal stack
np.vstack((a, b))                 # vertical stack
np.concatenate([a, b], axis=0)    # concatenate

# ---------------------------
# 12. Matrix Operations
# ---------------------------
a.T                                # transpose
np.transpose(a)                    # transpose function

np.dot(a, b)                       # dot product
a @ b                              # matrix multiplication

# ---------------------------
# 13. Copy vs View
# ---------------------------
b = a.copy()                       # deep copy
c = a.view()                       # shallow copy

# ---------------------------
# 14. Sorting
# ---------------------------
np.sort(a)                         # sorted array
a.sort()                           # sort in place
np.argsort(a)                      # return indices

# ---------------------------
# 15. Unique Elements
# ---------------------------
np.unique(a)                       # unique values
np.unique(a, return_counts=True)   # with counts

# ---------------------------
# 16. Handling NaN
# ---------------------------
np.isnan(a)                        # check NaN
np.nan_to_num(a)                   # replace NaN
np.nanmean(a)                      # mean ignoring NaN

# ---------------------------
# 17. Broadcasting
# ---------------------------
a + 5                              # scalar addition
a + np.array([1, 2, 3])            # vector broadcast

# ---------------------------
# 18. Save & Load Data
# ---------------------------
np.save("file.npy", a)             # save numpy array
np.load("file.npy")                # load array

np.savetxt("file.txt", a)          # save to text
np.loadtxt("file.txt")             # load from text

# ---------------------------
# 19. Data Types
# ---------------------------
a.dtype                            # get data type
a.astype(np.float32)               # convert dtype
a.astype(int)                      # convert to int

# ---------------------------
# 20. Useful Functions
# ---------------------------
np.clip(a, 0, 5)                   # limit range
np.where(a > 5, 1, 0)              # if-else condition
np.cumsum(a)                       # cumulative sum
np.cumprod(a)                      # cumulative product
