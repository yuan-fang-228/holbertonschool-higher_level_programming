-- list the number of records with the same score in second_table
-- result display with score and number of records descending
SELECT score, COUNT(score) AS number FROM second_table GROUP BY score ORDER BY number DESC;
