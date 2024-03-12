-- This script lists all genres in the database hbtn_0d_tvshows_rate by their rating.
SELECT d.name AS name, SUM(b.rate) AS rating 
FROM tv_shows AS a
JOIN tv_show_ratings AS b
ON a.id = b.show_id
JOIN tv_show_genres AS c
ON b.show_id = c.show_id
JOIN tv_genres AS d
ON c.genre_id = d.id
GROUP BY name
ORDER BY rating DESC;
