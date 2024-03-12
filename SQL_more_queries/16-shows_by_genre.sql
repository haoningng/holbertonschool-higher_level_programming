-- This script lists all shows, and all genres linked to that show, from the database hbtn_0d_tvshows.
SELECT c.title AS title, a.name AS name FROM tv_genres AS a
CROSS JOIN tv_show_genres AS b
ON a.id = b.genre_id
CROSS JOIN tv_shows AS c
ON b.show_id = c.id
ORDER BY title, name ASC;
