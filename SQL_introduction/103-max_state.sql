-- This script displays the max temperature of each state (ordered by State name).
USE hbtn_0c_0;
SOURCE temperatures.sql;

SELECT state, MAX(value) as max_temp
FROM temperatures
GROUP BY state
ORDER BY state ASC;