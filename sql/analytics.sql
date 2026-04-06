--top selling products
df.groupby("product_name")["order_id"].count().sort_values(ascending=False).head(10);
--most reordered products
df.groupby("product_name")["reordered"].sum().sort_values(ascending=False).head(10);
--peak order hour
df.groupby("order_hour_of_day")["order_id"].count().sort_values(ascending=False);
--orders per user
df.groupby("order_hour_of_day")["order_id"].count().sort_values(ascending=False);