# Text and Binary
# rb - read binary
# file = open('movies_dataset/movies.dat', 'r')
# data = file.read()
# print(data)

users = {
    'movie_name':['thor','hulk','superman','batman','ironman','aquaman',
          'dhamaal','baahubali','sultan','kgf'],
    'movie_rating':[5,5,4,4,5,3,4,4,3,5],
    'movie_category':['action','action','action','action','action',
                      'action','comedy','drama','drama','action']
}

for i in range(len(users['movie_rating'])):
    if users['movie_rating'][i] == 5:
        print(users['movie_name'][i], users['movie_category'][i])


