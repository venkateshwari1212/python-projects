#  Take a text file as input and create a new file with its
#  contents reversed

# Open the input file and read its contents
input_file = "input.txt"
output_file = "reversed.txt"

file = open(input_file, "r")  # Open file in read mode
content = file.read()  # Read content
file.close()  # Close the file manually

# Reverse the content
reversed_content = content[::-1]

# Open the output file and write the reversed content
file = open(output_file, "w")  # Open file in write mode
file.write(reversed_content)  # Write reversed content
file.close()  # Close the file manually

print(f"Reversed content has been saved to {output_file}")

