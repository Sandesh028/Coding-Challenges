# Objective: Write a Python program that performs the following tasks:

#     Generate a List of Random Numbers: Create a list containing 15 random integers between 1 and 100. (Hint: Use the random module's randint function.)
#     Filter the List: Create a new list that only contains numbers from the original list that are divisible by 5.
#     Sort the Filtered List: Sort this new list in descending order.
#     Sum and Average: Calculate and print the sum and the average of the numbers in the sorted, filtered list.

import random


a = [random.randint(1, 100) for _ in range(15)]
print("Original list of random numbers:", a)

b = [num for num in a if num % 5 == 0]
print("Filtered list (divisible by 5):", b)


b.sort(reverse=True)
print("Sorted list in descending order:", b)


c = sum(b)
avg = c / len(b) if b else 0
print("Sum of the list:", c)
print("Average of the list:", avg)
