
# input function for instructions. Type "OK"
user_instruct = input("Type 'OK' to clear first and last line = ")

OK = 0, 4
# Reads file
with open("pelicanPB.txt", "r") as my_file:
    content = my_file.read()

    with open("pelicanPB.txt", "r") as text:
        lines = text.readlines()

    # 'w' = code writes over file.
    # if "OK" is entered, first and last line are deleted ("helican" and "belican")
    # if "OK" not entered, no changes made
    # enumerate tracks number of iterations/lines in the file
    with open("pelicanPB.txt", "w") as text:
        for number, line in enumerate(lines):
            if number not in OK:
                text.write(line)

            else:
                print("No Changes made")
                break