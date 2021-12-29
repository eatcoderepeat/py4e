name = input("Enter File: ")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
count = {}
list = []

#find 'from' line with timestamp
for line in handle:
    line.rstrip()
    words = line.split()
    if len(words) == 0:
        continue
    if words[0] != 'From':
        continue
    #isolate the hour from timestamp, count the frequency of each hour
    time = words[5]
    hour = time.split(":")[0]
    count[hour] = count.get(hour, 0) + 1
#print(count)
for (k,v) in count.items():
    temp = (k, v)
    list.append(temp)

#sort the list, then print in desired format
list = sorted(list)
for k, v in list:
    print(k, v)
