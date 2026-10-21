moscow = {201, 202, 203, 204}
kazan = {203, 204, 205, 206}

in_both_cities = moscow.intersection(kazan)
only_moscow = moscow.difference(kazan)
only_kazan = kazan.difference(moscow)
all_products_count = len(moscow.union(kazan))

print("Есть в обоих городах:", in_both_cities)
print("Только в Москве:", only_moscow)
print("Только в Казани:", only_kazan)
print("Количество разных товаров:", all_products_count)
