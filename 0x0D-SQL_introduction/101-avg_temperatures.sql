-- import in hbtn_0c_0 database temperatures table
-- script that displays the average temperature by city ordered by temp
SELECT city, AVG(value) AS avg_temp FROM temperatures
GROUP BY city
ORDER BY avg_temp DESC;
