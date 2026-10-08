from collections import Counter

queries = [
    "чехол",
    "iphone",
    "чехол",
    "наушники",
    "iphone",
    "iphone",
    "кабель",
    "чехол",
    "iphone",
]

total_queries = len(queries)
query_count = Counter(queries)
most_common_query, most_common_count = query_count.most_common(1)[0]
most_common_share = most_common_count / total_queries
single_queries = [query for query in queries if query_count[query] == 1]

print("Всего запросов:", total_queries)
print("Количество каждого запроса:", query_count)
print("Самый частый запрос:", most_common_query)
print("Количество:", most_common_count)
print("Доля:", most_common_share)
print("Запросы, встретившиеся один раз:", single_queries)
