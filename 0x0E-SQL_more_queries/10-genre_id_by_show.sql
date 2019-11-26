-- script that lists all shows contained in hbtn_0d_tvshows that have at least one genre linked.
SELECT tv_shows.title AS title, tv_show_genres.genre_id AS genre_id
FROM tv_show_genres
RIGHT JOIN tv_shows
ON tv_show_genres.show_id = tv_shows.id
WHERE tv_show_genres.show_id IS NOT NULL
ORDER BY title, genre_id;
