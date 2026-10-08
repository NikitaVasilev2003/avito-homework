from collections import defaultdict

reviews = [
    {"id": 1, "product": "Чехол", "stars": 5},
    {"id": 1, "product": "Чехол", "stars": 3},
    {"id": 1, "product": "Чехол", "stars": 4},
    {"id": 2, "product": "Наушники", "stars": 2},
    {"id": 2, "product": "наушники", "stars": 2},
    {"id": 2, "product": "НАУШНИКИ", "stars": 5},
    {"id": 3, "product": "Планшет", "stars": 5},
    {"id": 4, "product": "Колонка", "stars": 4},
    {"id": 4, "product": "Колонка", "stars": 4},
    {"id": 5, "product": "Кабель", "stars": 1},
]

for review in reviews:
    review["product"] = review["product"].lower()

stars_by_product = defaultdict(list)
for review in reviews:
    stars_by_product[review["product"]].append(review["stars"])

avg_stars = {
    product: sum(stars) / len(stars) for product, stars in stars_by_product.items()
}

products_with_two_reviews = {
    product: avg_stars[product]
    for product, stars in stars_by_product.items()
    if len(stars) >= 2
}

worst_product = min(
    products_with_two_reviews, key=lambda product: products_with_two_reviews[product]
)

low_reviews_count = 0
all_count = len(reviews)
for review in reviews:
    low_reviews_count += review["stars"] <= 2
low_reviews_share = low_reviews_count / all_count

print("Средняя оценка каждого товара:", avg_stars)
print("Худший товар:", worst_product)
print("Его средняя оценка:", avg_stars[worst_product])
print("Количество отзывов на 1 или 2 звезды:", low_reviews_count)
print("Доля таких отзывов:", low_reviews_share)
