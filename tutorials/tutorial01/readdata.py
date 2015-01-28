
print("Accessing data file...\n")

f = open("datafile.csv", "r")  # code "r" means "read"

# Ingest the whole first line.
# .strip() removes the "\n" character
# .split(",") turns the items into a list
headers = f.readline().strip().split(",")

# for each remaining line in the file, do this:
for line in f.readlines():
    line = line.strip().split(",")

    # headers and line are lists. we access their items
    # with numerical indexes, counting from zero
    
    print(headers[0],"is",line[0])
    print(headers[1],"is",line[1])
    print(headers[2],"is",line[2],"\n")

# finish writing the file
f.close()

input('Press ENTER to continue...')
