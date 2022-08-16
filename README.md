# Backend-py
In this repo, i will work with python for backend



## Documentation

Documentation of some python commands used in this repository

### [yield Keyword](https://www.geeksforgeeks.org/python-yield-keyword/)

**Yield** is a keyword in Python that is used to return from a function without destroying the states of its local variable and when the function is called, the execution starts from the last yield statement. Any function that contains a yield keyword is termed a generator. Hence, yield is what makes a generator. The yield keyword in Python is less known but has a greater utility. we will see the **yield python example.**

### Difference between return and yield python

The **Yield keyword in Python** is similar to a return statement used for returning values in Python which returns a generator object to the one who calls the function which contains yield, instead of simply returning a value. The main difference between them is: In python the **return** statement stops the execution of the function. Whereas, the yield statement only pauses the execution of the function. Another difference is return statements are never executed. whereas, yield statements are executed when the function resumes its execution.

**Advantages of yield:**

- Since it stores the local variable states, hence overhead of memory allocation is controlled.
- Since the old state is retained, the flow doesn’t start from the beginning and hence saves time.

**Disadvantages of yield:** 

- Sometimes, the use of yield becomes erroneous if the calling of the function is not handled properly.
- Time and memory optimization has a cost of complexity of code and hence sometimes hard to understand the logic behind it.

**Example 1:** 

Demonstrating yield working with the help of a [list](https://www.geeksforgeeks.org/python-list/).

```python
# Python3 code to demonstrate
# yield keyword

# generator to print even numbers
def print_even(test_list):
	for i in test_list:
		if i % 2 == 0:
			yield i

# initializing list
test_list = [1, 4, 5, 6, 7]

# printing initial list
print("The original list is : " + str(test_list))

# printing even numbers
print("The even numbers in list are : ", end=" ")
for j in print_even(test_list):
	print(j, end=" ")

```

output

```
The original list is : [1, 4, 5, 6, 7]
The even numbers in list are :  4 6 
```

Example 2

In this example, we are yielding a square of a number between 1 to 100 using loop

```python
# A Python program to generate squares from 1
# to 100 using yield and therefore generator

# An infinite generator function that prints
# next square number. It starts with 1
def nextSquare():
	i = 1

	# An Infinite loop to generate squares
	while True:
		yield i*i
		# Next execution resumes from this point
		i += 1
		
# Driver Code
for num in nextSquare():
	if num > 100:
		break
	print(num)

```

Output

```
1
4
9
16
25
36
49
64
81
100
```

**Example 3:** 

The possible practical application is that when handling the last amount of data and searching particulars from it, yield can be used as we don’t need to look up again from start and hence would save time. There can possibly be many applications of yield depending upon the use cases. 

```python
# Python3 code to demonstrate yield keyword

# Checking number of occurrence of
# geeks in string

# generator to print even numbers


def print_even(test_string):
	for i in test_string:
		if i == "geeks":
			yield i


# initializing string
test_string = " The are many geeks around you, \
			geeks are known for teaching other geeks"

# printing even numbers using yield
count = 0
print("The number of geeks in string is : ", end="")
test_string = test_string.split()

for j in print_even(test_string):
	count = count + 1

print(count)
```

Output

```
The number of geeks in string is : 3
```
