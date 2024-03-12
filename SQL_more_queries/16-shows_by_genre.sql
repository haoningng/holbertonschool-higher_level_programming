-- This script lists all shows, and all genres linked to that show, from the database hbtn_0d_tvshows.
SELECT c.title AS title, a.name AS name FROM tv_genres AS a
RIGHT JOIN tv_show_genres AS b
ON a.id = b.genre_id
RIGHT JOIN tv_shows AS c
ON b.show_id = c.id
ORDER BY title, name ASC;
