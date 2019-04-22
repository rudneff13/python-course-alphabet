


data = "So the normal way you might go about doing this task in python is using a basic for loop:".split()



newdict = {}
for j in range(1, len(data)+1):
    for i in data:
        newdict[j] = i
        j += 1
print(newdict)