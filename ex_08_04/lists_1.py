fname = input("Enter file name: ")
fhand = open(fname)
lst = list()

#add unique words
for line in fhand:
    words = line.split()
    for word in words:
        if word in lst:
            continue
        lst.append(word)

lst.sort()
print(lst)
