""" with open("d2.txt", "w", encoding="utf-8") as content:
    content.write("Hello, World!") """

with open("d2.txt", "r+", encoding="utf-8") as content:
    f=content.read()
    print(f)
    content.write("Hello, World!")