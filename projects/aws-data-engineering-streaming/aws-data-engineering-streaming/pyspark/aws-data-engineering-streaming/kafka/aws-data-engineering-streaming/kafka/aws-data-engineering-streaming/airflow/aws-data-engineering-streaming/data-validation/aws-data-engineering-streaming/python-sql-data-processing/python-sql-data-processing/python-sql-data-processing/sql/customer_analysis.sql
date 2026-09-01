-- Total revenue by customer

SELECT
    customer_id,
    SUM(amount) AS total_revenue
FROM transactions
GROUP BY customer_id
ORDER BY total_revenue DESC;
