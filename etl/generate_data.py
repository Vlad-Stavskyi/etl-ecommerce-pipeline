import pandas as pd
import random
from faker import Faker

fake = Faker()


def generate_orders(n=100):
    orders = []

    for _ in range(n):
        orders.append({
            "order_id": fake.uuid4(),
            "user_id": random.randint(1, 100),
            "product_id": random.randint(1, 200),
            "price": round(random.uniform(10, 500), 2),
            "quantity": random.randint(1, 5),
            "order_date": fake.date_this_year()
        })

    return pd.DataFrame(orders)


def main():
    df = generate_orders(200)

    # TODO: save data to data/ folder later
    df.to_csv("orders.csv", index=False)

    print(f"Generated {len(df)} orders")


if __name__ == "__main__":
    main()