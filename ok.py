import random
import math

# example user data
user_rated_items = ["item1", "item2", "item3", "item4", "item5"]
user_reserved_items = ["restaurant1", "restaurant2", "restaurant3", "restaurant4", "restaurant5"]
user_viewed_items = ["movie1", "movie2", "movie3", "movie4", "movie5", "movie6"]

# function to choose user items based on k
def choose_user_items(k, user_rated_items, user_reserved_items, user_viewed_items):
    if k == 3:
        # choose user rated, reserved, and viewed items
        return user_rated_items + user_reserved_items + user_viewed_items
    else:
        # choose ceil(k/3) number of items from each user item list
        n = math.ceil(k/3)
        print(n)
        items = []
        for lst in [user_rated_items, user_reserved_items, user_viewed_items]:
            print
            if n >= len(lst):
                items += lst
            else:
                items += random.sample(lst, n)
        # randomly select k items from the concatenated list of user items
        return random.sample(items, k)

# example usage
k = 7
user_items = choose_user_items(k, user_rated_items, user_reserved_items, user_viewed_items)
print(user_items)
