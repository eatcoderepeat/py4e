name = input("Enter file: ")
if len(name) < 1:
    name = "mbox-short.txt"
text = open(name)
counter = {}

#Find lines beginning with From
for line in text:
    line.rstrip()
    words = line.split()
    if len(words) == 0:
        continue
    if words[0] != 'From':
        continue
    #If sender not in dict, add sender, set default to 0, then add 1;
    #else, add 1 to senders value
    counter[words[1]] = counter.get(words[1], 0) + 1

#Find most frequent sender
max_value = max(counter.values())
print(max(counter, key=counter.get), max_value)
