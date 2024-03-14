-- This script lists all genres not linked to the show Dexter from the database hbtn_0d_tvshows.
-- Each record displays: tv_genres.name
-- Results are sorted in ascending order by the genre name.

SELECT tv_genres.name
FROM tv_genres
WHERE tv_genres.id NOT IN (
	    SELECT tv_show_genres.tv_genre_id
	    FROM tv_show_genres
	    JOIN tv_shows ON tv_shows.id = tv_show_genres.tv_show_id
	    WHERE tv_shows.title = 'Dexter'
)
ORDER BY tv_genres.name ASC;
