import numpy as np

a = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])

# 1. How many negative numbers are there?
a1 = a[a < 0]
a1.shape[0]

# There are 4 negative numbers

# --------------
# 2. How many positive numbers are there?

a2 = a[a>0]
a2.shape[0]

# There are 5 positive numbers



# 3. How many even positive numbers are there?

a2 = [n for n in a if n > 0 and n % 2 == 0]

# There are 3 even positives


# 4.  If you were to add 3 to each data point, how many 
# positive numbers would there be?

x = a + 3 
x1 = x[x > 0]
x1.shape[0]

#  There will be 1010 positive numbers


# 5.  If you squared each number, what would the new mean 
#  and standard deviation be?

n = a ** 2 
print(n)
print(n.mean())
print(n.std())

# 6. A common statistical operation on a dataset is 
# centering. This means to adjust the data such that the 
# mean of the data is 0. This is done by subtracting the 
# mean from each data point. Center the data set. See this 
# link for more on centering



# 7.  Calculate the z-score for each data point. Recall 
#  that the z-score is given by:




# 8. Copy the setup and exercise directions from More 
# Numpy Practice into your numpy_exercises.py and add 
# your solutions.

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Exercise 1 - Make a variable called sum_of_a to hold 
# the sum of all the numbers in above list
sum_of_a = sum(a)
print(sum_of_a)


# Exercise 2 - Make a variable named min_of_a to hold the 
# minimum of all the numbers in the above list
min_of_a = min(a)
print(min_of_a)


# Exercise 3 - Make a variable named max_of_a to hold the 
# max number of all the numbers in the above list
max_of_a = max(a)
print(max_of_a)


# Exercise 4 - Make a variable named mean_of_a to hold the 
# average of all the numbers in the above list
mean_of_a = sum(a) / len(a)
print(mean_of_a)


# Exercise 5 - Make a variable named product_of_a to hold 
# the product of multiplying all the numbers in the above 
# list together

product_of_a = 1
for i in a:
    product_of_a = product_of_a * i
print(product_of_a)


# # Exercise 6 - Make a variable named squares_of_a. It 
# should hold each number in a squared like 
# [1, 4, 9, 16, 25...]

squares_of_a = []
for i in a:
    squares_of_a.append(i ** 2)

print(squares_of_a)


# Exercise 7 - Make a variable named odds_in_a. It should 
# hold only the odd numbers

odds_in_a = [num for num in a if num % 2 == 1]
print(odds_in_a)


# Exercise 8 - Make a variable named evens_in_a. It should 
# hold only the evens.

evens_in_a = [num for num in a if num % 2 == 0]
print(evens_in_a)


## What about life in two dimensions? A list of lists is 
# matrix, a table, a spreadsheet, a chessboard...

## Setup 2: Consider what it would take to find the sum, 
# min, max, average, sum, product, and list of squares for 
# this list 


b = np.array ([
    [3, 4, 5],
    [6, 7, 8]
])

# Exercise 1 - refactor the following to use numpy. 
# Use sum_of_b as the variable. **Hint, you'll first need 
# to make sure that the "b" variable is a numpy array**

sum_of_b = np.sum(b)
print(sum_of_b)
## print(type(b))


# # Exercise 2 - refactor the following to use numpy.

min_of_b = np.min(b)
print(min_of_b)


# Exercise 3 - refactor the following maximum calculation 
# to find the answer with numpy.

max_of_b = np.max(b)
print(max_of_b)


# Exercise 4 - refactor the following using numpy to find 
# the mean of b
mean_of_b = np.mean(b)
print(mean_of_b)


# # Exercise 5 - refactor the following to use numpy for 
# calculating the product of all numbers multiplied together.
product_of_b = np.prod(b)
print(product_of_b)


# Exercise 6 - refactor the following to use numpy to find the list of squares
squares_of_b = np.sqrt(b)
print(squares_of_b)


# Exercise 7 - refactor using numpy to determine the odds_in_b
odds_in_b = b[b % 2 == 1]
print(odds_in_b)



# 8. Exercise 8 - refactor the following to use numpy to filter only the even numbers
evens_in_b = b[b % 2 == 0]
print(evens_in_b)


# 9. Exercise 9 - print out the shape of the array b.
print(b.shape)


# Exercise 10 - transpose the array b.
print(np.transpose(b))


# Exercise 11 - reshape the array b to be a single list of 6 numbers. (1 x 6)
print(np.reshape(b, (1, 6)))


# Exercise 12 - reshape the array b to be a list of 6 lists, each containing only 1 
# number (6 x 1)
print(np.reshape(b, 6, 1))




######

## Setup 3






