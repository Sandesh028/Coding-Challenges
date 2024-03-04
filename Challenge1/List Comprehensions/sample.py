# ## Squaring numbers 1 to 5
# squares = [x**2 for x in range(1, 6)]
# print(squares)

# # Filtering Even Numbers
# num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# even = [i for i in num if i % 2 == 0]
# print(even)

# # Transforming Strings
# names = ["Bob", "Alice", "Tom", "Jerry"]
# uppercase = [n.upper() for n in names]
# print(uppercase)

# Negative Numbers
# num = [1, -2, 3, -4, 5]
# neg_num = [-n for n in num]
# print(neg_num)

# Words Longer Than Three Letters
# sentence = input("Enter the sentence :")
# words = sentence.split()
# print(words)

# w_length = {word: len(word) for word in words}
# larger_words = [word for word, length in w_length.items() if length >= 3]
# print(larger_words)

# Divisible by Both 2 and 3: From a list of numbers from 1 to 30, create a list of numbers that are divisible by both 2 and 3.
num = list(range(1, 31))
div = [i for i in num if i % 2 == 0 and i % 3 == 0]
print(div)