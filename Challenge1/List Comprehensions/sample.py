## Squaring numbers 1 to 5
squares = [x**2 for x in range(1, 6)]
print(squares)

## Filtering Even Numbers
num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even = [i for i in num if i % 2 == 0]
print(even)

## Transforming Strings
names = ["Bob", "Alice", "Tom", "Jerry"]
uppercase = [n.upper() for n in names]
print(uppercase)

## Negative Numbers
num = [1, -2, 3, -4, 5]
neg_num = [-n for n in num]
print(neg_num)

## Words Longer Than Three Letters
sentence = input("Enter the sentence :")
words = sentence.split()
print(words)

w_length = {word: len(word) for word in words}
larger_words = [word for word, length in w_length.items() if length >= 3]
print(larger_words)



## Divisible by Both 2 and 3: From a list of numbers from 1 to 30, create a list of numbers that are divisible by both 2 and 3.
num = list(range(1, 31))
div = [i for i in num if i % 2 == 0 and i % 3 == 0]
print(div)



## Problem : Swap Case
### Write a Python program that takes a sentence from the user and returns the sentence with the case of each letter swapped (i.e., lowercase letters become uppercase and vice versa). Try to use a list comprehension.
sentence = "Hello! World"
swap_sen = ''.join([char.swapcase() for char in sentence])
print(swap_sen)


## Problem : Unique Elements
### Given a list of numbers, write a Python program to create a new list that contains each number only once. Make sure the original order of numbers is preserved.
num = [1, 2, 2, 3, 3, 4, 4, 5]
unique_number = []
[unique_number.append(n) for n in num if n not in unique_number]
print(unique_number)

## Problem : Fibonacci Sequence
### Write a function that accepts a number n and returns a list containing the first n elements of the Fibonacci sequence. Recall that the Fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones, usually starting with 0 and 1.
def fibonacci(n):
    fib_seq = [0, 1]
    [fib_seq.append(fib_seq[-2] + fib_seq[-1]) for f in range (2, n)]
    return fib_seq[:n]
print(fibonacci(12))


# Problem : Filter Palindromes
### Given a list of words, use a list comprehension to create a new list containing only the words that are the same forwards and backwards (i.e., palindromes).
words = ["radar", "python", "level", "world", "madam"]
palindromes = [word for word in words if word == word[::-1]]
print(palindromes)


# Problem : Dictionary Comprehension
### Given two lists, one of keys and one of values, write a Python program that creates a dictionary from these keys and values using dictionary comprehension.
keys = ['a', 'b', 'c']
val = [1, 2, 3]
dictionary = {k: v for k, v in zip(keys, val)}
print(dictionary)
