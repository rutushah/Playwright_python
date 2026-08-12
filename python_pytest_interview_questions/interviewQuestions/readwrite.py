#read and write in file

#to wite in file in w mode
with open("test.txt", "w")  as f: 
    f.write("hello world")

try:
    #to read in file in r mode
    with open("test.txt","r") as f:
        content = f.read()
        print(content)
except FileNotFoundError as e:
    print("File not found:", e)

finally:
    print("File operation completed.")