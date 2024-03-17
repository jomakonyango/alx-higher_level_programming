-- Lists all records of the table second_table ordered by score (top first)
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
