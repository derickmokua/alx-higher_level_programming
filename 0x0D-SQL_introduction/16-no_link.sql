-- Display records from second_table with non-null names, sorted by score. 
-- Filters out entries where the name is NULL and presents the results in ascending order of the score.
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
