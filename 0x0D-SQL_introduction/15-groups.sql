-- Count occurrences of each score in second_table, grouped by the score. 
-- Provides a summary of how many times each score appears in the dataset.
SELECT score, COUNT(*) AS number
FROM second_table
GROUP BY score
ORDER BY number DESC;
