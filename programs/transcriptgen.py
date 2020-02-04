# Create Script for generating Language Model for CMU Sphinx

# Read The input file
try:
    infile = open("input.txt", "r")
except FileNotFoundError:
    print("Input file not found, Please rename it to input.txt")

# Create Output file and temp file
outfile = open("output.txt", "w+")
tempfile1 = open("temp1.txt", "w+")
tempfile2 = open("temp2.txt", "w+")

# Create set for checking duplicates
chklist = set()

# Clear the contents (IF written)
outfile.truncate()
tempfile1.truncate()
tempfile2.truncate()

# Copy to the temp file with period and newline fix.
for line in infile:
    tempfile1.write(line.replace(". ", "\n"))

tempfile1.seek(0, 0)
for line in tempfile1:
	tempfile2.write(line.replace(".", "\n"))

count = 0
# Write the output file with proper format.
tempfile2.seek(0, 0)
for anotherline in tempfile2:
    if anotherline not in chklist:
        chklist.add(anotherline)
        outfile.write("<s>")
        outfile.write(anotherline.replace("\n", "</s>\n"))
    else:
        count += 1

print("Found Duplicates: ", count)

# Close the files
outfile.close()
tempfile1.close()
tempfile2.close()
infile.close()

print("Completed!")