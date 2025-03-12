# Sample dictionary test data with only one key-value pair

data = {
    "1": "Alice",
    "2": "Bob",
    "3": "Charlie",
    "4": "David",
    "5": "Eve",
    "6": "Frank",
    "7": "Grace",
    "8": "Hank",
    "9": "Ivy",
    "10": "Jack"
}
query=input("Enter a key to search:")
if query in data:
    print("The key is found in the dictionary")
    print("The value of the key is:"+data[query])
else:
    print("The key is not found in the dictionary")
    print("the length of the dictionary is:"+str(len(data)))

