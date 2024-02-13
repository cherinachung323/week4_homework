# Write method creates a new .txt file in the directory
# file is opened, and the file pointer is assigned to the myFile variable
# "with" statement = when all statements in the block are executed, the file is closed automatically
with open("pelicanPB.txt", "a") as my_file:
    my_file.write("A wonderful bird is the pelican!\n")
    my_file.write("His bill holds more than his belican.\n")
    lines = ["He can take in his beak,\n",
         "Enough food for a week,\n",
         "But I'm damned if I see how the helican.\n"]
    my_file.writelines(lines)
