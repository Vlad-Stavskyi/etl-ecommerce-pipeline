import pandas as pd


def transform_orders(input_path="orders.csv", output_path="daily_sales.csv"):
    df = pd.read_csv(input_path)

    df = df.dropna(subset=["order_id", "price", "quantity", "order_date"])
    df = df[df["price"] > 0]
    df = df[df["quantity"] > 0]

    df["order_date"] = pd.to_datetime(df["order_date"])
    df["revenue"] = df["price"] * df["quantity"]

    daily_sales = (
        df.groupby(df["order_date"].dt.date)
        .agg(
            orders_count=("order_id", "count"),
            total_revenue=("revenue", "sum")
        )
        .reset_index()
    )

    # TODO: later round revenue at the reporting layer
    daily_sales.to_csv(output_path, index=False)

    print(f"Saved transformed data to {output_path}")


def main():
    transform_orders()


if __name__ == "__main__":
    main()