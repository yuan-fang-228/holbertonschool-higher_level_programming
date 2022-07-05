-- display all the records of second_table
-- don't list rows without a name value
SELECT score, name FROM second_table WHERE name != "" ORDER BY score DESC;
