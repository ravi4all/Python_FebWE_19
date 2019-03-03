import csv
# comma seperated values

data = [
    ['Sachin','Tendulkar'],
    ['MS','Dhoni'],
    ['Virat','Kohli'],
    ['Yuvraj','Singh']
]

# file = open('data.csv','w')
# file.close()

# Write CSV
with open('data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    for row in data:
        writer.writerow(row)

# Read CSV
with open('data.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)