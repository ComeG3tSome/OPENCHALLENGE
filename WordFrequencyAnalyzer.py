'''
Challenge: Word Frequency Analyzer (Case-Sensitive & Position-Aware)

Write a Python program that takes a paragraph of text and returns:

1. A dictionary of each unique word (case-sensitive) and the number of times it appears.


2. The position (index) of the first appearance of each word in the paragraph (counting words, not characters).


3. The most frequent word(s), with tie-breaker preference to the one that appeared first.



Rules:

A word is any sequence of characters separated by whitespace.

Punctuation stays (don't remove it).

Maintain case sensitivity (e.g., "Word" and "word" are different).
'''

paragraph = input("Enter your paragraph: \n")

wordFrequency = []

dictWordFrequency = {}

# Empty list of unique words to be able to return the index numbers of each unique word in the paragraph

uniqueWords = []

# List of words in the paragraph

words = paragraph.split()

# Variable that stores the highest frequency

hghFrequency = 0

#  loop to assign the number of times that each word appears in a paragraph in the wordFrequency list

for i in  range(len(words)):

    # Add each word of the paragraph at the end of the list
    wordFrequency.append(words.count(words[i]))

    # Reassign counter variable to 0
    i = 0

# For loop to assign all the values of the words' list and the word frequency list to the dictionary of the word frequency.

for i in range(len(words)):

    # Evaluate if the word is in the dictionary or not to avoid duplicates
    if words[i] not in dictWordFrequency:

    # Add the word and the number of times it appears in the dictionary.
     dictWordFrequency.update({words[i]:wordFrequency[i]})


# Print the dictionary of each unique word with the number of times that it appears
print(dictWordFrequency)

# Print empty line
print("\n")

# For loop to add each paragraph word in the list of unique words and print the index of each unique word
for word in words:
    # Ensure that the word is not in the list of unique words to avoid duplicates
    if word not in uniqueWords:

        # Add each item to the end of the list of unique words
        uniqueWords.append(word)

          # Print the index number of each unique word
        print(f"Index number of the word \"{word}\" is: {words.index(word)}")


# For loop to determine the value of the highest frequency variable
for key, value in dictWordFrequency.items():

    # Ensure that the frequency of the current word is greater than the current highest frequency
    if value > hghFrequency:
        # Assign the new highest frequency value
        hghFrequency = value
    else:
        # Go to the next iteration
        continue

# For loop that will be used to find the first word that appeared the most in the paragraph
for key, value in dictWordFrequency.items():

    # Determine if the frequency of the current word is equal to the highest frequency value
    if value == hghFrequency:

        # Print the word that appeared the most in the paragraph with its frequency
        print(f"The word that appeared the most in the paragraph is:  {key}\nFrequency: {value}")
        # Terminate the loop
        break

    else:
        # Go to the next iteration  
        continue
