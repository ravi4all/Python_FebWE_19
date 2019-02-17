data = {
    "names" : ['Sachin','Kohli','yuvraj','Dhoni','Rohit','Rahul'],
    "scores" : [78,100,56,45,80,41],
    "ranking" : [2,1,3,4,5,6]
}

for i in range(len(data["names"])):
    if data["ranking"][i] <= 3:
        print(data["names"][i], data["scores"][i],data["ranking"][i])