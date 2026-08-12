# file = open('test.txt')

# #read all contents of file
# # print(file.read())

# #read onyl 5 characters
# print("first 5 characters of file are:")
# # print(file.read(5))

# #read only first line
# print(file.readline())
# print(file.readline())  #reads second line



# file.close()

# print all the contents of the file line by line using readline method -- interview question
# file = open('test.txt')

# while True:
#     line  = file.readline()
#     if not line :
#         break
#     print(line)

# file.close()


# using readlines -> stores everything in the list and then we can iterate over it

file = open('test.txt')

for line in file.readlines():
    print(line)
 

file.close()
