# Define an array of strings
words = ["apple", "banana", "cherry", "apricot", "blueberry"]

# Use filter() to get words containing 'ap'
filtered_words = list(filter(lambda word: 'ap' in word, words))

print("Words containing 'ap':", filtered_words)
