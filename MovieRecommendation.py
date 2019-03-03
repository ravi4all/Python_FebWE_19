# Finding Similarity of two users
user_1 = {'thor','hulk','superman','batman','ironman','aquaman',
          'dhamaal','baahubali','sultan','kgf'}
user_2 = {'thor','hulk','spiderman','avengers','ironman','aquaman',
          'fukrey','baahubali','sanju','kgf'}

# jaccard distance - a intersection b / a union b
intersection = user_1.intersection(user_2)
union = user_1.union(user_2)
d = len(intersection) / len(union)
sim = 1 - d
print(sim * 100)
print("Similar Movies", intersection)