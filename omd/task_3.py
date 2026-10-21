orders = [
    {"id": 1, "buyer": "anya", "status": "delivered", "amount": 900},
    {"id": 2, "buyer": "boris", "status": "returned", "amount": 4_500},
    {"id": 3, "buyer": "anya", "status": "delivered", "amount": 1_500},
    {"id": 4, "buyer": "vera", "status": "delivered", "amount": 3_200},
    {"id": 5, "buyer": "boris", "status": "delivered", "amount": 700},
    {"id": 6, "buyer": "gleb", "status": "returned", "amount": 2_100},
]

returned_amount = sum(
    order["amount"] for order in orders if order["status"] == "returned"
)
returned_buyers = {order["buyer"] for order in orders if order["status"] == "returned"}
delivered_orders = [order for order in orders if order["status"] == "delivered"]
delivered_count = len(delivered_orders)
delivered_amount = sum(order["amount"] for order in delivered_orders)
avg_delivered_check = delivered_amount / delivered_count

print("Сумма возвратов:", returned_amount)
print("Кто возвращал заказ:", returned_buyers)
print("Количество доставленных заказов:", delivered_count)
print("Средний чек доставленных заказов:", avg_delivered_check)
