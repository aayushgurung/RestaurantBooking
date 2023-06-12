# Collect data
from tabulate import tabulate
import json
from scipy.sparse import csr_matrix
from sklearn.metrics.pairwise import cosine_similarity
import time
# reviews = {
#     'Alice': {'A': 5, 'B': 2, 'C': 3},
#     'Bob': {'A': 3, 'B': 4, 'C': 5, 'D': 3},
#     'Charlie': {'A': 4, 'B': 1, 'C': 4, 'D': 2},
#     'Dave': {'B': 3, 'C': 4, 'D': 5},
#     'Eve': {'A': 2, 'C': 5, 'D': 4}
# }
start_time=time.time()
with open('C:/Users/Nirajan/Desktop/python 30 days/final data for restaurant/user_item_matrix_test.json', 'r',encoding='utf-8') as f:
    reviews = json.load(f)
with open('C:/TEST FINAL YEAR/user_ratings.json', 'r',encoding='utf-8') as f:
    user_ratings=json.load(f)
# print(user_ratings)

# Preprocess data
users = list(reviews.keys())
restaurants = sorted(set.union(*[set(r.keys()) for r in reviews.values()]))
# user_ratings = []
# for user in users:
#     row = []
#     for restaurant in restaurants:
#         if restaurant in reviews[user]:
#             row.append(reviews[user][restaurant])
#         else:
#             row.append(0)
#     user_ratings.append(row)


user_ratings_sparse = csr_matrix(user_ratings)
# print(user_ratings_sparse)
# print('Restaurants\n{}'.format(restaurants))
cosine_similarities = cosine_similarity(user_ratings_sparse)

# user_ratings = [[0 for _ in range(len(restaurants))] for _ in range(len(users))]
# for i, user in enumerate(users):
#     for j, restaurant in enumerate(restaurants):
#         if restaurant in reviews[user]:
#             user_ratings[i][j] = reviews[user][restaurant]

# print(user_ratings)

# # Compute cosine similarity
def dot(a, b):
    return sum([a[i] * b[i] for i in range(len(a))])

def norm(a):
    return (dot(a, a)) ** 0.5

# def cosine_similarity(a, b):
#     return dot(a, b) / (norm(a) * norm(b))

# cosine_similarities = [[0 for _ in range(len(users))] for _ in range(len(users))]

# for i in range(len(users)):
#     for j in range(i+1, len(users)):
#         similarity = cosine_similarity(user_ratings[i], user_ratings[j])
#         cosine_similarities[i][j] = similarity
#         cosine_similarities[j][i] = similarity

# with open('C:/TEST FINAL YEAR/cosine.json', 'w',encoding='utf-8') as f:
#     json.dump(cosine_similarities, f)
# print(tabulate(cosine_similarities,headers=restaurants,showindex=True))
# # Implement KNN algorithm
def knn(user, k):
    user_index = users.index(user)
    similarities = cosine_similarities[user_index]
    indices = sorted(range(len(similarities)), key=lambda x: similarities[x], reverse=True)[:k]
    return [(users[i], similarities[i]) for i in indices]

user = 'parilya'
k = 10
recommendations = []
for restaurant in restaurants:
    if restaurant in reviews[user]:
        restaurant_ratings = [0 for _ in range(k)]
        for i, u in enumerate(users):
            if restaurant in reviews[u]:
                if u in [user for user, _ in knn(user, k)]:
                    similarity_index = [user for user, _ in knn(user, k)].index(u)
                    print(similarity_index)
                    restaurant_ratings[similarity_index] = reviews[u][restaurant]
                    print(restaurant_ratings)
                    # print('\nSimilarity indes : {} '.format(u),similarity_index)
                    # print('Restaurant Ratings{}'.format(restaurant_ratings))
        similarities = [similarity for _, similarity in knn(user, k)]
        print(similarities)
        # print('KNN',knn(user,k))
        # print('Similarities {}'.format(similarities))
        # print('Restaurant -- ',restaurant)
        recommendation = (restaurant, dot(similarities, restaurant_ratings) / sum(similarities))
        # print('Recommendations',recommendation)
        recommendations.append(recommendation)
        # print(recommendations,'\n')

recommendations.sort(key=lambda x: x[1], reverse=True)
for i, (restaurant, rating) in enumerate(recommendations[:10]):
    print('Recommendation {}: {} (predicted rating: {:.2f})'.format(i+1, restaurant, rating))

end_time=time.time()
print(f'Eclapsed time{end_time-start_time}')
