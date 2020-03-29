# find common elements in two lists
first = ['cat','dog','parrot','fish']
second = ['fish', 'hamster', 'mouse', 'dog']

# Solution 1
match = []
for i in first:
    for j in second:
        if i == j:
            match.append(i)

print('Match: {}'.format(match))

# Solution 2
match = list(set(first).intersection(second))
print('Match: {}'.format(match))

# solution 3 (List comprehension)
# Syntax to use comprehension: [expression for item in list]

match = [ i for i in first if i in second]
print('Match: {}'.format(match))
