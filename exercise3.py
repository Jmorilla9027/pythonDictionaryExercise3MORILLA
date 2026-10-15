fname = input('Enter file name: ')
fhand = open(fname)

counts = dict()

for line in fhand:
    line = line.rstrip()
    if not line.startswith('From '):
        continue
    words = line.split()
    email = words[1]
    counts[email] = counts.get(email, 0) + 1

print(counts)
