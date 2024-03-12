-- This script  uses the hbtn_0d_tvshows database to lists all genres of the show Dexter.
SELECT name FROM tv_genres AS a
RIGHT JOIN tv_show_genres AS b
ON a.id = b.genre_id
RIGHT JOIN tv_shows as c
ON b.show_id = c.id
WHERE c.title = 'DEXTER'
ORDER BY name ASC;
