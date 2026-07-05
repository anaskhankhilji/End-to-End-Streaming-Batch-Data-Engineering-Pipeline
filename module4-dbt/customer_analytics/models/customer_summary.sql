WITH orders AS (
    SELECT
        customer,
        COUNT(*) AS total_orders,
        SUM(amount) AS total_spent,
        AVG(amount) AS avg_order_value
    FROM {{ source('raw_data', 'orders') }}
    GROUP BY customer
)

SELECT
    customer,
    total_orders,
    total_spent,
    avg_order_value
FROM orders
ORDER BY total_spent DESC
