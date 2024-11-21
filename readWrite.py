file = open('test.txt')

# Read All contents of file
# print (file.read()) #restricnt with example file.read(5)
# print (file.readline())
# print (file.readline())
# file.close()


# Print line by line using readline method

# line = file.readline()
# while line !="":
#    print(line)
#    line = file.readline()


# common task and interview issue to print list
# values = [apple, boy, cat, dog, elephant]
for line in file.readlines():
    print(line)

file.close()
