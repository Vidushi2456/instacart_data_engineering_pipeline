import pandas as pd

DATA_PATH = "C:/Users/DELL/OneDrive/Desktop/instacart_data_engineering_pipeline/data/"

def load_data():
    print("Starting data ingestion...")

    orders = pd.read_csv(DATA_PATH + "orders_sample.csv")
    order_products = pd.read_csv(DATA_PATH + "order_products__prior_sample.csv")
    products = pd.read_csv(DATA_PATH + "products_sample.csv")
    aisles = pd.read_csv(DATA_PATH + "aisles_sample.csv")
    departments = pd.read_csv(DATA_PATH + "departments_sample.csv")

    print("All datasets loaded successfully!\n")

    return {
        "orders": orders,
        "order_products": order_products,
        "products": products,
        "aisles": aisles,
        "departments": departments
    }


if __name__ == "__main__":
    data = load_data()

    # preview one dataset
    print("Orders Preview:")
    print(data["orders"].head())