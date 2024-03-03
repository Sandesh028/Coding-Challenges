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
