#week7fileprocessing
#namechecker

# On file names
valid_names = {
    "James", "Sally", "Sue", "William", "Mary",
    "Betty", "John", "Peter", "Ivan", "Denise"
}

# Names not found
with open("nofound.txt", "w") as output_file:
    while True:
        user_input = input("Enter a string (or type 'exit' to quit): ")
        if user_input.lower() == 'exit':
            break

        if user_input in valid_names:
            print(f"The string '{user_input}' is already in the file.")
        else:
            print(f"The string '{user_input}' has been written to nofound.txt.")
            output_file.write(user_input + "\n")
