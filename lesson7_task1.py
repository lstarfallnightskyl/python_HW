# Ask user to input a sentence
sentence = input("Enter a sentence: ")

# Split the sentence into words
words = sentence.split()

# Create an empty dictionary to store word counts
word_counts = {}

# Go through each word and count occurrences
for word in words:
    if word in word_counts:
        word_counts[word] = word_counts[word] + 1
    else:
        word_counts[word] = 1

# Print the final dictionary
print(word_counts)
