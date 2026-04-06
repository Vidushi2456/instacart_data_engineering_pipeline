from injest import load_data

def transform_data():
    print("Starting transformation...")

    data = load_data()

    # ✅ FIRST extract data
    orders = data["orders"]
    order_products = data["order_products"]
    products = data["products"]

    # ✅ THEN clean columns
    orders.columns = orders.columns.str.strip().str.lower()
    order_products.columns = order_products.columns.str.strip().str.lower()
    products.columns = products.columns.str.strip().str.lower()

    # ✅ THEN fix datatypes
    orders["order_id"] = orders["order_id"].astype(int)
    order_products["order_id"] = order_products["order_id"].astype(int)

    products["product_id"] = products["product_id"].astype(int)
    order_products["product_id"] = order_products["product_id"].astype(int)

    # ✅ DEBUG (IMPORTANT)
    print("orders shape:", orders.shape)
    print("order_products shape:", order_products.shape)
    print("products shape:", products.shape)

    # Join
    merged = order_products.merge(orders, on="order_id", how="inner")
    print("after first merge:", merged.shape)

    final_df = merged.merge(products, on="product_id", how="inner")
    print("after second merge:", final_df.shape)

    print("Transformation complete!")

    return final_df


if __name__ == "__main__":
    df = transform_data()

    print("\nPreview:")
    print(df.head())

    df.to_csv("C:\\Users\\DELL\\OneDrive\\Desktop\\instacart_data_engineering_pipeline\\output\\fact_order_products.csv", index=False)
    print("Saved final dataset!")