-- This script lists all shows contained in hbtn_0d_tvshows without a genre linked
SELECT a.title, b.genre_id FROM tv_shows AS a
CROSS JOIN tv_show_genres AS b
ON a.id = b.show_id
WHERE b.genre_id = NULL;
