import string
import matplotlib.pyplot as plt

def word_frequency_counter(text):
    # Remove punctuation and convert to lowercase
    translator = str.maketrans("", "", string.punctuation)
    text = text.translate(translator).lower()

    # Tokenize the text into words
    words = text.split()

    # Initialize an empty dictionary to store word frequencies
    word_counts = {}

    # Count the frequency of each word
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1

    return word_counts

# Example usage
sample_text = "This is a sample text. This text will be used to demonstrate the word frequency counter."

result = word_frequency_counter(sample_text)

# Output the word frequencies
for word, count in result.items():
    print(f"{word}: {count}")

# Plotting the word frequencies
plt.bar(result.keys(), result.values())
plt.xlabel('Words')
plt.ylabel('Frequency')
plt.title('Word Frequency Counter')
plt.show()
