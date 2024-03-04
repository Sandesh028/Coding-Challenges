# Problem Statement: Word Lengths in Sentences

# Objective: Write a Python program that performs the following tasks:

#     Input a Sentence: Ask the user to input a sentence.
#     Split the Sentence into Words: Break the sentence into individual words.
#     Calculate the Length of Each Word: For each word in the sentence, calculate its length.
#     Store Word Lengths: Create a dictionary where each key is a word from the sentence, and its value is the length of that word.
#     Find the Longest Word(s): Identify the longest word or words in the sentence (as there might be more than one word of the same maximum length).
#     Output the Results: Print the dictionary of word lengths, and then print the longest word or words along with their length.

a = input("Please enter a sentence: ")

words = a.split()

print("This the Sentence: ", a)
print(words)

w_length = {word: len(word) for word in words}
max_len = max(w_length.values())

longest_words = [word for word, length in w_length.items() if length == max_len]

print("Dictionary of word lengths:", w_length)
print("Longest word(s):", longest_words)
print("Length of the longest word(s):", max_len)