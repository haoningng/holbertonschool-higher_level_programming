-- This script lists all shows without the genre Comedy in the database hbtn_0d_tvshows.
SELECT title FROM tv_shows 
WHERE title NOT IN (
    SELECT c.title FROM tv_genres AS a
    RIGHT JOIN tv_show_genres AS b
    ON a.id = b.genre_id
    RIGHT JOIN tv_shows AS c
    ON b.show_id = c.id
    WHERE a.name = 'COMEDY'
)
GROUP BY title
ORDER BY title ASC;
