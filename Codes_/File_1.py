# Step - 1 : Open File
file = open('file_1.txt','r')
# Step - 2 : Read File
# data = file.read()
# will read file till 10th character
# data = file.read(10)

# data = file.readline()

data = file.readlines()
print(data)
# Step - 3 : Close File
file.close()