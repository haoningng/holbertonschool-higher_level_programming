-- This script lists all shows from hbtn_0d_tvshows_rate by their rating.
SELECT a.title AS title, SUM(b.rate) AS rating 
FROM tv_shows AS a
JOIN tv_show_ratings AS b
ON a.id = b.show_id
GROUP BY title
ORDER BY rating DESC;
