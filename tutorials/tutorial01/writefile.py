
# open a new file
f = open("datafile.csv", "w")

# write headings, then some data
# separated by the newline symbol
# \n which is like pressing Enter
f.write("NAME,AGE,SEX\n")
f.write("Robert,37,M\n")
f.write("Kelly,29,F\n") 

# finish writing the file
f.close()

input('Press ENTER to continue...')
