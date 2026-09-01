-- Find duplicate transaction IDs

SELECT
    transaction_id,
    COUNT(*) AS record_count
FROM transactions
GROUP BY transaction_id
HAVING COUNT(*) > 1;


-- Find transactions with missing customer IDs

SELECT *
FROM transactions
WHERE customer_id IS NULL;
