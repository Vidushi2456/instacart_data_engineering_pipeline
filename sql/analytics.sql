-- Top Products
SELECT product_name, COUNT(order_id) AS total_orders
FROM fact_order_products
GROUP BY product_name
ORDER BY total_orders DESC
LIMIT 10;

-- Most Reordered
SELECT product_name, SUM(reordered) AS reorder_count
FROM fact_order_products
GROUP BY product_name
ORDER BY reorder_count DESC
LIMIT 10;