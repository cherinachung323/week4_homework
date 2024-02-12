# Open and append to pelican.txt
# Open the file "pelican.txt" in append mode ("a"), which allows us to add content to the end of the file.
with open("pelican.txt", "a") as file_handle:
    # Append the first line
    # use the write() method to append the first and second lines to the file.
    file_handle.write("A wonderful bird is the pelican,\n")
    # Append the second line
    file_handle.write("His bill holds more than his belican.\n")

    # Create a list of additional lines
    # \n creates line break
    lines = ["He can take in his beak,\n",
             "Enough food for a week,\n",
             "But I’m damned if I see how the helican.\n"]

    # 7. Append the list to the file
    file_handle.writelines(lines)
