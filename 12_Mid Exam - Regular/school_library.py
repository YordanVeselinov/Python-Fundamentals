library = input().split("&")
while True:
    command = input().split(" | ")
    if command[0] == "Done":
        break
    if command[0] == "Add Book":
        book = command[1]
        if book not in library:
            library.insert(0, book)
    elif command[0] == "Take Book":
        book = command[1]
        if book in library:
            index = library.index(book)
            library.pop(index)
    elif command[0] == "Swap Books":
        book_one = command[1]
        book_two = command[2]
        if book_one in library and book_two in library:
            index_one = library.index(book_one)
            index_two = library.index(book_two)
            library[index_one] , library[index_two] = library[index_two], library[index_one]
    elif command[0] == "Insert Book":
        book = command[1]
        if book not in library:
            library.append(book)
    elif command[0] == "Check Book":
        index = int(command[1])
        if 0 <= index < len(library):
            print(library[index])

print(", ".join(library))