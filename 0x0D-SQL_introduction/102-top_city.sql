-- displays the top 3 of cities temperature during July and August ordered by temperature
SELECT city, DISTINCT TOP 3 AVG(value) AS avg_temp from temperatures WHERE month = 7 or month = 8 GROUP BY city ORDER BY avg_temp DESC;
