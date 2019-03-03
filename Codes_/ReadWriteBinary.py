import sys
file = open('cap.png', 'rb')
data = file.read()
# print(data)
file.close()
# print(sys.getsizeof(data))
file = open('cap_2.png', 'wb')
file.write(data)
file.close()