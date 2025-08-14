-- script that displays the max temperature of each state
SELECT state, AVG(value) AS max_temp
FROM temperatures
GROUP BY state
ORDER BY state;
