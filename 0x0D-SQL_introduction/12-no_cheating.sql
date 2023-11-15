-- Update the score of the record with the name 'Bob' to 10
UPDATE `second_table`
SET
`score` = 10
WHERE `second_table` . `name` = 'Bob';
