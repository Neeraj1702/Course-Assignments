
filename='Output.txt'
file=open(filename, 'r+')
user_input=(input("Enter text to Write to the file: "))
writing_in_file=file.write(user_input)
print(f"Data successfully written to {filename}")

file=open(filename,'a')
new_input=input("Enter additional text to append to the file: ")
appending_in_file=file.write(f"\n{new_input}")
print(f"Data successfully appended")

file=open(filename,'r+')
reading_file=file.read()
file.close()

print(f"Final Content of {filename}:\n{reading_file}")