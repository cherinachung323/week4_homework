# # file is opened, and the file pointer is assigned to the myFile variable
# # "with" statement = when all statements are executed, the file is closed automatically
with open("pelicanPB.txt", "r") as my_file:
    content = my_file.read()
    print("Class type is ", type(content))
    print("File content is\n", content)
    print("\n" + "#" * 50)

    my_file.seek(0)
    file_lines = my_file.readlines()

    print("Number of items in the list = ", len(file_lines))
    print("\n" + "#" * 50)

    print("File content: ")
    for line in file_lines:
        print(line[:-1])



