try:
    filename='Sample.txt'
    file = open(filename, 'r+')
    reading_file=file.read()
    print(f"Reading File Content: \n Line1: {reading_file.split('\n')[0]} \n Line2: {reading_file.split('\n')[1]}")
except FileNotFoundError:
    print(f"Error: The file '{filename}' was not found")

