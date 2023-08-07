"""
Word Occurrences
Estimate: 10 minutes
Actual:   16 minutes
"""

user_text = input("Text: ")
word_to_count = {}
for word in user_text.split():
    word_to_count[word] = word_to_count.get(word, 0) + 1

maximum_length = max(len(word) for word in list(word_to_count.keys()))

for word, count in sorted(word_to_count.items()):
    print(f"{word:<{maximum_length}} : {count}")
