from injest import load_data

def transform_data():
    print("Starting transformation...")

    data = load_data()

    orders = data["orders"]
    order_products = data["order_products"]
    products = data["products"]

    # Join order_products with orders
    merged = order_products.merge(
        orders,
        on="order_id",
        how="inner"
    )

    #  Join with products
    final_df = merged.merge(
        products,
        on="product_id",
        how="inner"
    )

    print(" Transformation complete!")

    return final_df


if __name__ == "__main__":
    df = transform_data()

    print("\nPreview:")
    print(df.head())

df.to_csv("C:\\Users\\DELL\\OneDrive\\Desktop\\instacart_data_engineering_pipeline\\output\\fact_order_products.csv", index=False)
print(" Saved final dataset!")