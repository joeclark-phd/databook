
f = open("datafile.csv", "w")
f.write("NAME,AGE,SEX\n")

while True:
    name = input("Name (or ENTER to quit): ")
    if name == "": break
    age = input("Age: ")
    sex = input("Sex: ")
    
    # write one line of data
    f.write( name + "," + str(age) + "," + sex + "\n" )

# finish writing the file
f.close()
