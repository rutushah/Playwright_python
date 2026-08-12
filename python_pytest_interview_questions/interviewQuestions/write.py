#reverse the list and write the list back to the file

with open('test.txt', 'r') as reader:
    content = reader.readlines() 
    reversed_list = reversed(content)

    with open('test.txt', 'w') as writer:
        for line in reversed_list:
            writer.writelines(line)