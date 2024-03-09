-- This script creates a table second_table in the database hbtn_0c_0 in your MySQL server and add multiples rows.
CREATE TABLE IF NOT EXISTS second_table (id INT, name VARCHAR(256), score INT)

SELECT 1 AS id, "John" AS name, 10 AS score
UNION ALL
SELECT 2 AS id, "Alex" AS name, 3 AS score
UNION ALL
SELECT 3 AS id, "Bob" AS name, 14 AS score
UNION ALL
SELECT 4 AS id, "George" AS name, 8 AS score
