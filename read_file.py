# Open and read pelican.txt
# Read the entire contents of the file using the read() method and stores them in file_contents.
with open("pelican.txt", "r") as file_handle:
    # Read the entire contents of the file
    file_contents = file_handle.read()

    # Display the type and contents of the data
    print("Type:", type(file_contents))
    print("Contents:", file_contents)
    # It prints the type of data stored in file_contents (which will be a string)
    # and prints the actual contents of the file.

    # Read the file into a list
    file_handle.seek(0)  # Move cursor to the beginning of the file
    file_lines = file_handle.readlines()

    # Output the number of items in the list
    print("Number of lines:", len(file_lines))
    print("\n" + "#" * 50)
    # Iterate over and print the contents of the file
    print("File contents:")
    for line in file_lines:
        print(line[:-1])
