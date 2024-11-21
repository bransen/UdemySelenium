# Read the file and store all lines in list
# Reverse  list
# Write back to file

with open('test.txt', 'r') as reader:
    content = reader.readlines()  # [apple, boy, cat, dog, elephant]
    reversed(content)  # {elephant, dog, cat, boy, apple]
    with open('test.txt', 'w') as writer:
        for line in reversed(content):
            writer.write(line)
