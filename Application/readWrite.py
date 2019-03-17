import csv

def readData():
    data = []
    with open('users.csv') as file:
        reader = csv.reader(file)
        for row in reader:
            data.append(row)
    return data

def writeData(user):
    with open('users.csv','a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(user.values())