print("Enter a sentence \n")
sent =input("")
words=sent.split()

dict1 = {}

for x in words:
    if x not in dict1:
        dict1[x] = 1
    else:
        dict1[x] += 1

# Print the dictionary
print(dict1)
