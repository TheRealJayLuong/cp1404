"""Count the occurrences of words in a string"""

counts = {}

text = input("Please enter your Text:")
texts = text.split()


for word in texts:
    counts[word] = counts.get(word,0) + 1

texts = list(counts.keys())
texts.sort()

max_length = max((len(word)for word in texts))

for word in texts:
    print("{:{}} : {}".format(word, max_length, counts[word]))