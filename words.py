"""
Get a file from the web
http://icarus.cs.weber.edu/~hvalle/hafb/words.txt

Task 1: Count number of words in document
"""
from urllib.request import urlopen
file = "http://icarus.cs.weber.edu/~hvalle/hafb/words.txt"

count = 0
data = {}
with urlopen(file) as story:
    for line in story:
        words = line.decode('utf-8').split()
        for word in words:
            count += 1
            if word in data:
                data[word] += 1
            else:
                data[word] = 1
print(count)
print(data)
print(sorted(data.items()))

for key in sorted(data.keys()):
    print(key, data[key])

