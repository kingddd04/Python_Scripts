filepath = "program.py"

filename = filepath.removesuffix(".py")  # Removes the ".py" suffix
fileextension = filepath.split(".")[-1]  # Extracts the file extension

print(filename)       # Output: program
print(fileextension)  # Output: py