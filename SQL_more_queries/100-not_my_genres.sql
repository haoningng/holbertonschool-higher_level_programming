-- This script uses the hbtn_0d_tvshows database to list all genres not linked to the show Dexter
SELECT name FROM tv_genres 
WHERE name NOT IN (
    SELECT a.name AS name FROM tv_genres AS a
    RIGHT JOIN tv_show_genres AS b
    ON a.id = b.genre_id
    RIGHT JOIN tv_shows AS c
    ON b.show_id = c.id
    WHERE c.title = 'DEXTER'
    ORDER BY name ASC
);

