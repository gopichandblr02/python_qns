import  numpy as np
################################ 1. Introduction to NumPy ###################################
"""
NumPy is a Python library created in 2005 that performs numerical calculations. It is generally used for working with arrays.
NumPy also includes a wide range of mathematical functions, such as linear algebra, Fourier transforms, and random number generation, which can be applied to arrays.

What is NumPy Used for?
NumPy is an important library generally used for:

Machine Learning
Data Science
Image and Signal Processing
Scientific Computing
Quantum Computing
Why Use NumPy?
Some of the major reasons why we should use NumPy are:

1. Faster Execution

In Python, we use lists to work with arrays. But when it comes to large array operations, Python lists are not optimized enough.
Numpy arrays are optimized for complex mathematical and statistical operations. 
Operations on NumPy are up to 50x faster than iterating over native Python lists using loops.
Here're some of the reasons why NumPy is so fast:
Uses specialized data structures called numpy arrays.
Created using high-performance languages like C and C++.

2. Used with Various Libraries
NumPy is heavily used with various libraries like Pandas, Scipy, scikit-learn, etc.
Import NumPy in Python
We can import NumPy in Python using the import statement.
import numpy as np
The code above imports the numpy library in our program as an alias np.
After this import statement, we can use NumPy functions and objects by calling them with np.
Note:
If we import NumPy without an alias using import numpy, we can create an array using the numpy.array() function.
Using an alias np is a common convention among Python programmers, as it makes it easier and quicker to refer to the NumPy library in your code.
"""
####################### 2. NumPy Array Creation #######################
"""
The NumPy array is similar to a list, but with added benefits such as being faster and more memory efficient.
"""
import numpy as np
# create a list named list1
list1 = [2, 4, 6, 8]
# create numpy array using list1
array1 = np.array(list1)
print(array1)
# Output: [2 4 6 8]
############################################
import numpy as np
# create an array with 4 elements filled with zeros
array1 = np.zeros(4)
print(array1)
# Output: [0. 0. 0. 0.]
# Note: Similarly we can use np.ones() to create an array filled with values 1.
############################################
import numpy as np
# create an array with values from 0 to 4
array1 = np.arange(5)
print("Using np.arange(5):", array1)
# create an array with values from 1 to 8 with a step of 2
array2 = np.arange(1, 9, 2)
print("Using np.arange(1, 9, 2):",array2)
# Using np.arange(5): [0 1 2 3 4]
# Using np.arange(1, 9, 2): [1 3 5 7]
###########################################
import numpy as np
# generate an array of 5 random numbers
array1 = np.random.rand(5)
print(array1)
# [0.08455648 0.56379034 0.66463204 0.97608605 0.30700052]
########################################
import numpy as np
# create an empty array of length 4
array1 = np.empty(4)
print(array1)
# [1.47966080e-316 0.00000000e+000 9.06092203e-312 2.47218893e-253]