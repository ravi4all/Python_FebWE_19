data = [
    {'brand':'Apple','price':50000,'color':'silver','product':'iphone'},
    {'brand':'Samsung','price':45000,'color':'black','product':'Tab'},
    {'brand':'Xiaomi','price':15000,'color':'black','product':'Note'},
    {'brand':'Apple','price':80000,'color':'white','product':'Macbook'},
    {'brand':'Samsung','price':55000,'color':'golden','product':'Galaxy'},
    {'brand':'Micromax','price':10000,'color':'black','product':'N-series'},
]

brandName = input("Enter brand name : ")
for i in range(len(data)):
    if data[i]['brand'] == brandName:
        print(data[i])