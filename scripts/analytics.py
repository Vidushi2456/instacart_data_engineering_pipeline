from transform import transform_data

def run_analytics():
    print("🚀 Starting analytics...")

    df = transform_data()

    print("📊 Data loaded. Shape:", df.shape)

    top_products = df.groupby("product_name")["order_id"].count().sort_values(ascending=False).head(10)
    
    print("\n🔥 Top Products:")
    print(top_products)

    reorder_products = df.groupby("product_name")["reordered"].sum().sort_values(ascending=False).head(10)

    print("\n🔁 Most Reordered:")
    print(reorder_products)

    top_products.to_csv("C:\\Users\\DELL\\OneDrive\\Desktop\\instacart_data_engineering_pipeline\\output\\top_products.csv")
    reorder_products.to_csv("C:\\Users\\DELL\\OneDrive\\Desktop\\instacart_data_engineering_pipeline\\output\\top_reordered_products.csv")

    print("\n✅ Analytics completed and files saved!")


if __name__ == "__main__":
    run_analytics()
