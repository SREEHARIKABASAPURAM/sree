#file objects
file = open('Dummy.txt','r')
print(file.name)
print(file)
print(file.mode)
file.close() #in this method you must close file
# #context manager
with open('Dummy.txt', 'r') as file:
#context manager
# print(file.read())
    print(file.readline(), end="")
    print(file.readline(), end="")
    print(file.tell())
#print(file.readlines())
with open('Dummy.txt', 'r')as file:
    for line in file:
        print(line, end='')

with open('Dummy.txt', 'r')as file:
    file_content = file.read(100)
    print(file_content, end='')
    file_content = file.readline()
    print(file_content, end='')
    print(file.tell()) #tells the position in file

with open('Dummy.txt','r')as file:
    size_to_read = 20
    file_contents = file.read(size_to_read)
    while len(file_contents) > 0:
        print(file_contents,end='*')
        file_contents = file.read(size_to_read)

with open('Text.txt','a')as file:
    file.write('test write....')

sampleFile = open("Text.txt",'w')
sampleFile.write("This should write to a file")
sampleFile.close()

file = op


