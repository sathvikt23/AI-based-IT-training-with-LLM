import Textsum as ps
import sys 
data="""
Basics of Loops in Python

Loops in Python are used to execute a block of code repeatedly. There are two main types of loops:

For Loop: Iterates over a sequence and executes a block of code for each item in the sequence.
Example:

python
Copy code
for item in sequence:
    # Code block to be executed for each item
While Loop: Repeats a block of code as long as a specified condition is true.
Example:

python
Copy code
while condition:
    # Code block to be executed as long as condition is true
Advanced Looping in Python

Python offers several advanced looping techniques for efficient iteration:

Enumerate: Adds a counter to an iterable object, allowing iteration over elements and their indices simultaneously.

Zip: Combines multiple iterables into tuples, allowing simultaneous iteration over corresponding elements.

List Comprehension: Provides a concise way to create lists using a single line of code.

Dictionary Comprehension: Creates dictionaries in a compact form.

Generator Expression: Creates a generator object that lazily generates values, saving memory compared to lists.

These looping techniques provide powerful tools for iterating over data efficiently in Python, enhancing code readability and reducing complexity.

"""
new="""
# Python3 program for Bubble Sort Algorithm Implementation
def bubbleSort(arr):
	
	n = len(arr)

	# For loop to traverse through all 
	# element in an array
	for i in range(n):
		for j in range(0, n - i - 1):
			
			# Range of the array is from 0 to n-i-1
			# Swap the elements if the element found 
			#is greater than the adjacent element
			if arr[j] > arr[j + 1]:
				arr[j], arr[j + 1] = arr[j + 1], arr[j]
				
# Driver code

# Example to test the above code
arr = [ 2, 1, 10, 23 ]

bubbleSort(arr)

print("Sorted array is:")
for i in range(len(arr)):
	print("%d" % arr[i])



"""
#prompt="""Generate 5 coding DSA questions with expected output on this text , return in JSON format '{'questions':['question','output']}' ?"""
data1=ps.all_in_one.askgem(f"explain this code and give a better alternative approach time complexity  \n  {new}  ")

print(data1) 
