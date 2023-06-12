import numpy as np

# Collect data
reviews = {
    'Alice': {'A': 5, 'B': 2, 'C': 3},
    'Bob': {'A': 3, 'B': 4, 'C': 5, 'D': 3},
    'Charlie': {'A': 4, 'B': 1, 'C': 4, 'D': 2},
    'Dave': {'B': 3, 'C': 4, 'D': 5},
    'Eve': {'A': 2, 'C': 5, 'D': 4}
}

# Preprocess data
users = list(reviews.keys())
restaurants = sorted(set.union(*[set(r.keys()) for r in reviews.values()]))
user_ratings = np.zeros((len(users), len(restaurants)))
for i, user in enumerate(users):
    for j, restaurant in enumerate(restaurants):
        if restaurant in reviews[user]:
            user_ratings[i, j] = reviews[user][restaurant]

# Compute item-item cosine similarity
def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

item_ratings = user_ratings.T
item_similarities = np.zeros((len(restaurants), len(restaurants)))
for i in range(len(restaurants)):
    for j in range(i+1, len(restaurants)):
        similarity = cosine_similarity(item_ratings[i], item_ratings[j])
        item_similarities[i, j] = similarity
        item_similarities[j, i] = similarity

# Implement KNN algorithm
def knn(restaurant, k):
    restaurant_index = restaurants.index(restaurant)
    similarities = item_similarities[restaurant_index]
    indices = np.argsort(similarities)[::-1][:k]
    return [(restaurants[i], similarities[i]) for i in indices]

user = 'Charlie'
k = 4
recommendations = []
for restaurant in restaurants:
    if restaurant not in reviews[user]:
        restaurant_ratings = np.zeros(k)
        for i, item in enumerate(restaurants):
            if item in reviews[user]:
                if item in [restaurant for restaurant, _ in knn(restaurant, k)]:
                    similarity_index = [restaurant for restaurant, _ in knn(restaurant, k)].index(item)
                    restaurant_ratings[similarity_index] = reviews[user][item]
        similarities = np.array([similarity for _, similarity in knn(restaurant, k)])
        recommendation = (restaurant, np.dot(similarities, restaurant_ratings) / np.sum(similarities))
        recommendations.append(recommendation)

recommendations.sort(key=lambda x: x[1], reverse=True)
print(recommendations)
